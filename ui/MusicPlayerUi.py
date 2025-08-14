# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MusicPlayer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QWidget)
import resources_rc
import resources_rc

class Ui_MusicPlayer(object):
    def setupUi(self, MusicPlayer):
        if not MusicPlayer.objectName():
            MusicPlayer.setObjectName(u"MusicPlayer")
        MusicPlayer.resize(1000, 600)
        MusicPlayer.setMinimumSize(QSize(1000, 600))
        MusicPlayer.setMaximumSize(QSize(1000, 600))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaTape))
        MusicPlayer.setWindowIcon(icon)
        self.actionplay = QAction(MusicPlayer)
        self.actionplay.setObjectName(u"actionplay")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/pase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionplay.setIcon(icon1)
        self.actionplay.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionpause = QAction(MusicPlayer)
        self.actionpause.setObjectName(u"actionpause")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionpause.setIcon(icon2)
        self.actionpause.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionNext = QAction(MusicPlayer)
        self.actionNext.setObjectName(u"actionNext")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNext.setIcon(icon3)
        self.actionNext.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionPrevious = QAction(MusicPlayer)
        self.actionPrevious.setObjectName(u"actionPrevious")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/pre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPrevious.setIcon(icon4)
        self.actionPrevious.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionAddToFavorite = QAction(MusicPlayer)
        self.actionAddToFavorite.setObjectName(u"actionAddToFavorite")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/heart-flat-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAddToFavorite.setIcon(icon5)
        self.actionAddToFavorite.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionaddToPlaylist = QAction(MusicPlayer)
        self.actionaddToPlaylist.setObjectName(u"actionaddToPlaylist")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/add-round-grey-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionaddToPlaylist.setIcon(icon6)
        self.actionaddToPlaylist.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionremoveFromPlaylist = QAction(MusicPlayer)
        self.actionremoveFromPlaylist.setObjectName(u"actionremoveFromPlaylist")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionremoveFromPlaylist.setIcon(icon7)
        self.actionremoveFromPlaylist.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionImportPath = QAction(MusicPlayer)
        self.actionImportPath.setObjectName(u"actionImportPath")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/addFromLocal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionImportPath.setIcon(icon8)
        self.actionImportPath.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.centralwidget = QWidget(MusicPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 600))
        self.centralwidget.setMaximumSize(QSize(1000, 600))
        self.backgroundColor = QLabel(self.centralwidget)
        self.backgroundColor.setObjectName(u"backgroundColor")
        self.backgroundColor.setGeometry(QRect(0, 0, 1000, 600))
        self.backgroundColor.setStyleSheet(u"background-color: rgb(29, 37, 51);")
        self.titleFrame = QFrame(self.centralwidget)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(0, 0, 1000, 42))
        self.titleFrame.setMinimumSize(QSize(0, 0))
        self.titleFrame.setStyleSheet(u"background-color: rgba(35, 45, 60, 220);\n"
"")
        self.titleFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.appIcon = QLabel(self.titleFrame)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setGeometry(QRect(0, 3, 40, 31))
        self.appIcon.setPixmap(QPixmap(u":/icons/icons/app_icon.png"))
        self.appName = QLabel(self.titleFrame)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(40, 9, 111, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.appName.setFont(font)
        self.appName.setStyleSheet(u"color: white;")
        self.appName.setTextFormat(Qt.TextFormat.PlainText)
        self.quitButton = QPushButton(self.titleFrame)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(965, 6, 31, 31))
        self.quitButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-style: insert;\n"
"	border-radius: 10px;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(100, 10, 10, 255);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quitButton.setIcon(icon9)
        self.minimizeButton = QPushButton(self.titleFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(930, 4, 31, 31))
        self.minimizeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-style: insert;\n"
