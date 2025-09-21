import os
from typing import Any

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform, QTextCharFormat, QTextCursor)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QFontComboBox,
                               QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
                               QLayout, QMainWindow, QMenu, QMenuBar,
                               QProgressBar, QPushButton, QSizePolicy, QSpinBox,
                               QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
                               QWidget, QPlainTextEdit, QDoubleSpinBox, QFileDialog)
import sys
import logging
import re
import func

logger = logging.getLogger(__name__)

class Ui_root(object):
    def __init__(self):
        self.ani_connect = None
        self.file_path = ""
        self.lyrics = []
        self.isPitched = False
        self.delay = 0
        self.time_mark = 0
        self.nowLrcIndex = 0
        self.current_index = 0
        self.audio_path = ""
        self.playback_rate = 1.0
        self.time_static = []
        self.u3d = False

    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())
        root.setSizePolicy(sizePolicy)
        root.setMinimumSize(QSize(800, 600))
        root.setMaximumSize(QSize(800, 600))
        self.actionOpen_a_LRC_File = QAction(root)
        self.actionOpen_a_LRC_File.setObjectName(u"actionOpen_a_LRC_File")
        self.actionExit = QAction(root)
        self.actionExit.setObjectName(u"actionExit")
        self.actionth_is_app = QAction(root)
        self.actionth_is_app.setObjectName(u"actionth_is_app")
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 980, 555))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.labelPath = QLabel(self.verticalLayoutWidget)
        self.labelPath.setObjectName(u"labelPath")
        self.labelPath.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.labelPath)

        self.labelTimePitch = QLabel(self.verticalLayoutWidget)
        self.labelTimePitch.setObjectName(u"labelTimePitch")
        self.labelTimePitch.setMaximumSize(QSize(400, 20))

        self.horizontalLayout.addWidget(self.labelTimePitch)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(80)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(800, 500))
        self.tabWidget.setBaseSize(QSize(800, 700))
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.OverView = QWidget()
        self.OverView.setObjectName(u"OverView")
        self.LRCBrowser = QPlainTextEdit(self.OverView)
        self.LRCBrowser.setObjectName(u"LRCBrowser")
        self.LRCBrowser.setGeometry(QRect(0, 0, 790, 430))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LRCBrowser.sizePolicy().hasHeightForWidth())
        self.LRCBrowser.setSizePolicy(sizePolicy2)
        self.LRCBrowser.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.horizontalLayoutWidget = QWidget(self.OverView)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 430, 791, 42))
        self.horizontalLayout_overView_downset = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_overView_downset.setObjectName(u"horizontalLayout_overView_downset")
        self.horizontalLayout_overView_downset.setContentsMargins(0, 0, 0, 0)
        self.pushButton_openFile = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_openFile.setObjectName(u"pushButton_openFile")
        self.pushButton_openFile.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_overView_downset.addWidget(self.pushButton_openFile)

        self.pushButton_upon = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_upon.setObjectName(u"pushButton_upon")
        self.pushButton_upon.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_overView_downset.addWidget(self.pushButton_upon)

        self.pushButton_save = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_overView_downset.addWidget(self.pushButton_save)

        self.commandLinkButton_1 = QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_1.setObjectName(u"commandLinkButton_1")

        self.horizontalLayout_overView_downset.addWidget(self.commandLinkButton_1)

        self.tabWidget.addTab(self.OverView, "")
        self.Setting = QWidget()
        self.Setting.setObjectName(u"Setting")
        self.gridLayoutWidget = QWidget(self.Setting)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 791, 271))
        self.gridLayout_setting = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_setting.setObjectName(u"gridLayout_setting")
        self.gridLayout_setting.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_delay = QVBoxLayout()
        self.verticalLayout_delay.setObjectName(u"verticalLayout_delay")
        self.labelDelay = QLabel(self.gridLayoutWidget)
        self.labelDelay.setObjectName(u"labelDelay")
        self.labelDelay.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_delay.addWidget(self.labelDelay)

        self.DelaySetting = QSpinBox(self.gridLayoutWidget)
        self.DelaySetting.setObjectName(u"DelaySetting")
        self.DelaySetting.setMinimumSize(QSize(0, 30))
        self.DelaySetting.setMinimum(-3000)
        self.DelaySetting.setMaximum(3000)
        self.DelaySetting.setValue(-300)

        self.verticalLayout_delay.addWidget(self.DelaySetting)

        self.gridLayout_setting.addLayout(self.verticalLayout_delay, 2, 1, 1, 1)

        self.checkBox_3d = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3d.setObjectName(u"checkBox_3d")
        self.checkBox_3d.setMinimumSize(QSize(0, 30))
        self.checkBox_3d.setTristate(False)

        self.gridLayout_setting.addWidget(self.checkBox_3d, 1, 0, 1, 1)

        self.checkBox_no_animation = QCheckBox(self.gridLayoutWidget)
        self.checkBox_no_animation.setObjectName(u"checkBox_SaveOri")
        self.checkBox_no_animation.setMinimumSize(QSize(0, 30))

        self.gridLayout_setting.addWidget(self.checkBox_no_animation, 1, 1, 1, 1)

        self.verticalLayout_font = QVBoxLayout()
        self.verticalLayout_font.setObjectName(u"verticalLayout_font")
        self.labelFont = QLabel(self.gridLayoutWidget)
        self.labelFont.setObjectName(u"labelFont")
        self.labelFont.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_font.addWidget(self.labelFont)

        self.fontComboBox = QFontComboBox(self.gridLayoutWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout_font.addWidget(self.fontComboBox)

        self.gridLayout_setting.addLayout(self.verticalLayout_font, 2, 0, 1, 1)

        self.verticalLayout_audio = QVBoxLayout()
        self.verticalLayout_audio.setObjectName(u"verticalLayout_audio")
        self.label_choose_audio = QLabel(self.gridLayoutWidget)
        self.label_choose_audio.setObjectName(u"label_choose_audio")

        self.verticalLayout_audio.addWidget(self.label_choose_audio)

        self.pushButton_choose_audio = QPushButton(self.gridLayoutWidget)
        self.pushButton_choose_audio.setObjectName(u"pushButton_choose_audio")
        self.pushButton_choose_audio.setMinimumSize(QSize(0, 80))

        self.verticalLayout_audio.addWidget(self.pushButton_choose_audio)

        self.gridLayout_setting.addLayout(self.verticalLayout_audio, 0, 0, 1, 1)

        self.verticalLayout_speed = QVBoxLayout()
        self.verticalLayout_speed.setObjectName(u"verticalLayout_speed")
        self.label_set_speed = QLabel(self.gridLayoutWidget)
        self.label_set_speed.setObjectName(u"label_set_speed")
        self.label_set_speed.setMaximumSize(QSize(16777215, 20))
        self.label_set_speed.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_speed.addWidget(self.label_set_speed)

        self.doubleSpinBox_speed = QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_speed.setObjectName(u"doubleSpinBox_speed")
        self.doubleSpinBox_speed.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox_speed.setMaximum(3.000000000000000)
        self.doubleSpinBox_speed.setSingleStep(0.100000000000000)
        self.doubleSpinBox_speed.setValue(1.000000000000000)

        self.verticalLayout_speed.addWidget(self.doubleSpinBox_speed)

        self.gridLayout_setting.addLayout(self.verticalLayout_speed, 0, 1, 1, 1)

        self.commandLinkButton_2 = QCommandLinkButton(self.Setting)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setGeometry(QRect(620, 430, 172, 41))
        self.tabWidget.addTab(self.Setting, "")
        self.Edit = QWidget()
        self.Edit.setObjectName(u"Edit")
        self.verticalLayoutWidget_4 = QWidget(self.Edit)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 791, 191))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_pastLyric = QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_pastLyric.setObjectName(u"textBrowser_pastLyric")
        self.textBrowser_pastLyric.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(12)
        self.textBrowser_pastLyric.setFont(font)

        self.verticalLayout_4.addWidget(self.textBrowser_pastLyric)

        self.textBrowser_nowLyric = QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_nowLyric.setObjectName(u"textBrowser_nowLyric")
        font1 = QFont()
        font1.setPointSize(44)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.textBrowser_nowLyric.setFont(font1)
        self.textBrowser_nowLyric.setAutoFillBackground(False)

        self.verticalLayout_4.addWidget(self.textBrowser_nowLyric)

        self.textBrowser_incLyric = QTextBrowser(self.verticalLayoutWidget_4)
        self.textBrowser_incLyric.setObjectName(u"textBrowser_incLyric")
        self.textBrowser_incLyric.setMaximumSize(QSize(16777215, 40))
        self.textBrowser_incLyric.setFont(font)

        self.verticalLayout_4.addWidget(self.textBrowser_incLyric)

        self.gridLayoutWidget_2 = QWidget(self.Edit)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 190, 791, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.gridLayoutWidget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_Back = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Back.setObjectName(u"pushButton_Back")
        self.pushButton_Back.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_Back)

        self.pushButton_Pause = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Pause.setObjectName(u"pushButton_Pause")
        self.pushButton_Pause.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_Pause)

        self.lcdNumber_min = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_min.setObjectName(u"lcdNumber_min")
        self.lcdNumber_min.setMinimumSize(QSize(0, 60))
        self.lcdNumber_min.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_2.addWidget(self.lcdNumber_min)

        self.lcdNumber_sec = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_sec.setObjectName(u"lcdNumber_sec")
        self.lcdNumber_sec.setMinimumSize(QSize(0, 60))
        self.lcdNumber_sec.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_2.addWidget(self.lcdNumber_sec)

        self.lcdNumber_ms = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_ms.setObjectName(u"lcdNumber_ms")
        self.lcdNumber_ms.setMinimumSize(QSize(0, 60))
        self.lcdNumber_ms.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_2.addWidget(self.lcdNumber_ms)

        self.pushButton_Rec = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Rec.setObjectName(u"pushButton_Rec")
        self.pushButton_Rec.setMinimumSize(QSize(0, 60))
        self.pushButton_Rec.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_Rec)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.pushButton_Mark = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_Mark.setObjectName(u"pushButton_Mark")
        self.pushButton_Mark.setMinimumSize(QSize(0, 80))

        self.gridLayout_2.addWidget(self.pushButton_Mark, 4, 0, 1, 1)

        self.tabWidget.addTab(self.Edit, "")

        self.verticalLayout.addWidget(self.tabWidget)

        root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName(u"statusbar")
        root.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuEdit.addAction(self.actionOpen_a_LRC_File)
        self.menuEdit.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionth_is_app)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.retranslateUi(root)
        self.blind_func(root)  # 绑定函数
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(root)


    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Word-for-word lyrics matching tool", None))
        self.actionOpen_a_LRC_File.setText(QCoreApplication.translate("root", u"Open a LRC File", None))
        self.actionExit.setText(QCoreApplication.translate("root", u"Exit", None))
        self.actionth_is_app.setText(QCoreApplication.translate("root", u"this app", None))
        self.labelPath.setText(QCoreApplication.translate("root", u"File Path:", None))
        self.labelTimePitch.setText(QCoreApplication.translate("root", u"Original Time Pitch:", None))
        self.pushButton_openFile.setText(QCoreApplication.translate("root", u"Open a lrc/txt for Lyrics", None))
        self.pushButton_upon.setText(QCoreApplication.translate("root", u"Use the Lyrics upon", None))
        self.pushButton_save.setText(QCoreApplication.translate("root", u"Save current Lyrics", None))
        self.commandLinkButton_1.setText(QCoreApplication.translate("root", u"Next Step", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OverView),
                                  QCoreApplication.translate("root", u"OverView", None))
        self.labelDelay.setText(QCoreApplication.translate("root", u"Delay(- for early; + for later; ms)", None))
        self.checkBox_3d.setText(
            QCoreApplication.translate("root", u"Using three decimal places (maybe incompatible with some app)",
                                       None))
        self.checkBox_no_animation.setText(
            QCoreApplication.translate("root", u"No More Animation(For devices with poor performance)", None))
        self.labelFont.setText(QCoreApplication.translate("root", u"Font Setting", None))
        self.label_choose_audio.setText(
            QCoreApplication.translate("root", u"Choose a related audio for match", None))
        self.pushButton_choose_audio.setText(QCoreApplication.translate("root", u"Audio File: ", None))
        self.label_set_speed.setText(
            QCoreApplication.translate("root", u"Speed(adjust this value according to your own ability)", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("root", u"Next Step", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Setting),
                                  QCoreApplication.translate("root", u"Setting", None))
        self.textBrowser_pastLyric.setHtml(QCoreApplication.translate("root",
                                                                      u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "hr { height: 1px; border-width: 0; }\n"
                                                                      "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                      "li.checked::marker { content: \"\\2612\"; }\n"
                                                                      "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>",
                                                                      None))
        self.textBrowser_nowLyric.setHtml(QCoreApplication.translate("root",
                                                                     u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "hr { height: 1px; border-width: 0; }\n"
                                                                     "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                     "li.checked::marker { content: \"\\2612\"; }\n"
                                                                     "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:44pt; font-weight:700; font-style:normal;\">\n"
                                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:48pt;\"><br /></p></body></html>",
                                                                     None))
        self.textBrowser_incLyric.setHtml(QCoreApplication.translate("root",
                                                                     u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "hr { height: 1px; border-width: 0; }\n"
                                                                     "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                     "li.checked::marker { content: \"\\2612\"; }\n"
                                                                     "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                     None))
        self.pushButton_Back.setText(QCoreApplication.translate("root", u"Back 10s", None))
        self.pushButton_Pause.setText(QCoreApplication.translate("root", u"Pause", None))
        self.pushButton_Rec.setText(QCoreApplication.translate("root", u"Reset", None))
        self.pushButton_Mark.setText(QCoreApplication.translate("root", u"Start Player", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Edit),
                                  QCoreApplication.translate("root", u"Edit", None))
        self.menuEdit.setTitle(QCoreApplication.translate("root", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("root", u"About", None))
        # retranslateUi


    def blind_func(self, root):
        def choose_file():
            file_path = func.choose_file(root, "Choose the original Lyrics", "LyricsFile (*.lrc *.txt)")
            if file_path and func.os.path.exists(file_path):
                self.file_path = file_path
                logger.info(f"File path: {file_path}")
                self.labelPath.setText(f"File Path: {file_path}")
                with open(file_path, "r", encoding="utf-8") as f:
                    self.lyrics = f.readlines()
                    logger.info(f"Loaded Lyrics: {self.lyrics[0]}")
                if "[" in self.lyrics[0] and "]" in self.lyrics[0]:
                    self.isPitched =  True
                self.labelTimePitch.setText("Original Time Pitch: " + ("True" if self.isPitched else "False"))
                temp = ""
                for x in self.lyrics:
                    temp += x
                self.LRCBrowser.setPlainText(temp)

        def update_lyrics():
            self.lyrics = self.LRCBrowser.toPlainText().split("\n")
            for i in range(len(self.lyrics)):
                self.lyrics[i] = self.lyrics[i] + "\n"
            self.labelPath.setText("File Path: None(From the temporary input texts)")
            if "[" in self.lyrics[0] and "]" in self.lyrics[0]:
                self.isPitched = True
            self.labelTimePitch.setText("Original Time Pitch: " + ("True" if self.isPitched else "False"))

        def next_step_01():
            if self.lyrics:
                self.tabWidget.setCurrentIndex(1)
            else:
                func.messaagebox(root, "Error", "Please choose a LRC file or set your own Lyrics.")

        def choose_audio():
            file_path = func.choose_file(root, "Choose the audio file", "AudioFile (*.mp3 *.wav *.flac)")
            if file_path and func.os.path.exists(file_path):
                self.audio_path = file_path
                self.player.setSource(QUrl.fromLocalFile(file_path))
                self.pushButton_choose_audio.setText(f"Audio File: {file_path}")
                logger.info(f"Audio path: {file_path}")

        def update_playback_rate():
            self.player.setPlaybackRate(self.doubleSpinBox_speed.value())
            logger.info(f"Playback rate: {self.doubleSpinBox_speed.value()}")

        def update_delay():
            self.delay = self.DelaySetting.value()

        def prepare_edit():
            logger.info("Entering Edit Page..")
            self.nowLrcIndex = 0
            self.current_index = 0
            self.time_static = []
            self.pushButton_Mark.setText("Start Play")
            self.textBrowser_pastLyric.setText(" ")
            self.textBrowser_nowLyric.setText(self.lyrics[0])
            self.textBrowser_incLyric.setText(self.lyrics[1])
            self.tabWidget.setCurrentIndex(2)
            self.player.pause()
            self.player.setPosition(0)
            self.pushButton_Pause.setText("Pause")
            cursor = self.textBrowser_nowLyric.textCursor()
            cursor.select(QTextCursor.SelectionType.Document)
            format = QTextCharFormat()
            palette = self.textBrowser_nowLyric.palette()
            format.setForeground(palette.color(QPalette.ColorRole.WindowText))
            format.setBackground(palette.color(QPalette.ColorRole.Window))
            format.setFont(QFont(self.fontComboBox.currentFont().families(), 40, QFont.Weight.Bold))
            cursor.setCharFormat(format)
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            cursor.clearSelection()
            self.textBrowser_nowLyric.setTextCursor(cursor)


        def highlight_next_char():
            """高亮下一个字符"""
            if not self.player.isPlaying():
                self.player.play()
                self.pushButton_Mark.setText("Next Char (N)")
                return
            def highlight_char(index):
                """高亮指定索引的字符"""
                if index < 0 or index >= len(self.lyrics[self.nowLrcIndex]):
                    return
                # 获取光标
                cursor = self.textBrowser_nowLyric.textCursor()
                if index == 0:
                    cursor = self.textBrowser_nowLyric.textCursor()
                    # 选择所有文本
                    cursor.select(QTextCursor.SelectionType.Document)
                    format = QTextCharFormat()
                    # 使用系统调色盘的默认文本和背景颜色
                    palette = self.textBrowser_nowLyric.palette()
                    # 设置前景色（文本颜色）为系统默认的窗口文本颜色
                    format.setForeground(palette.color(QPalette.ColorRole.WindowText))
                    # 设置背景色为系统默认的窗口背景颜色（透明效果）
                    format.setBackground(palette.color(QPalette.ColorRole.Window))
                    format.setFont(QFont(self.fontComboBox.currentFont().families(), 40, QFont.Weight.Bold))
                    # 应用默认格式
                    cursor.setCharFormat(format)
                    # 清除选择
                    cursor.clearSelection()
                    self.textBrowser_nowLyric.setTextCursor(cursor)
                # 首先重置所有文本的格式为默认（可选，这里我们选择逐个处理）
                # 创建用于恢复之前字符的格式
                if index > 0:
                    # 重置前一个字符的格式：去除背景色，前景色变绿
                    prev_format = QTextCharFormat()
                    prev_format.setBackground(QColor("white"))  # 去除背景色
                    prev_format.setForeground(QColor("green"))  # 前景色变绿
                    prev_format.setFont(QFont(self.fontComboBox.currentFont().families(), 40, QFont.Weight.Bold))
                    cursor.setPosition(index - 1, QTextCursor.MoveMode.MoveAnchor)
                    cursor.setPosition(index, QTextCursor.MoveMode.KeepAnchor)
                    cursor.setCharFormat(prev_format)

                # 设置当前字符的格式：背景色变黄，前景色变红
                current_format = QTextCharFormat()
                current_format.setBackground(QColor("yellow"))
                current_format.setForeground(QColor("red"))
                current_format.setFont(QFont(self.fontComboBox.currentFont().families(), 40, QFont.Weight.Bold))
                cursor.setPosition(index, QTextCursor.MoveMode.MoveAnchor)
                cursor.setPosition(index + 1, QTextCursor.MoveMode.KeepAnchor)
                cursor.setCharFormat(current_format)

                # 移动光标以便看到效果（可选）
                cursor.clearSelection()
                cursor.setPosition(index + 1)
                self.textBrowser_nowLyric.setTextCursor(cursor)


            self.current_index += 1
            logger.debug(f"Current index: {self.current_index}")
            logger.debug(f"Current position: {self.player.position()}")
            self.time_static.append(self.player.position())
            if self.current_index >= len(self.lyrics[self.nowLrcIndex]):
                self.nowLrcIndex += 1
                self.textBrowser_pastLyric.setText(self.lyrics[self.nowLrcIndex - 1])
                if self.nowLrcIndex == len(self.lyrics):
                    func.messaagebox(root, "Finished", "All done. Click OK to start lrc generate.")
                    outcome = func.generate_lrc(self.time_static, self.lyrics, self.delay)
                    self.LRCBrowser.setPlainText(outcome)
                    self.tabWidget.setCurrentIndex(0)
                    return
                self.textBrowser_nowLyric.setText(self.lyrics[self.nowLrcIndex])
                if self.nowLrcIndex >= len(self.lyrics) - 1:
                    self.textBrowser_incLyric.setText("")
                else:
                    self.textBrowser_incLyric.setText(self.lyrics[self.nowLrcIndex + 1])
                self.current_index = 0  # 循环到开头

            highlight_char(self.current_index)

        def update_position():
            now = self.player.position()
            pgs = int(self.player.position() / self.player.duration() * 100)
            min = now // 60000
            now = now % 60000
            sec = now // 1000
            ms = now % 1000
            self.progressBar.setValue(pgs)
            self.lcdNumber_min.display(min)
            self.lcdNumber_sec.display(sec)
            self.lcdNumber_ms.display(ms)

        def save_file():
            save_path, _ = QFileDialog.getSaveFileName(root, "Save File", os.getcwd(), "LRC File (*.lrc);;Any File (*.*)")
            if save_path:
                temp = self.LRCBrowser.toPlainText()
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(temp)
                func.messaagebox(root, "Success", "File saved successfully.")

        def update_3d():
            logger.info("Selected Using 3 decimal places")
            self.u3d = self.checkBox_3d.isChecked()

        def update_animation():
            if self.checkBox_no_animation.isChecked():
                self.player.positionChanged.disconnect(self.ani_connect)
                self.ani_connect = None
            else:
                self.ani_connect=self.player.positionChanged.connect(update_position)

        def update_font():
            def change_font(browser: QTextBrowser|QPlainTextEdit, selected_font: QFont):
                cursor = browser.textCursor()
                document = browser.document()
                cursor.movePosition(QTextCursor.MoveOperation.Start)
                while not cursor.atEnd():
                    cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock)
                    cursor.movePosition(QTextCursor.MoveOperation.EndOfBlock, QTextCursor.MoveMode.KeepAnchor)
                    # 获取当前文本块的字符格式
                    char_format = cursor.charFormat()
                    # 创建新的字符格式，保留原有属性只更改字体
                    new_format = QTextCharFormat(char_format)
                    new_format.setFontFamily(selected_font.family())
                    # 应用新格式
                    cursor.mergeCharFormat(new_format)
                    # 移动到下一个文本块
                    cursor.movePosition(QTextCursor.MoveOperation.NextBlock)
                # 恢复光标位置
                cursor.setPosition(0)
                browser.setTextCursor(cursor)
            change_font(self.LRCBrowser, self.fontComboBox.currentFont())
            change_font(self.textBrowser_nowLyric, self.fontComboBox.currentFont())
            change_font(self.textBrowser_pastLyric, self.fontComboBox.currentFont())
            change_font(self.textBrowser_incLyric, self.fontComboBox.currentFont())

        def back_10s():
            logger.info(f"User Back 10s from {str(self.player.position())} to {self.player.position() - 10000}")
            self.player.setPosition(self.player.position() - 10000)

        def pause():
            if self.player.isPlaying():
                self.player.pause()
                self.pushButton_Pause.setText("Play")
            else:
                self.player.play()
                self.pushButton_Pause.setText("Pause")

        def rec():
            logger.info("Reset every change")
            prepare_edit()

        self.actionOpen_a_LRC_File.setShortcut(u"Ctrl+O")
        self.actionExit.triggered.connect(root.close)
        self.pushButton_openFile.clicked.connect(choose_file)
        self.pushButton_save.clicked.connect(save_file)
        self.actionOpen_a_LRC_File.triggered.connect(choose_file)
        self.commandLinkButton_1.clicked.connect(next_step_01)
        self.pushButton_upon.clicked.connect(update_lyrics)
        self.pushButton_choose_audio.clicked.connect(choose_audio)
        self.checkBox_3d.stateChanged.connect(update_3d)
        self.checkBox_no_animation.stateChanged.connect(update_animation)
        self.fontComboBox.currentFontChanged.connect(update_font)
        self.doubleSpinBox_speed.valueChanged.connect(update_playback_rate)
        self.DelaySetting.valueChanged.connect(update_delay)
        self.commandLinkButton_2.clicked.connect(prepare_edit)
        self.pushButton_Mark.clicked.connect(highlight_next_char)
        self.pushButton_Pause.clicked.connect(pause)
        self.pushButton_Back.clicked.connect(back_10s)
        self.pushButton_Rec.clicked.connect(rec)
        self.ani_connect=self.player.positionChanged.connect(update_position)
        self.pushButton_Mark.setShortcut(u"n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_root()
    root = QMainWindow()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec())