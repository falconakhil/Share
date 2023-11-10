# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SharingDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SharingDialog(object):
    def setupUi(self, SharingDialog):
        if not SharingDialog.objectName():
            SharingDialog.setObjectName(u"SharingDialog")
        SharingDialog.setWindowModality(Qt.ApplicationModal)
        SharingDialog.resize(400, 300)
        SharingDialog.setModal(True)
        self.stopSharing = QPushButton(SharingDialog)
        self.stopSharing.setObjectName(u"stopSharing")
        self.stopSharing.setGeometry(QRect(140, 210, 111, 51))
        self.linkLabel = QLabel(SharingDialog)
        self.linkLabel.setObjectName(u"linkLabel")
        self.linkLabel.setGeometry(QRect(50, 40, 311, 71))
        self.linkLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.sharingLabel = QLabel(SharingDialog)
        self.sharingLabel.setObjectName(u"sharingLabel")
        self.sharingLabel.setGeometry(QRect(40, 140, 331, 20))

        self.retranslateUi(SharingDialog)

        QMetaObject.connectSlotsByName(SharingDialog)
    # setupUi

    def retranslateUi(self, SharingDialog):
        SharingDialog.setWindowTitle(QCoreApplication.translate("SharingDialog", u"Dialog", None))
        self.stopSharing.setText(QCoreApplication.translate("SharingDialog", u"Stop Sharing", None))
        self.linkLabel.setText("")
        self.sharingLabel.setText("")
    # retranslateUi