"	border-radius: 10px;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/min.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeButton.setIcon(icon10)
        self.playListsAndStatusFrame = QFrame(self.centralwidget)
        self.playListsAndStatusFrame.setObjectName(u"playListsAndStatusFrame")
        self.playListsAndStatusFrame.setGeometry(QRect(10, 70, 241, 511))
        self.playListsAndStatusFrame.setStyleSheet(u"background-color: rgba(35, 45, 60, 70);\n"
"border-radius: 10px;")
        self.playListsAndStatusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.playListsAndStatusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.statusFrame = QFrame(self.playListsAndStatusFrame)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setGeometry(QRect(10, 22, 221, 221))
        self.statusFrame.setStyleSheet(u"background-color: rgb(50, 58, 69);\n"
"border-radius: 20px;")
        self.statusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.currentSongIconLabel = QLabel(self.statusFrame)
        self.currentSongIconLabel.setObjectName(u"currentSongIconLabel")
        self.currentSongIconLabel.setGeometry(QRect(10, 10, 31, 31))
        self.currentSongIconLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0 );\n"
"")
        self.currentSongIconLabel.setPixmap(QPixmap(u":/icons/icons/current-music.png"))
        self.currentSongIconLabel.setScaledContents(True)
        self.currentSongStatus = QLabel(self.statusFrame)
        self.currentSongStatus.setObjectName(u"currentSongStatus")
        self.currentSongStatus.setGeometry(QRect(40, 15, 71, 31))
        self.currentSongStatus.setFont(font)
        self.currentSongStatus.setStyleSheet(u"color: white;\n"
"background-color: rgba(255,255, 255, 0);")
        self.currentSongStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.currentSongName = QLabel(self.statusFrame)
        self.currentSongName.setObjectName(u"currentSongName")
        self.currentSongName.setGeometry(QRect(20, 56, 61, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.currentSongName.setFont(font1)
        self.currentSongName.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongName.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.currentSongSinger = QLabel(self.statusFrame)
        self.currentSongSinger.setObjectName(u"currentSongSinger")
        self.currentSongSinger.setGeometry(QRect(20, 90, 61, 16))
        self.currentSongSinger.setFont(font1)
        self.currentSongSinger.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongSinger.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.currentSongAlbum = QLabel(self.statusFrame)
        self.currentSongAlbum.setObjectName(u"currentSongAlbum")
        self.currentSongAlbum.setGeometry(QRect(20, 120, 61, 16))
        self.currentSongAlbum.setFont(font1)
        self.currentSongAlbum.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongAlbum.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.currentSongYear = QLabel(self.statusFrame)
        self.currentSongYear.setObjectName(u"currentSongYear")
        self.currentSongYear.setGeometry(QRect(20, 150, 51, 16))
        self.currentSongYear.setFont(font1)
        self.currentSongYear.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongYear.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.currentSongPath = QLabel(self.statusFrame)
        self.currentSongPath.setObjectName(u"currentSongPath")
        self.currentSongPath.setGeometry(QRect(20, 180, 51, 16))
        self.currentSongPath.setFont(font1)
        self.currentSongPath.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongPath.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.currentSongNameValue = QLabel(self.statusFrame)
        self.currentSongNameValue.setObjectName(u"currentSongNameValue")
        self.currentSongNameValue.setGeometry(QRect(80, 59, 131, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.currentSongNameValue.setFont(font2)
        self.currentSongNameValue.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongNameValue.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.currentSongSingerValue = QLabel(self.statusFrame)
        self.currentSongSingerValue.setObjectName(u"currentSongSingerValue")
        self.currentSongSingerValue.setGeometry(QRect(80, 90, 131, 16))
        self.currentSongSingerValue.setFont(font2)
        self.currentSongSingerValue.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongSingerValue.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.currentSongAlbumValue = QLabel(self.statusFrame)
        self.currentSongAlbumValue.setObjectName(u"currentSongAlbumValue")
        self.currentSongAlbumValue.setGeometry(QRect(80, 120, 131, 16))
        self.currentSongAlbumValue.setFont(font2)
        self.currentSongAlbumValue.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongAlbumValue.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.currentSongYearValue = QLabel(self.statusFrame)
        self.currentSongYearValue.setObjectName(u"currentSongYearValue")
        self.currentSongYearValue.setGeometry(QRect(80, 150, 131, 16))
        self.currentSongYearValue.setFont(font2)
        self.currentSongYearValue.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongYearValue.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.currentSongPathValue = QLabel(self.statusFrame)
        self.currentSongPathValue.setObjectName(u"currentSongPathValue")
        self.currentSongPathValue.setGeometry(QRect(80, 180, 131, 16))
        self.currentSongPathValue.setFont(font2)
        self.currentSongPathValue.setStyleSheet(u"color: rgb(190, 190, 190);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.currentSongPathValue.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.playListFrame = QFrame(self.playListsAndStatusFrame)
        self.playListFrame.setObjectName(u"playListFrame")
        self.playListFrame.setGeometry(QRect(10, 261, 221, 231))
        self.playListFrame.setStyleSheet(u"background-color: rgb(50, 58, 69);\n"
"border-raduis: 20px;")
        self.playListFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.playListFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.playListIcon = QLabel(self.playListFrame)
        self.playListIcon.setObjectName(u"playListIcon")
        self.playListIcon.setGeometry(QRect(10, 10, 31, 31))
        self.playListIcon.setStyleSheet(u"background-color: rgba(255, 255, 255, 0 );\n"
"")
        self.playListIcon.setPixmap(QPixmap(u":/icons/icons/music_list.png"))
        self.playListIcon.setScaledContents(True)
        self.playListLabel = QLabel(self.playListFrame)
        self.playListLabel.setObjectName(u"playListLabel")
        self.playListLabel.setGeometry(QRect(40, 11, 101, 31))
        self.playListLabel.setFont(font)
        self.playListLabel.setStyleSheet(u"color: white;\n"
"background-color: rgba(255,255, 255, 0);")
        self.playListLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.globalListButton = QPushButton(self.playListFrame)
        self.globalListButton.setObjectName(u"globalListButton")
        self.globalListButton.setGeometry(QRect(6, 50, 211, 20))
        self.globalListButton.setFont(font1)
        self.globalListButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.globalListButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        self.addPlayListButton = QPushButton(self.playListFrame)
        self.addPlayListButton.setObjectName(u"addPlayListButton")
        self.addPlayListButton.setGeometry(QRect(5, 72, 211, 20))
        self.addPlayListButton.setFont(font1)
        self.addPlayListButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addPlayListButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        self.currentSongFrame = QFrame(self.centralwidget)
        self.currentSongFrame.setObjectName(u"currentSongFrame")
        self.currentSongFrame.setGeometry(QRect(270, 70, 391, 511))
        self.currentSongFrame.setStyleSheet(u"background-color: rgba(35, 45, 60, 70);\n"
"border-radius: 10px;")
        self.currentSongFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.currentSongFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.songAPICFrame = QFrame(self.currentSongFrame)
        self.songAPICFrame.setObjectName(u"songAPICFrame")
        self.songAPICFrame.setGeometry(QRect(22, 12, 320, 300))
        self.songAPICFrame.setStyleSheet(u"border-radius: 15px;\n"
"border-size: 3px;\n"
"border-style: solid;\n"
"border-color: rgb(50, 58, 69);")
        self.songAPICFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.songAPICFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.controllerFrame = QFrame(self.currentSongFrame)
        self.controllerFrame.setObjectName(u"controllerFrame")
        self.controllerFrame.setGeometry(QRect(76, 429, 242, 49))
        self.controllerFrame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(50, 58, 69);")
        self.controllerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.shuffleButton = QPushButton(self.controllerFrame)
        self.shuffleButton.setObjectName(u"shuffleButton")
        self.shuffleButton.setGeometry(QRect(14, 10, 30, 30))
        self.shuffleButton.setMinimumSize(QSize(30, 30))
        self.shuffleButton.setMaximumSize(QSize(30, 30))
        self.shuffleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shuffleButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-radius: 10px;\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/play-random.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shuffleButton.setIcon(icon11)
        self.shuffleButton.setCheckable(True)
        self.previousButton = QPushButton(self.controllerFrame)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setGeometry(QRect(53, 10, 30, 30))
        self.previousButton.setMinimumSize(QSize(30, 30))
        self.previousButton.setMaximumSize(QSize(30, 30))
        self.previousButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.previousButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-radius: 10px;\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        self.previousButton.setIcon(icon4)
        self.pauseButton = QPushButton(self.controllerFrame)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(90, 10, 30, 30))
        self.pauseButton.setMinimumSize(QSize(30, 30))
        self.pauseButton.setMaximumSize(QSize(30, 30))
        self.pauseButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pauseButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-radius: 10px;\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        self.pauseButton.setIcon(icon2)
        self.playButton = QPushButton(self.controllerFrame)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setGeometry(QRect(120, 10, 30, 30))
        self.playButton.setMinimumSize(QSize(30, 30))
        self.playButton.setMaximumSize(QSize(30, 30))
        self.playButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-radius: 10px;\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        self.playButton.setIcon(icon1)
        self.nextButton = QPushButton(self.controllerFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(156, 10, 30, 30))
        self.nextButton.setMinimumSize(QSize(30, 30))
        self.nextButton.setMaximumSize(QSize(30, 30))
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-radius: 10px;\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        self.nextButton.setIcon(icon3)
        self.loopButton = QPushButton(self.controllerFrame)
        self.loopButton.setObjectName(u"loopButton")
        self.loopButton.setGeometry(QRect(199, 10, 30, 30))
        self.loopButton.setMinimumSize(QSize(30, 30))
        self.loopButton.setMaximumSize(QSize(30, 30))
        self.loopButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loopButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-radius: 10px;\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 70);\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/loop-one.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loopButton.setIcon(icon12)
        self.loopButton.setCheckable(True)
        self.timeLineFrmae = QFrame(self.currentSongFrame)
        self.timeLineFrmae.setObjectName(u"timeLineFrmae")
        self.timeLineFrmae.setGeometry(QRect(0, 370, 391, 41))
        self.timeLineFrmae.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(50, 58, 69);")
        self.timeLineFrmae.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeLineFrmae.setFrameShadow(QFrame.Shadow.Raised)
        self.songTimeLine = QSlider(self.timeLineFrmae)
        self.songTimeLine.setObjectName(u"songTimeLine")
        self.songTimeLine.setGeometry(QRect(49, 13, 287, 16))
        self.songTimeLine.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.songTimeLine.setOrientation(Qt.Orientation.Horizontal)
        self.currentTimeLine = QLabel(self.timeLineFrmae)
        self.currentTimeLine.setObjectName(u"currentTimeLine")
        self.currentTimeLine.setGeometry(QRect(10, 11, 36, 16))
        self.currentTimeLine.setStyleSheet(u"color: white;\n"
"")
        self.songLength = QLabel(self.timeLineFrmae)
        self.songLength.setObjectName(u"songLength")
        self.songLength.setGeometry(QRect(345, 12, 36, 16))
        self.songLength.setStyleSheet(u"color: white;")
        self.volumeFrame = QFrame(self.currentSongFrame)
        self.volumeFrame.setObjectName(u"volumeFrame")
        self.volumeFrame.setGeometry(QRect(350, 38, 40, 251))
        self.volumeFrame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(50, 58, 69);")
        self.volumeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.volumeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.volumeSlider = QSlider(self.volumeFrame)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setGeometry(QRect(11, 4, 17, 240))
        self.volumeSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.volumeSlider.setOrientation(Qt.Orientation.Vertical)
        self.addToFavoriteButton = QPushButton(self.currentSongFrame)
        self.addToFavoriteButton.setObjectName(u"addToFavoriteButton")
        self.addToFavoriteButton.setGeometry(QRect(190, 315, 30, 30))
        self.addToFavoriteButton.setMinimumSize(QSize(30, 30))
        self.addToFavoriteButton.setMaximumSize(QSize(30, 30))
        self.addToFavoriteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addToFavoriteButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(100, 10, 10, 255);\n"
"}\n"
"")
        self.addToFavoriteButton.setIcon(icon5)
        self.addToPlayList = QPushButton(self.currentSongFrame)
        self.addToPlayList.setObjectName(u"addToPlayList")
        self.addToPlayList.setGeometry(QRect(150, 315, 30, 30))
        self.addToPlayList.setMinimumSize(QSize(30, 30))
        self.addToPlayList.setMaximumSize(QSize(30, 30))
        self.addToPlayList.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addToPlayList.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 100);\n"
"}\n"
"")
        self.addToPlayList.setIcon(icon6)
        self.addToPlayList_2 = QPushButton(self.currentSongFrame)
        self.addToPlayList_2.setObjectName(u"addToPlayList_2")
        self.addToPlayList_2.setGeometry(QRect(356, 291, 30, 30))
        self.addToPlayList_2.setMinimumSize(QSize(30, 30))
        self.addToPlayList_2.setMaximumSize(QSize(30, 30))
        self.addToPlayList_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addToPlayList_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 100);\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/volume-silent-white-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addToPlayList_2.setIcon(icon13)
        self.addToPlayList_3 = QPushButton(self.currentSongFrame)
        self.addToPlayList_3.setObjectName(u"addToPlayList_3")
        self.addToPlayList_3.setGeometry(QRect(355, 6, 30, 30))
        self.addToPlayList_3.setMinimumSize(QSize(30, 30))
        self.addToPlayList_3.setMaximumSize(QSize(30, 30))
        self.addToPlayList_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addToPlayList_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 100);\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/volume-medium-white-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addToPlayList_3.setIcon(icon14)
        self.currentPlayListFrame = QFrame(self.centralwidget)
        self.currentPlayListFrame.setObjectName(u"currentPlayListFrame")
        self.currentPlayListFrame.setGeometry(QRect(670, 69, 321, 511))
        self.currentPlayListFrame.setStyleSheet(u"border-radius: 10px;")
        self.currentPlayListFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.currentPlayListFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.currentPlayList = QFrame(self.currentPlayListFrame)
        self.currentPlayList.setObjectName(u"currentPlayList")
        self.currentPlayList.setGeometry(QRect(5, 3, 310, 500))
        self.currentPlayList.setStyleSheet(u"background-color: rgb(50, 58, 69);\n"
"border-raduis: 20px;")
        self.currentPlayList.setFrameShape(QFrame.Shape.StyledPanel)
        self.currentPlayList.setFrameShadow(QFrame.Shadow.Raised)
        self.currentPlayListNameFrame = QFrame(self.currentPlayList)
        self.currentPlayListNameFrame.setObjectName(u"currentPlayListNameFrame")
        self.currentPlayListNameFrame.setGeometry(QRect(10, 0, 290, 50))
        self.currentPlayListNameFrame.setStyleSheet(u"background-color: rgba(100, 100, 100, 50);\n"
"border-raduis: 20px;")
        self.currentPlayListNameFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.currentPlayListNameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.addToFavoriteButton_4 = QPushButton(self.currentPlayListNameFrame)
        self.addToFavoriteButton_4.setObjectName(u"addToFavoriteButton_4")
        self.addToFavoriteButton_4.setGeometry(QRect(240, 10, 30, 30))
        self.addToFavoriteButton_4.setMinimumSize(QSize(30, 30))
        self.addToFavoriteButton_4.setMaximumSize(QSize(30, 30))
        self.addToFavoriteButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addToFavoriteButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(100, 10, 10, 255);\n"
