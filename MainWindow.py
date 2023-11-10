# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileButton = QPushButton(self.centralwidget)
        self.fileButton.setObjectName(u"fileButton")

        self.verticalLayout.addWidget(self.fileButton)

        self.folderButton = QPushButton(self.centralwidget)
        self.folderButton.setObjectName(u"folderButton")

        self.verticalLayout.addWidget(self.folderButton)

        self.selectedFiles = QListView(self.centralwidget)
        self.selectedFiles.setObjectName(u"selectedFiles")
        self.selectedFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selectedFiles.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.selectedFiles)

        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")

        self.verticalLayout.addWidget(self.clearButton)

        self.ngrokCheck = QCheckBox(self.centralwidget)
        self.ngrokCheck.setObjectName(u"ngrokCheck")

        self.verticalLayout.addWidget(self.ngrokCheck)

        self.shareButton = QPushButton(self.centralwidget)
        self.shareButton.setObjectName(u"shareButton")

        self.verticalLayout.addWidget(self.shareButton)

        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.status)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 696, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fileButton.setText(QCoreApplication.translate("MainWindow", u"Select Files", None))
        self.folderButton.setText(QCoreApplication.translate("MainWindow", u"Select Folders", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.ngrokCheck.setText(QCoreApplication.translate("MainWindow", u"Use Ngrok (Tick it if u want to send stuff outside your LAN)", None))
        self.shareButton.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.status.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
