#!/usr/bin/python3.12.3

from os import path
from os import listdir


class Info(object):

    # the frames that stored are those which helpfull not all.
    FRAMES: dict[bytes, str] = {
        "TIT2": "",
        "TPE1": "",
        "TALB": "",
        "TYER": "",
        "APIC": "",
        "TCON": "",
    }
    MAGIC_NUMBERS: list[str] = ["fffb", "494433"]
    
    def __init__(self, file_path: str):
        """Initializing the Info calss."""

        self.isValid: bool = None
        self.fileType: str = None
        self.fileCursor: BufferedReader = None
        
        try:

            self.fileCursor = open(file_path, "rb")
            self.fileType   = self.fileCursor.read(3).hex()
            self.isValid    = self.validateFile()
            self.fileSize   = path.getsize(file_path)
            
        except (FileNotFoundError, IsADirectoryError) as er:
            pass            

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

        self.currentSongFrame = self.FRAMES.copy()
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
                    self.currentSongFrame[frameName] = info
                    
                else:
                    self.currentSongFrame[frameName] = f"{self.fileCursor.tell()}_{frameSize}"
                    self.fileCursor.seek(self.fileCursor.tell()+frameSize)
            else:
                self.fileCursor.seek(self.fileCursor.tell()+frameSize)

        return self.currentSongFrame

    def closeFile(self,):
        """Closing the specified file and go for another."""

        self.fileCursor.close()
        self.fileCursor = None
        
    def exportImage(self,) -> None:
        """exporting the image from current song based on APIC frame, if exists."""

        byte: bytes = bytes()
        mimeType: str = str()
        seekSize: str = str()
        readSize: str = str()
                
        if self.currentSongFrame["APIC"]:
            seekSize, readSize = self.currentSongFrame["APIC"].split('_')

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

            with open(f"{self.fileCursor.name}.{mimeType}", "wb") as img:
                img.write(self.fileCursor.read(int(readSize)))
                img.close()

                del img
                
    def exportXml(self,):
        """Exporting the info as a xml."""
        pass
    
if __name__ == "__main__":

    musicList = listdir("/home/woozy/Music/m/")
    musicList.sort()
    for music in musicList:
        ins = Info(f"/home/woozy/Music/m/{music}")
        if ins.isValid:
            ins.readHeader()
            if ins.id3Version == b'\x03\x00' or b'\x04\x00':
                print(music, ins.findFrames())
                ins.exportImage()
                ins.closeFile()
                del ins
                    
