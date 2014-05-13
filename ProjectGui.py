# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectWindow.ui'
#
# Created: Sat May  3 22:10:29 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_projectWindow(object):
    def setupUi(self, projectWindow):
        projectWindow.setObjectName("projectWindow")
        projectWindow.resize(783, 395)
        self.centralwidget = QtGui.QWidget(projectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 771, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        projectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(projectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        projectWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(projectWindow)
        self.statusbar.setObjectName("statusbar")
        projectWindow.setStatusBar(self.statusbar)
        self.actionNew_Project = QtGui.QAction(projectWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionEdit_Project = QtGui.QAction(projectWindow)
        self.actionEdit_Project.setObjectName("actionEdit_Project")
        self.actionExit = QtGui.QAction(projectWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(projectWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionEdit_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(projectWindow)
        QtCore.QMetaObject.connectSlotsByName(projectWindow)

    def retranslateUi(self, projectWindow):
        projectWindow.setWindowTitle(QtGui.QApplication.translate("projectWindow", "ReadySet Volunteer - Project Management", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("projectWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("projectWindow", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("projectWindow", "Supervisor", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("projectWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("projectWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("projectWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Project.setText(QtGui.QApplication.translate("projectWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Project.setText(QtGui.QApplication.translate("projectWindow", "Edit Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("projectWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("projectWindow", "About", None, QtGui.QApplication.UnicodeUTF8))


