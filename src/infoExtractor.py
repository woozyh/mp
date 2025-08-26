#!/usr/bin/python3.12.3

from os import path
from os import listdir


class Info(object):

    # the frames that stored are those which helpfull not all.
    FRAMES: dict[str, str | bytes] = {
        "TIT2": "N/A",
        "TPE1": "N/A",
        "TALB": "N/A",
        "TYER": "N/A",
        "APIC": "N/A",
        "TCON": "N/A",
    }
    MAGIC_NUMBERS: list[str] = ["fffb", "494433"]
    
    def __init__(self,):
        """Initializing the Info calss."""

        self.isValid: bool = None
        self.fileType: str = None
        self.fileCursor: BufferedReader = None
        
    def process(self, file_path: str) -> None:
        """processing the file."""

        songFrames = self.FRAMES.copy()
        
        try:
            self.fileCursor = open(file_path, "rb")
            self.fileType = self.fileCursor.read(3).hex()
            self.isValid  = self.validateFile()
            self.fileSize = path.getsize(file_path)

            if self.isValid:
                self.readHeader()
                if self.id3Version == b'\x03\x00' or b'\x04\x00':
                    songFrames = self.findFrames()
                    print("songFrames: ", songFrames)
                    songFrames = self.exportImage(song_frames = songFrames)
                    self.closeFile()
            else:
                print(f"This {file_path} song doesn't support id3Tag.")
            
        except (FileNotFoundError, IsADirectoryError) as er:
            pass
        
        return songFrames
        
    def validateFile(self,):
        """Validating file with magicNumber."""

        return True if (self.fileType or self.fileType[:4]) in self.MAGIC_NUMBERS else False
        
    def readHeader(self,):
        """Reading the specified file."""
        
        self.id3Version: bytes = self.fileCursor.read(2)
        self.id3Flags: bytes = self.fileCursor.read(1)
        self.id3Size: int = int.from_bytes(self.fileCursor.read(4))
        
    def findFrames(self,) -> dict:
        """Matching each fram from specified file."""

        currentSongFrames = self.FRAMES.copy()
        keys  = self.FRAMES.keys()
        
        while self.fileCursor.tell() < self.id3Size < self.fileSize:
            
            frameName  = self.fileCursor.read(4).decode('utf-8', errors='ignore')
            frameSize  = int.from_bytes(self.fileCursor.read(4))
            frameFlags = self.fileCursor.read(2)

            if frameName in keys:
                if frameName != 'APIC':
                    info = ""                  
                    for char in self.fileCursor.read(frameSize):
                        if char == 32 or 64 < char < 123 or 47 < char < 58:
                            info += chr(char)
                    currentSongFrames[frameName] = info
                    
                else:
                    currentSongFrames[frameName] = f"{self.fileCursor.tell()}_{frameSize}"
                    self.fileCursor.seek(self.fileCursor.tell()+frameSize)
            else:
                self.fileCursor.seek(self.fileCursor.tell() + frameSize)

        return currentSongFrames
    
    def exportImage(self, song_frames: dict) -> None:
        """exporting the image from current song based on APIC frame, if exists."""
        
        byte: bytes = bytes()
        mimeType: str = str()
        seekSize: str = str()
        readSize: str = str()

        if song_frames["APIC"] != "N/A":
            seekSize, readSize = song_frames["APIC"].split('_')
            
            if int(readSize) > 66:
                self.fileCursor.seek(int(seekSize))
                
                while True:
                    byte = self.fileCursor.read(1)
                    
                    if byte == b"\xff":
                        
                        if self.fileCursor.read(2) == b"\xd8\xff":
                            mimeType = "jpg"
                            self.fileCursor.seek(self.fileCursor.tell()-3)
                            break
                        else:
                            self.fileCursor.seek(self.fileCursor.tell()-2)
                            continue
                        
                    elif byte == b"\x89":
                        
                        if self.fileCursor.read(7) == b"\x50\x4e\x47\x0d\x0a\x1a\x0a":
                            mimeType = "png"
                            self.fileCursor.seek(self.fileCursor.tell()-8)
                            break
                        else:
                            self.fileCursor.seek(self.fileCursor.tell()-7)
                            continue

                with open(f"APIC.{mimeType}", "wb") as img:
                    img.write(self.fileCursor.read(int(readSize)))
                    img.close()
                    
                    del img
                    
                    song_frames['APIC'] = f"APIC.{mimeType}"
                    
                    return song_frames
                
    def closeFile(self,):
        """Closing the specified file and go for another."""

        self.fileCursor.close()
        self.fileCursor = None
                