"}\n"
"")
        self.addToFavoriteButton_4.setIcon(icon7)
        self.addToPlayList_4 = QPushButton(self.currentPlayListNameFrame)
        self.addToPlayList_4.setObjectName(u"addToPlayList_4")
        self.addToPlayList_4.setGeometry(QRect(210, 10, 30, 30))
        self.addToPlayList_4.setMinimumSize(QSize(30, 30))
        self.addToPlayList_4.setMaximumSize(QSize(30, 30))
        self.addToPlayList_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addToPlayList_4.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgba(200, 200, 200, 240);\n"
"	border-style: insert;\n"
"	background-color: rgba(35, 45, 70, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border: insert lightgray;\n"
"  	background-color: rgba(140, 140, 140, 100);\n"
"}\n"
"")
        self.addToPlayList_4.setIcon(icon8)
        self.currentPlayListNameLabel = QLabel(self.currentPlayListNameFrame)
        self.currentPlayListNameLabel.setObjectName(u"currentPlayListNameLabel")
        self.currentPlayListNameLabel.setGeometry(QRect(50, 10, 111, 31))
        self.currentPlayListNameLabel.setFont(font)
        self.currentPlayListNameLabel.setStyleSheet(u"color: white;\n"
"background-color: rgba(255,255, 255, 0);")
        self.currentPlayListNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.playListIcon_2 = QLabel(self.currentPlayListNameFrame)
        self.playListIcon_2.setObjectName(u"playListIcon_2")
        self.playListIcon_2.setGeometry(QRect(10, 10, 31, 31))
        self.playListIcon_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0 );\n"
