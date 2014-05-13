# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VolunteerLoginWindow.ui'
#
# Created: Sun May  4 00:55:41 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_volunteerDialog(object):
    def setupUi(self, volunteerDialog):
        volunteerDialog.setObjectName("volunteerDialog")
        volunteerDialog.resize(620, 453)
        self.listWidget = QtGui.QListWidget(volunteerDialog)
        self.listWidget.setGeometry(QtCore.QRect(40, 100, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.cancelButton = QtGui.QPushButton(volunteerDialog)
        self.cancelButton.setGeometry(QtCore.QRect(460, 400, 112, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.listView = QtGui.QListView(volunteerDialog)
        self.listView.setGeometry(QtCore.QRect(330, 100, 256, 192))
        self.listView.setWordWrap(True)
        self.listView.setObjectName("listView")

        self.retranslateUi(volunteerDialog)
        QtCore.QMetaObject.connectSlotsByName(volunteerDialog)

    def retranslateUi(self, volunteerDialog):
        volunteerDialog.setWindowTitle(QtGui.QApplication.translate("volunteerDialog", "ReadySet Volunteer - Volunteer Login", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("volunteerDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

