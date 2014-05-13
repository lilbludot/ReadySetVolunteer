# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created: Sat May  3 23:12:22 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(600, 343)
        self.volunteerButton = QtGui.QPushButton(loginDialog)
        self.volunteerButton.setGeometry(QtCore.QRect(40, 130, 131, 101))
        self.volunteerButton.setObjectName("volunteerButton")
        self.newVolunteerButton = QtGui.QPushButton(loginDialog)
        self.newVolunteerButton.setGeometry(QtCore.QRect(230, 130, 131, 101))
        self.newVolunteerButton.setObjectName("newVolunteerButton")
        self.guestButton = QtGui.QPushButton(loginDialog)
        self.guestButton.setGeometry(QtCore.QRect(420, 130, 131, 101))
        self.guestButton.setObjectName("guestButton")
        self.cancelButton = QtGui.QPushButton(loginDialog)
        self.cancelButton.setGeometry(QtCore.QRect(430, 300, 112, 28))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QtGui.QApplication.translate("loginDialog", "ReadySet Volunteer - Login ", None, QtGui.QApplication.UnicodeUTF8))
        self.volunteerButton.setText(QtGui.QApplication.translate("loginDialog", "Volunteer", None, QtGui.QApplication.UnicodeUTF8))
        self.newVolunteerButton.setText(QtGui.QApplication.translate("loginDialog", "First Time\n"
"Volunteer\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.guestButton.setText(QtGui.QApplication.translate("loginDialog", "Guest", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("loginDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

