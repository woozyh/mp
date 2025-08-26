#!/usr/bin/python3.12.3


from os import path
from ui import resources
from random import shuffle
from ui.MusicPlayerUi import MusicPlayerUi
from src import (
    dataBase,
    infoExtractor,
)
from time import (
    strftime,
    localtime,
)
from PySide6.QtCore import (
    Qt,
    QUrl,
    QTime,
    QTimer,
)
from PySide6.QtGui import (
    QPixmap,
    QMouseEvent,
)
from PySide6.QtWidgets import(
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QInputDialog,
    QApplication,
)
from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
)


class Player(QMainWindow):


    STATUS: dict[str, bool] = {
        "shuffled": False,
        "looped": False,
    }
    INITIAL_VOLUME: int = 50
    CURRENT_PLAYLIST: list[str] = list()
    CURRENT_PLAYLIST_NAME: str = "Global"
    FAVORITE_PLAYLIST: list[str] = list()
    
    
    def __init__(self,) -> None:
        """initializig the Player class."""

        super().__init__()

        # instantiating from DataBase
        self.db = dataBase.DataBase()

        # add MusicPlayerUi to main window
        self.musicPlayerWindow = MusicPlayerUi()
        self.musicPlayerWindow.setupUi(self)

        # remove the title bar from window 
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # setting the status
        self.STATUS = {
            "looped": False,
            "shuffled": False,
        }
        
        # set the initial window position
        self.initialPosition = self.pos()

        # setting timer for song time line
        self.timer = QTimer()
        self.timer.start(500)
        self.timer.timeout.connect(self.timeLineHandler)
        
        # set events
        self.musicPlayerWindow.titleFrame.mouseMoveEvent = self.moveWindow

        # connect buttons with functions
        self.musicPlayerWindow.addSongsFromPath.clicked.connect(self.loadSongsFromPath) # add song path button
        self.musicPlayerWindow.playButton.clicked.connect(self.streamSong) # song play button
        self.musicPlayerWindow.pauseButton.clicked.connect(self.pauseOrUnPuase) # puase button
        self.musicPlayerWindow.nextButton.clicked.connect(self.playNextSong) # next button
        self.musicPlayerWindow.previousButton.clicked.connect(self.playPrevSong) # previous button
        self.musicPlayerWindow.volumeUp.clicked.connect(self.increaseVolumeHandler) # increase volume slider
        self.musicPlayerWindow.volumeDown.clicked.connect(self.decreaseVolumeHandler) # decrease volume slide
        self.musicPlayerWindow.songTimeLine.sliderMoved.connect(self.changeTimeLine) # changing the time line of current song
        self.musicPlayerWindow.shuffleButton.clicked.connect(self.shufflePlayList) # changin the state of shuffling 
        self.musicPlayerWindow.loopButton.clicked.connect(self.loopOnSong) # cahnging the state of looping
        self.musicPlayerWindow.playListWidget.itemClicked.connect(self.loadPlayList) # loading play list
        self.musicPlayerWindow.removeFromPlayList.clicked.connect(self.removeSongFromPlayList) # removing song from playlist
        self.musicPlayerWindow.addNewPlayList.clicked.connect(self.addNewPlayList) # adding new playlist
        self.musicPlayerWindow.removePlayList.clicked.connect(self.deletePlayList) # removing the playlist
        self.musicPlayerWindow.addToFavoriteButton.clicked.connect(self.addSongToFavorite) # adding song to favorites playlist
        self.musicPlayerWindow.addToPlayList.clicked.connect(self.addSongToPlayList) # adding song to a playlist
        
        # connect volume slider with volumeHandler
        self.musicPlayerWindow.volumeSlider.valueChanged.connect(self.volumeHandler)
        
        # setting the player and audio output
        self.audio  = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.INITIAL_VOLUME)
        self.musicPlayerWindow.volumeSlider.setValue(self.INITIAL_VOLUME)

        # load available playlists
        self.listPlayLists()
        
        # instantiating the infoExtractor
        self.songInfo = infoExtractor.Info()

        
    def moveWindow(self, mouseEvent: QMouseEvent) -> None:
        """handling mouse pressing event to move window while pressing mouse left button on titleFrame.
        Note: by default the globalPosition() returns in float but we need to convert it to int so just
        try globalPosition().toPoint().
        Note: globalPos() is outdated and gives warning and may not supported in future anymore.
        """

        if mouseEvent.buttons() == Qt.LeftButton:
            self.move(self.pos() + mouseEvent.globalPosition().toPoint() -  self.initialPosition)
            self.initialPosition = mouseEvent.globalPosition().toPoint()
            
            mouseEvent.accept()

    # over writing the mousePressEvent to move window with it
    def mousePressEvent(self, mouseEvent: QMouseEvent) -> None:
        """changing the base class methods to rewrite the mouse pressing functionality."""
        
        self.initialPosition = mouseEvent.globalPosition().toPoint()

    def loadSongsFromPath(self,) -> None:
        """loading songs from usere specified path."""

        
        pathsInTuple: list[tuple[str]] = list()
        songsPath, pattern = QFileDialog.getOpenFileNames(
            parent  = self,
            caption = 'Add songs from path',
            filter = '(*.mp3 *.MP3 *.mpeg *.ogg *.wma *.acc)', 
        )
        
        if songsPath:
            for songPath in songsPath:
                self.CURRENT_PLAYLIST.append(songPath)

                pathsInTuple.append((songPath,))
                
                self.musicPlayerWindow.listWidget.addItem(
                    f"  {path.basename(songPath)}",
                )

        self.db.executeQuery(
            query = ["Insert"],
            info = {
                "TABLE": "Global",
                "VALUES": pathsInTuple,
            },
        )
        
        self.db.executeQuery(
            query = ["Insert"],
            info = {
                "TABLE": self.CURRENT_PLAYLIST_NAME,
                "VALUES": pathsInTuple,
            },
        )

    def listPlayLists(self,) -> None:
        """listing the existing playlists from database."""

        playLists = self.db.executeQuery(
            query = ["Select", "playList"],
        )

        if playLists:
            self.musicPlayerWindow.playListWidget.addItems(list(playLists))
        
    def setSongStatus(self, status: dict, songPath: str) -> None:
        """setting the song status."""

        self.musicPlayerWindow.currentSongNameValue.setText(status['TIT2'])
        self.musicPlayerWindow.currentSongSingerValue.setText(status['TPE1'])
        self.musicPlayerWindow.currentSongAlbumValue.setText(status['TALB'])
        self.musicPlayerWindow.currentSongYearValue.setText(status['TYER'])
        self.musicPlayerWindow.currentSongPathValue.setText(songPath)

        if status['APIC'] != "N/A":
            self.musicPlayerWindow.songAPICLabel.setPixmap(QPixmap(f"./{status['APIC']}"))
        else:
            self.musicPlayerWindow.songAPICLabel.setPixmap(QPixmap("./ui/defaultApic.png"))

        self.musicPlayerWindow.songAPICLabel.setScaledContents(True)
        
    def streamSong(self,) -> None:
        """streaming the song.
        Note: the QMediaContent removed from qt6 instead using the Qurl directly is solution.
        """
        
        try:
            currentSelection = self.musicPlayerWindow.listWidget.currentRow()
            currentSongPath  = self.CURRENT_PLAYLIST[currentSelection]
            
            songMetaData = self.songInfo.process(file_path = currentSongPath)

            self.setSongStatus(status = songMetaData, songPath = currentSongPath)
            
            self.player.setSource(QUrl.fromLocalFile(currentSongPath))
            self.player.play()

        except Exception as e:
            print(f"Error: {e} on {currentSongPath} song.")
            
    def pauseOrUnPuase(self,) -> None:
        """setting the functionlity of puasing and unpausing."""

        if self.player.isPlaying():
            self.player.pause()
        else:
            self.player.play()

    def increaseVolumeHandler(self,):
        """increasing the volume."""

        currentVolume: int = self.musicPlayerWindow.volumeSlider.value()
        
        try:
            self.musicPlayerWindow.volumeSlider.setValue(currentVolume + 5)
            self.audio.setVolume(self.musicPlayerWindow.volumeSlider.value() * 0.01)
        except Exception as er:
            print(f"Error: error on increaseVolumeHandler.\n{er}")

    def decreaseVolumeHandler(self,):
        """decreasing the volume."""

        currentVolume: int = self.musicPlayerWindow.volumeSlider.value()
        
        try:
            self.musicPlayerWindow.volumeSlider.setValue(currentVolume - 5)
            self.audio.setVolume(self.musicPlayerWindow.volumeSlider.value() * 0.01)
        except Exception as er:
            print(f"Error: error on decreaseVolumeHandler.\n{er}")
            
    def volumeHandler(self,) -> None:
        """getting the value of slide after changing."""

        try:
            self.audio.setVolume(self.musicPlayerWindow.volumeSlider.value() * 0.01)
        except Exception as er:
            print(f"Error: error on volumeHandler. {er}")

    def timeLineHandler(self,) -> None:
        """handing the changes of current song time line."""

        # there is a bug in time calculation be aware
        songLength = strftime("%M:%S", localtime((self.player.duration() / 1000) - 1800))
        songCurrentTime = strftime("%M:%S", localtime((self.player.position() / 1000) - 1800))
        
        try:
            if self.player.isPlaying():
                self.musicPlayerWindow.songTimeLine.setMinimum(0)
                self.musicPlayerWindow.songTimeLine.setMaximum(self.player.duration())
                self.musicPlayerWindow.songTimeLine.setValue(self.player.position())

                self.musicPlayerWindow.currentTimeLine.setText(songCurrentTime)
                self.musicPlayerWindow.songLength.setText(songLength)

            # checking whether the song is reached the end or not
            if self.player.mediaStatus() == QMediaPlayer.MediaStatus.EndOfMedia:
                if not self.STATUS["looped"]:
                    self.playNextSong()
                else:
                    self.player.play()
            
        except Exception as er:
            print(f"Error: error on timeLineHandler.\n{er}")
        
    def changeTimeLine(self,) -> None:
        """handling the song time line while changing."""
        
        self.player.setPosition(self.musicPlayerWindow.songTimeLine.value())

    def playNextSong(self,):
        """playing the next song near current song on list."""

        try:

            numberOfRows = self.musicPlayerWindow.listWidget.count()
            currentSongIndex = self.musicPlayerWindow.listWidget.currentRow()

            if numberOfRows != (currentSongIndex + 1):
                nextSongPath = self.CURRENT_PLAYLIST[currentSongIndex + 1]
                
                self.musicPlayerWindow.listWidget.setCurrentRow(currentSongIndex + 1)
                
                self.player.setSource(QUrl.fromLocalFile(nextSongPath))
                self.player.play()
            else:
                nextSongPath = self.CURRENT_PLAYLIST[0]
                
                self.musicPlayerWindow.listWidget.setCurrentRow(0)
                
                self.player.setSource(QUrl.fromLocalFile(nextSongPath))
                self.player.play()

            songMetaData = self.songInfo.process(file_path = nextSongPath)
            self.setSongStatus(status = songMetaData, songPath = nextSongPath)
                
        except Exception as er:
                print(f"Error: error on playNextSong. {er}")
                
    def playPrevSong(self,) -> None:
        """plyaing the previous song near current song on list."""

        try:
            numberOfRows = self.musicPlayerWindow.listWidget.count()
            currentSongIndex = self.musicPlayerWindow.listWidget.currentRow()
            
            if currentSongIndex != 0:
                prevSongPath = self.CURRENT_PLAYLIST[currentSongIndex - 1]

                self.musicPlayerWindow.listWidget.setCurrentRow(currentSongIndex - 1)
                
                self.player.setSource(QUrl.fromLocalFile(prevSongPath))
                self.player.play()
                
            else:
                prevSongPath = self.CURRENT_PLAYLIST[numberOfRows - 1]
                
                self.musicPlayerWindow.listWidget.setCurrentRow(numberOfRows - 1)
                    
                self.player.setSource(QUrl.fromLocalFile(prevSongPath))
                self.player.play()

            
            songMetaData = self.songInfo.process(file_path = prevSongPath)
            self.setSongStatus(status = songMetaData, songPath = prevSongPath)
            
        except Exception as er:
            print(f"Error: error on playPrevSong. {er}")

    def shufflePlayList(self,):
        """shuffling the play list."""

        if self.STATUS["shuffled"]:
            self.STATUS["shuffled"] = False
            self.CURRENT_PLAYLIST.sort()

            self.musicPlayerWindow.listWidget.clear()
            if self.CURRENT_PLAYLIST:
                for songPath in self.CURRENT_PLAYLIST:
                    self.musicPlayerWindow.listWidget.addItem(
                        f"  {path.basename(songPath)}",
                    )
        else:
            self.STATUS["shuffled"] = True
            shuffle(self.CURRENT_PLAYLIST)

            self.musicPlayerWindow.listWidget.clear()
            if self.CURRENT_PLAYLIST:
                for songPath in self.CURRENT_PLAYLIST:
                    self.musicPlayerWindow.listWidget.addItem(
                        f"  {path.basename(songPath)}",
                    )
            
    def loopOnSong(self,):
        """looping on song."""
        
        if self.STATUS["looped"]:
            self.STATUS["looped"] = False

        else:
            self.STATUS["looped"] = True

    def addSongToFavorite(self,) -> None:
        """adding currently streaming song to Favorites list."""

        currentSongIndex = self.musicPlayerWindow.listWidget.currentRow()
        
        self.db.executeQuery(
            query = ["Insert"],
            info = {
                "TABLE": "Favorites",
                "VALUES": [(self.CURRENT_PLAYLIST[currentSongIndex],)],
            },
        )
        
    def addSongToPlayList(self,) -> None:
        """adding currently playing song to another playlist."""

        currentSongIndex = self.musicPlayerWindow.listWidget.currentRow()      
        path = self.CURRENT_PLAYLIST[currentSongIndex]
        numberOfPlayLists = self.musicPlayerWindow.playListWidget.count()
        
        destinationPlayList, result = QInputDialog.getText(
            self,
            "destination playlist",
            "Enter name of playlist",
        )

        if destinationPlayList and result:
            playLists = []
            for _ in range(numberOfPlayLists):
                playLists.append(
                    self.musicPlayerWindow.playListWidget.item(_).text()
                )
            if destinationPlayList in playLists:
                self.db.executeQuery(
                    query = ["Insert"],
                    info = {
                        "TABLE": destinationPlayList,
                        "VALUES": [(path,),],
                    },
                )
            else:
                QMessageBox.question(
                    self,
                    "Alert",
                    "This playlist is not available.",
                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok,
                )
        
    def addNewPlayList(self,) -> None:
        """creating new play list."""

        playListName, result = QInputDialog.getText(
            self,
            "Create new playlist",
            "Enter playlist name",
        )

        if playListName and result:
            if playListName not in ("Global", "Favorites"):
                self.db.executeQuery(
                    query = ["Create"],
                    info = {"TABLE": playListName},
                )
                self.musicPlayerWindow.playListWidget.addItem(playListName)
            else:
                QMessageBox.question(
                    self,
                    "Alert",
                    "This play list already exists.",
                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok,
                )
        
    def loadPlayList(self, item) -> None:
        """loading the clicked play list for user."""

        itemText: str = item.text()

        self.CURRENT_PLAYLIST_NAME = itemText
        
        self.musicPlayerWindow.listWidget.clear()

        songsPath = self.db.executeQuery(
            query = ["Select", "song"],
            info = {"TABLE": self.CURRENT_PLAYLIST_NAME},
        )
        
        if songsPath:
            self.CURRENT_PLAYLIST = list(songsPath)
            
            for paths in self.CURRENT_PLAYLIST:
                self.musicPlayerWindow.listWidget.addItem(
                    f"  {path.basename(paths)}",
                )

    def deletePlayList(self,) -> None:
        """deleting playlist."""

        try:

            if self.CURRENT_PLAYLIST_NAME not in ("Global", "Favorites"):
                alertQuestion = QMessageBox.question(
                    self,
                    "delete playlist",
                    f"Are you sure you want to delete {self.CURRENT_PLAYLIST_NAME} from playlists.",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
                )
                if alertQuestion == QMessageBox.StandardButton.Yes:
                    self.db.executeQuery(
                        query = ["Delete", "playList"],
                        info = {"TABLE": self.musicPlayerWindow.playListWidget.currentItem().text()},
                    )
                    self.musicPlayerWindow.playListWidget.takeItem(
                        self.musicPlayerWindow.playListWidget.currentRow(),
                    )
                    self.musicPlayerWindow.listWidget.clear()
                    self.CURRENT_PLAYLIST.clear()

                    self.player.stop()
                    
                else:
                    pass
            else:
                QMessageBox.question(
                    self,
                    "Alert",
                    f"Sorry, but you can't delete {self.CURRENT_PLAYLIST_NAME}",
                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok,
                )
                
        except Exception as er:
            print(f"Error: error on deletePlayList. {er}")

    def removeSongFromPlayList(self,) -> None:
        """removing song from playlist."""

        if len(self.CURRENT_PLAYLIST) != 0:

            try:

                currentSongIndex = self.musicPlayerWindow.listWidget.currentRow()
                
                self.musicPlayerWindow.listWidget.takeItem(currentSongIndex)
                self.db.executeQuery(
                    query = ["Delete", "song"],
                    info = {
                        "TABLE": self.musicPlayerWindow.playListWidget.currentItem().text(),
                        "PATH": self.CURRENT_PLAYLIST[currentSongIndex],
                    },
                )
                self.CURRENT_PLAYLIST.pop(currentSongIndex)

                self.afterSongRemoveAction()
                
            except Exception as er:
                print(f"Error: error on removeSongFromPlayList. {er}")
        else:
            QMessageBox.question(
                self,
                "Alert",
                f"The list is empty.",
                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok,
            )

    def afterSongRemoveAction(self,) -> None:
        """setting some values to default after the song deletion."""
        try:
            self.player.stop()
            self.musicPlayerWindow.songAPICLabel.clear()
            self.musicPlayerWindow.currentSongNameValue.setText("N/A")
            self.musicPlayerWindow.currentSongSingerValue.setText("N/A")
            self.musicPlayerWindow.currentSongAlbumValue.setText("N/A")
            self.musicPlayerWindow.currentSongYearValue.setText("N/A")
            self.musicPlayerWindow.currentSongPathValue.setText("N/A")
            self.musicPlayerWindow.currentTimeLine.setText("00:00")
            self.musicPlayerWindow.songLength.setText("00:00")
            self.musicPlayerWindow.songTimeLine.setValue(0)
        except Exception as er:
            print(f"Error: error on afterSongRemoveAction. {er}")
        
if __name__ == "__main__":

    app = QApplication([])
    window = Player()
    window.show()
    app.exec()
    
