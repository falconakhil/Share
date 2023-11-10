# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MessageDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        if not MessageDialog.objectName():
            MessageDialog.setObjectName(u"MessageDialog")
        MessageDialog.setWindowModality(Qt.ApplicationModal)
        MessageDialog.resize(416, 300)
        MessageDialog.setModal(True)
        self.message = QLabel(MessageDialog)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(10, 10, 391, 201))
        self.message.setTextFormat(Qt.MarkdownText)
        self.message.setAlignment(Qt.AlignCenter)
        self.closeButton = QPushButton(MessageDialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(160, 250, 94, 28))

        self.retranslateUi(MessageDialog)

        QMetaObject.connectSlotsByName(MessageDialog)
    # setupUi

    def retranslateUi(self, MessageDialog):
        MessageDialog.setWindowTitle(QCoreApplication.translate("MessageDialog", u"Dialog", None))
        self.message.setText("")
        self.closeButton.setText(QCoreApplication.translate("MessageDialog", u"Close", None))
    # retranslateUi