"")
        self.playListIcon_2.setPixmap(QPixmap(u":/icons/icons/music_list.png"))
        self.playListIcon_2.setScaledContents(True)
        self.currentPlayListSongs = QLabel(self.currentPlayList)
        self.currentPlayListSongs.setObjectName(u"currentPlayListSongs")
        self.currentPlayListSongs.setGeometry(QRect(10, 60, 290, 31))
        self.currentPlayListSongs.setFont(font)
        self.currentPlayListSongs.setStyleSheet(u"color: white;\n"
"border-raduis: 20px;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"")
        self.currentPlayListSongs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.listWidget = QListWidget(self.currentPlayList)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 100, 290, 390))
        font3 = QFont()
        font3.setPointSize(11)
        self.listWidget.setFont(font3)
        self.listWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.listWidget.setStyleSheet(u"color: rgba(230, 230, 230, 220);\n"
"padding: 5px;\n"
"background-color: rgba(100, 100, 100, 70);\n"
"selection-color: rgba(250, 250, 250, 240);\n"
"selection-background-color: rgba(140, 140, 140, 70);\n"
"")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        MusicPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(MusicPlayer)
        self.minimizeButton.clicked.connect(MusicPlayer.showMinimized)
        self.quitButton.clicked.connect(MusicPlayer.close)

        QMetaObject.connectSlotsByName(MusicPlayer)
    # setupUi

    def retranslateUi(self, MusicPlayer):
        MusicPlayer.setWindowTitle(QCoreApplication.translate("MusicPlayer", u"MusicPlayer", None))
        self.actionplay.setText(QCoreApplication.translate("MusicPlayer", u"Play", None))
