# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstWindow.ui'
#
# Created: Fri May  9 18:56:28 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_firstWindow(object):
    def setupUi(self, firstWindow):
        firstWindow.setObjectName("firstWindow")
        firstWindow.resize(548, 375)
        firstWindow.setStyleSheet("QWidget #centralwidget, #statusbar, #menubar{\n"
"    background-color: qlineargradient(spread:pad, x1:0.515633, y1:0.192, x2:0.502367, y2:0.708, stop:0.222707 rgba(21, 21, 21, 255), stop:0.799127 rgba(0, 0, 0, 251));\n"
"}\n"
"\n"
"QFrame #logoQFrame{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    image: url(:/icons/rosewood-logo-red.png);\n"
"}\n"
"")
        firstWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(firstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 30, 531, 151))
        self.frame.setStyleSheet("QFrame #frame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.458934, y1:0.857, x2:0.459035, y2:0.266, stop:0.161572 rgba(214, 0, 0, 255), stop:0.427948 rgba(196, 0, 0, 255), stop:0.68559 rgba(166, 0, 0, 255), stop:0.965066 rgba(147, 0, 0, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton{\n"
"   background-color: transparent;\n"
"   border: none;\n"
"}")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginLogoutqToolButton = QtGui.QToolButton(self.frame)
        self.loginLogoutqToolButton.setGeometry(QtCore.QRect(60, 10, 131, 131))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/volunteer64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginLogoutqToolButton.setIcon(icon)
        self.loginLogoutqToolButton.setIconSize(QtCore.QSize(64, 64))
        self.loginLogoutqToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.loginLogoutqToolButton.setObjectName("loginLogoutqToolButton")
        self.projectMngmntQToolButton = QtGui.QToolButton(self.frame)
        self.projectMngmntQToolButton.setGeometry(QtCore.QRect(330, 10, 131, 131))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/edit64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.projectMngmntQToolButton.setIcon(icon1)
        self.projectMngmntQToolButton.setIconSize(QtCore.QSize(64, 64))
        self.projectMngmntQToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.projectMngmntQToolButton.setObjectName("projectMngmntQToolButton")
        self.logoQFrame = QtGui.QFrame(self.centralwidget)
        self.logoQFrame.setGeometry(QtCore.QRect(40, 230, 301, 81))
        self.logoQFrame.setAutoFillBackground(False)
        self.logoQFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.logoQFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.logoQFrame.setObjectName("logoQFrame")
        firstWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(firstWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        firstWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(firstWindow)
        self.statusbar.setObjectName("statusbar")
        firstWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(firstWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/right24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(firstWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/info24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(firstWindow)
        QtCore.QMetaObject.connectSlotsByName(firstWindow)

    def retranslateUi(self, firstWindow):
        firstWindow.setWindowTitle(QtGui.QApplication.translate("firstWindow", "ReadySet Volunteer - Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.loginLogoutqToolButton.setText(QtGui.QApplication.translate("firstWindow", "Login\n"
"Logout", None, QtGui.QApplication.UnicodeUTF8))
        self.projectMngmntQToolButton.setText(QtGui.QApplication.translate("firstWindow", "Project\n"
"Management\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("firstWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("firstWindow", "Help ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("firstWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("firstWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