#if QT_CONFIG(tooltip)
        self.actionplay.setToolTip(QCoreApplication.translate("MusicPlayer", u"play", None))
#endif // QT_CONFIG(tooltip)
        self.actionpause.setText(QCoreApplication.translate("MusicPlayer", u"Pause/Unpause", None))
#if QT_CONFIG(tooltip)
        self.actionpause.setToolTip(QCoreApplication.translate("MusicPlayer", u"Pause/Unpause", None))
#endif // QT_CONFIG(tooltip)
        self.actionNext.setText(QCoreApplication.translate("MusicPlayer", u"Next", None))
#if QT_CONFIG(tooltip)
        self.actionNext.setToolTip(QCoreApplication.translate("MusicPlayer", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.actionPrevious.setText(QCoreApplication.translate("MusicPlayer", u"Previous", None))
        self.actionAddToFavorite.setText(QCoreApplication.translate("MusicPlayer", u"AddToFavorite", None))
#if QT_CONFIG(tooltip)
        self.actionAddToFavorite.setToolTip(QCoreApplication.translate("MusicPlayer", u"AddToFavorite", None))
#endif // QT_CONFIG(tooltip)
        self.actionaddToPlaylist.setText(QCoreApplication.translate("MusicPlayer", u"addToPlaylist", None))
#if QT_CONFIG(tooltip)
        self.actionaddToPlaylist.setToolTip(QCoreApplication.translate("MusicPlayer", u"addToPlaylist", None))
#endif // QT_CONFIG(tooltip)
        self.actionremoveFromPlaylist.setText(QCoreApplication.translate("MusicPlayer", u"removeFromPlaylist", None))
#if QT_CONFIG(tooltip)
        self.actionremoveFromPlaylist.setToolTip(QCoreApplication.translate("MusicPlayer", u"deleteFromPlaylist", None))
#endif // QT_CONFIG(tooltip)
        self.actionImportPath.setText(QCoreApplication.translate("MusicPlayer", u"ImportPath", None))
#if QT_CONFIG(tooltip)
        self.actionImportPath.setToolTip(QCoreApplication.translate("MusicPlayer", u"ImportPath", None))
#endif // QT_CONFIG(tooltip)
        self.backgroundColor.setText("")
        self.appIcon.setText("")
        self.appName.setText(QCoreApplication.translate("MusicPlayer", u"MsuicPlayer", None))
        self.quitButton.setText("")
        self.minimizeButton.setText("")
        self.currentSongIconLabel.setText("")
        self.currentSongStatus.setText(QCoreApplication.translate("MusicPlayer", u"Status", None))
        self.currentSongName.setText(QCoreApplication.translate("MusicPlayer", u"song : ", None))
        self.currentSongSinger.setText(QCoreApplication.translate("MusicPlayer", u"singer :", None))
        self.currentSongAlbum.setText(QCoreApplication.translate("MusicPlayer", u"album : ", None))
        self.currentSongYear.setText(QCoreApplication.translate("MusicPlayer", u"year : ", None))
        self.currentSongPath.setText(QCoreApplication.translate("MusicPlayer", u"path : ", None))
        self.currentSongNameValue.setText(QCoreApplication.translate("MusicPlayer", u"song value", None))
        self.currentSongSingerValue.setText(QCoreApplication.translate("MusicPlayer", u"singer value", None))
        self.currentSongAlbumValue.setText(QCoreApplication.translate("MusicPlayer", u"album value", None))
        self.currentSongYearValue.setText(QCoreApplication.translate("MusicPlayer", u"year value", None))
        self.currentSongPathValue.setText(QCoreApplication.translate("MusicPlayer", u"path value", None))
        self.playListIcon.setText("")
        self.playListLabel.setText(QCoreApplication.translate("MusicPlayer", u"PlayLists", None))
        self.globalListButton.setText(QCoreApplication.translate("MusicPlayer", u"Global", None))
        self.addPlayListButton.setText(QCoreApplication.translate("MusicPlayer", u"add +", None))
        self.shuffleButton.setText("")
        self.previousButton.setText("")
        self.pauseButton.setText("")
        self.playButton.setText("")
        self.nextButton.setText("")
        self.loopButton.setText("")
        self.currentTimeLine.setText(QCoreApplication.translate("MusicPlayer", u"00:00", None))
        self.songLength.setText(QCoreApplication.translate("MusicPlayer", u"00:00", None))
        self.addToFavoriteButton.setText("")
        self.addToPlayList.setText("")
        self.addToPlayList_2.setText("")
        self.addToPlayList_3.setText("")
        self.addToFavoriteButton_4.setText("")
        self.addToPlayList_4.setText("")
        self.currentPlayListNameLabel.setText(QCoreApplication.translate("MusicPlayer", u"Song List", None))
        self.playListIcon_2.setText("")
        self.currentPlayListSongs.setText(QCoreApplication.translate("MusicPlayer", u"name              |               path", None))
    # retranslateUi

