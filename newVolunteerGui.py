# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstTimeVolunteerWindow.ui'
#
# Created: Fri May  9 18:55:28 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NewVolunteerDialog(object):
    def setupUi(self, NewVolunteerDialog):
        NewVolunteerDialog.setObjectName("NewVolunteerDialog")
        NewVolunteerDialog.resize(1146, 890)
        self.firstNameLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.firstNameLineEdit.setGeometry(QtCore.QRect(60, 140, 251, 31))
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.lastNameLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.lastNameLineEdit.setGeometry(QtCore.QRect(60, 200, 251, 31))
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.streetLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.streetLineEdit.setGeometry(QtCore.QRect(380, 140, 251, 31))
        self.streetLineEdit.setText("")
        self.streetLineEdit.setObjectName("streetLineEdit")
        self.cityLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.cityLineEdit.setGeometry(QtCore.QRect(380, 200, 251, 31))
        self.cityLineEdit.setText("")
        self.cityLineEdit.setObjectName("cityLineEdit")
        self.homePhoneLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.homePhoneLineEdit.setGeometry(QtCore.QRect(380, 290, 251, 31))
        self.homePhoneLineEdit.setText("")
        self.homePhoneLineEdit.setObjectName("homePhoneLineEdit")
        self.emergFirstLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.emergFirstLineEdit.setGeometry(QtCore.QRect(50, 510, 251, 31))
        self.emergFirstLineEdit.setObjectName("emergFirstLineEdit")
        self.emergPhoneLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.emergPhoneLineEdit.setGeometry(QtCore.QRect(50, 600, 251, 31))
        self.emergPhoneLineEdit.setObjectName("emergPhoneLineEdit")
        self.buttonBox = QtGui.QDialogButtonBox(NewVolunteerDialog)
        self.buttonBox.setGeometry(QtCore.QRect(920, 820, 176, 28))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.stateLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.stateLineEdit.setGeometry(QtCore.QRect(380, 230, 251, 31))
        self.stateLineEdit.setText("")
        self.stateLineEdit.setObjectName("stateLineEdit")
        self.zipCodeLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.zipCodeLineEdit.setGeometry(QtCore.QRect(380, 260, 251, 31))
        self.zipCodeLineEdit.setText("")
        self.zipCodeLineEdit.setObjectName("zipCodeLineEdit")
        self.miLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.miLineEdit.setGeometry(QtCore.QRect(60, 170, 251, 31))
        self.miLineEdit.setObjectName("miLineEdit")
        self.aptUnitLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.aptUnitLineEdit.setGeometry(QtCore.QRect(380, 170, 251, 31))
        self.aptUnitLineEdit.setObjectName("aptUnitLineEdit")
        self.altPhoneLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.altPhoneLineEdit.setGeometry(QtCore.QRect(380, 320, 251, 31))
        self.altPhoneLineEdit.setText("")
        self.altPhoneLineEdit.setObjectName("altPhoneLineEdit")
        self.birthdateLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.birthdateLineEdit.setGeometry(QtCore.QRect(60, 230, 251, 31))
        self.birthdateLineEdit.setAutoFillBackground(False)
        self.birthdateLineEdit.setText("")
        self.birthdateLineEdit.setObjectName("birthdateLineEdit")
        self.emailLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.emailLineEdit.setGeometry(QtCore.QRect(380, 350, 251, 31))
        self.emailLineEdit.setText("")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.olderThan18Checkbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.olderThan18Checkbox.setGeometry(QtCore.QRect(60, 280, 191, 25))
        self.olderThan18Checkbox.setAutoExclusive(True)
        self.olderThan18Checkbox.setObjectName("olderThan18Checkbox")
        self.youngerThan18Checkbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.youngerThan18Checkbox.setGeometry(QtCore.QRect(60, 310, 211, 25))
        self.youngerThan18Checkbox.setAutoExclusive(True)
        self.youngerThan18Checkbox.setObjectName("youngerThan18Checkbox")
        self.parentGuardianLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.parentGuardianLineEdit.setGeometry(QtCore.QRect(60, 350, 251, 31))
        self.parentGuardianLineEdit.setText("")
        self.parentGuardianLineEdit.setObjectName("parentGuardianLineEdit")
        self.employmentLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.employmentLineEdit.setGeometry(QtCore.QRect(380, 510, 251, 31))
        self.employmentLineEdit.setText("")
        self.employmentLineEdit.setObjectName("employmentLineEdit")
        self.empStreetLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.empStreetLineEdit.setGeometry(QtCore.QRect(380, 540, 251, 31))
        self.empStreetLineEdit.setText("")
        self.empStreetLineEdit.setObjectName("empStreetLineEdit")
        self.empCityLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.empCityLineEdit.setGeometry(QtCore.QRect(380, 570, 251, 31))
        self.empCityLineEdit.setText("")
        self.empCityLineEdit.setObjectName("empCityLineEdit")
        self.empStateLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.empStateLineEdit.setGeometry(QtCore.QRect(380, 600, 251, 31))
        self.empStateLineEdit.setText("")
        self.empStateLineEdit.setObjectName("empStateLineEdit")
        self.empZipCodeLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.empZipCodeLineEdit.setGeometry(QtCore.QRect(380, 630, 251, 31))
        self.empZipCodeLineEdit.setText("")
        self.empZipCodeLineEdit.setObjectName("empZipCodeLineEdit")
        self.EmergencyLabel = QtGui.QLabel(NewVolunteerDialog)
        self.EmergencyLabel.setGeometry(QtCore.QRect(50, 460, 181, 21))
        self.EmergencyLabel.setObjectName("EmergencyLabel")
        self.emergLastLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.emergLastLineEdit.setGeometry(QtCore.QRect(50, 540, 251, 31))
        self.emergLastLineEdit.setObjectName("emergLastLineEdit")
        self.emergRelationshipLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.emergRelationshipLineEdit.setGeometry(QtCore.QRect(50, 570, 251, 31))
        self.emergRelationshipLineEdit.setObjectName("emergRelationshipLineEdit")
        self.formTitleLabel = QtGui.QLabel(NewVolunteerDialog)
        self.formTitleLabel.setGeometry(QtCore.QRect(230, 30, 581, 31))
        self.formTitleLabel.setObjectName("formTitleLabel")
        self.iContributeLabel = QtGui.QLabel(NewVolunteerDialog)
        self.iContributeLabel.setGeometry(QtCore.QRect(740, 130, 341, 51))
        self.iContributeLabel.setObjectName("iContributeLabel")
        self.anywhereCheckbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.anywhereCheckbox.setGeometry(QtCore.QRect(740, 200, 231, 25))
        self.anywhereCheckbox.setObjectName("anywhereCheckbox")
        self.cafeCheckbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.cafeCheckbox.setGeometry(QtCore.QRect(740, 230, 231, 25))
        self.cafeCheckbox.setObjectName("cafeCheckbox")
        self.administrationCheckbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.administrationCheckbox.setGeometry(QtCore.QRect(740, 260, 231, 25))
        self.administrationCheckbox.setObjectName("administrationCheckbox")
        self.communityCheckbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.communityCheckbox.setGeometry(QtCore.QRect(740, 290, 231, 25))
        self.communityCheckbox.setObjectName("communityCheckbox")
        self.YouthCheckbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.YouthCheckbox.setGeometry(QtCore.QRect(740, 320, 231, 25))
        self.YouthCheckbox.setObjectName("YouthCheckbox")
        self.otherCheckbox = QtGui.QCheckBox(NewVolunteerDialog)
        self.otherCheckbox.setGeometry(QtCore.QRect(740, 350, 91, 25))
        self.otherCheckbox.setObjectName("otherCheckbox")
        self.areasOfInteresLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.areasOfInteresLineEdit.setGeometry(QtCore.QRect(790, 380, 251, 31))
        self.areasOfInteresLineEdit.setObjectName("areasOfInteresLineEdit")
        self.mondayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.mondayFromLineEdit.setGeometry(QtCore.QRect(830, 510, 101, 31))
        self.mondayFromLineEdit.setText("")
        self.mondayFromLineEdit.setObjectName("mondayFromLineEdit")
        self.mondayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.mondayToLineEdit.setGeometry(QtCore.QRect(930, 510, 101, 31))
        self.mondayToLineEdit.setText("")
        self.mondayToLineEdit.setObjectName("mondayToLineEdit")
        self.MondayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.MondayLabel.setGeometry(QtCore.QRect(730, 520, 71, 20))
        self.MondayLabel.setObjectName("MondayLabel")
        self.tuesdayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.tuesdayLabel.setGeometry(QtCore.QRect(730, 550, 71, 20))
        self.tuesdayLabel.setObjectName("tuesdayLabel")
        self.wednesdayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.wednesdayLabel.setGeometry(QtCore.QRect(730, 580, 101, 20))
        self.wednesdayLabel.setObjectName("wednesdayLabel")
        self.thursdayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.thursdayLabel.setGeometry(QtCore.QRect(730, 610, 79, 20))
        self.thursdayLabel.setObjectName("thursdayLabel")
        self.fridayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.fridayLabel.setGeometry(QtCore.QRect(730, 640, 79, 20))
        self.fridayLabel.setObjectName("fridayLabel")
        self.saturdayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.saturdayLabel.setGeometry(QtCore.QRect(730, 670, 79, 20))
        self.saturdayLabel.setObjectName("saturdayLabel")
        self.sundayLabel = QtGui.QLabel(NewVolunteerDialog)
        self.sundayLabel.setGeometry(QtCore.QRect(730, 700, 79, 20))
        self.sundayLabel.setObjectName("sundayLabel")
        self.TuesdayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.TuesdayFromLineEdit.setGeometry(QtCore.QRect(830, 540, 101, 31))
        self.TuesdayFromLineEdit.setText("")
        self.TuesdayFromLineEdit.setObjectName("TuesdayFromLineEdit")
        self.wednesdayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.wednesdayFromLineEdit.setGeometry(QtCore.QRect(830, 570, 101, 31))
        self.wednesdayFromLineEdit.setText("")
        self.wednesdayFromLineEdit.setObjectName("wednesdayFromLineEdit")
        self.thursdayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.thursdayFromLineEdit.setGeometry(QtCore.QRect(830, 600, 101, 31))
        self.thursdayFromLineEdit.setText("")
        self.thursdayFromLineEdit.setObjectName("thursdayFromLineEdit")
        self.fridayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.fridayFromLineEdit.setGeometry(QtCore.QRect(830, 630, 101, 31))
        self.fridayFromLineEdit.setText("")
        self.fridayFromLineEdit.setObjectName("fridayFromLineEdit")
        self.saturdayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.saturdayFromLineEdit.setGeometry(QtCore.QRect(830, 660, 101, 31))
        self.saturdayFromLineEdit.setText("")
        self.saturdayFromLineEdit.setObjectName("saturdayFromLineEdit")
        self.sundayFromLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.sundayFromLineEdit.setGeometry(QtCore.QRect(830, 690, 101, 31))
        self.sundayFromLineEdit.setText("")
        self.sundayFromLineEdit.setObjectName("sundayFromLineEdit")
        self.wednesdayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.wednesdayToLineEdit.setGeometry(QtCore.QRect(930, 570, 101, 31))
        self.wednesdayToLineEdit.setText("")
        self.wednesdayToLineEdit.setObjectName("wednesdayToLineEdit")
        self.tuesdayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.tuesdayToLineEdit.setGeometry(QtCore.QRect(930, 540, 101, 31))
        self.tuesdayToLineEdit.setText("")
        self.tuesdayToLineEdit.setObjectName("tuesdayToLineEdit")
        self.thursdayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.thursdayToLineEdit.setGeometry(QtCore.QRect(930, 600, 101, 31))
        self.thursdayToLineEdit.setText("")
        self.thursdayToLineEdit.setObjectName("thursdayToLineEdit")
        self.fridayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.fridayToLineEdit.setGeometry(QtCore.QRect(930, 630, 101, 31))
        self.fridayToLineEdit.setText("")
        self.fridayToLineEdit.setObjectName("fridayToLineEdit")
        self.saturdayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.saturdayToLineEdit.setGeometry(QtCore.QRect(930, 660, 101, 31))
        self.saturdayToLineEdit.setText("")
        self.saturdayToLineEdit.setObjectName("saturdayToLineEdit")
        self.sundayToLineEdit = QtGui.QLineEdit(NewVolunteerDialog)
        self.sundayToLineEdit.setGeometry(QtCore.QRect(930, 690, 101, 31))
        self.sundayToLineEdit.setText("")
        self.sundayToLineEdit.setObjectName("sundayToLineEdit")
        self.availabilityLabel = QtGui.QLabel(NewVolunteerDialog)
        self.availabilityLabel.setGeometry(QtCore.QRect(730, 460, 131, 20))
        self.availabilityLabel.setObjectName("availabilityLabel")
        self.label_10 = QtGui.QLabel(NewVolunteerDialog)
        self.label_10.setGeometry(QtCore.QRect(380, 460, 131, 20))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(NewVolunteerDialog)
        QtCore.QObject.connect(self.youngerThan18Checkbox, QtCore.SIGNAL("clicked()"), self.parentGuardianLineEdit.setFocus)
        QtCore.QObject.connect(self.otherCheckbox, QtCore.SIGNAL("clicked()"), self.areasOfInteresLineEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(NewVolunteerDialog)
        NewVolunteerDialog.setTabOrder(self.firstNameLineEdit, self.miLineEdit)
        NewVolunteerDialog.setTabOrder(self.miLineEdit, self.lastNameLineEdit)
        NewVolunteerDialog.setTabOrder(self.lastNameLineEdit, self.birthdateLineEdit)
        NewVolunteerDialog.setTabOrder(self.birthdateLineEdit, self.olderThan18Checkbox)
        NewVolunteerDialog.setTabOrder(self.olderThan18Checkbox, self.youngerThan18Checkbox)
        NewVolunteerDialog.setTabOrder(self.youngerThan18Checkbox, self.parentGuardianLineEdit)
        NewVolunteerDialog.setTabOrder(self.parentGuardianLineEdit, self.streetLineEdit)
        NewVolunteerDialog.setTabOrder(self.streetLineEdit, self.aptUnitLineEdit)
        NewVolunteerDialog.setTabOrder(self.aptUnitLineEdit, self.cityLineEdit)
        NewVolunteerDialog.setTabOrder(self.cityLineEdit, self.stateLineEdit)
        NewVolunteerDialog.setTabOrder(self.stateLineEdit, self.zipCodeLineEdit)
        NewVolunteerDialog.setTabOrder(self.zipCodeLineEdit, self.homePhoneLineEdit)
        NewVolunteerDialog.setTabOrder(self.homePhoneLineEdit, self.altPhoneLineEdit)
        NewVolunteerDialog.setTabOrder(self.altPhoneLineEdit, self.emailLineEdit)
        NewVolunteerDialog.setTabOrder(self.emailLineEdit, self.emergFirstLineEdit)
        NewVolunteerDialog.setTabOrder(self.emergFirstLineEdit, self.emergLastLineEdit)
        NewVolunteerDialog.setTabOrder(self.emergLastLineEdit, self.emergRelationshipLineEdit)
        NewVolunteerDialog.setTabOrder(self.emergRelationshipLineEdit, self.emergPhoneLineEdit)
        NewVolunteerDialog.setTabOrder(self.emergPhoneLineEdit, self.employmentLineEdit)
        NewVolunteerDialog.setTabOrder(self.employmentLineEdit, self.empStreetLineEdit)
        NewVolunteerDialog.setTabOrder(self.empStreetLineEdit, self.empCityLineEdit)
        NewVolunteerDialog.setTabOrder(self.empCityLineEdit, self.empStateLineEdit)
        NewVolunteerDialog.setTabOrder(self.empStateLineEdit, self.empZipCodeLineEdit)
        NewVolunteerDialog.setTabOrder(self.empZipCodeLineEdit, self.anywhereCheckbox)
        NewVolunteerDialog.setTabOrder(self.anywhereCheckbox, self.cafeCheckbox)
        NewVolunteerDialog.setTabOrder(self.cafeCheckbox, self.administrationCheckbox)
        NewVolunteerDialog.setTabOrder(self.administrationCheckbox, self.communityCheckbox)
        NewVolunteerDialog.setTabOrder(self.communityCheckbox, self.YouthCheckbox)
        NewVolunteerDialog.setTabOrder(self.YouthCheckbox, self.otherCheckbox)
        NewVolunteerDialog.setTabOrder(self.otherCheckbox, self.areasOfInteresLineEdit)
        NewVolunteerDialog.setTabOrder(self.areasOfInteresLineEdit, self.mondayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.mondayFromLineEdit, self.mondayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.mondayToLineEdit, self.TuesdayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.TuesdayFromLineEdit, self.tuesdayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.tuesdayToLineEdit, self.wednesdayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.wednesdayFromLineEdit, self.wednesdayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.wednesdayToLineEdit, self.thursdayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.thursdayFromLineEdit, self.thursdayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.thursdayToLineEdit, self.fridayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.fridayFromLineEdit, self.fridayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.fridayToLineEdit, self.saturdayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.saturdayFromLineEdit, self.saturdayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.saturdayToLineEdit, self.sundayFromLineEdit)
        NewVolunteerDialog.setTabOrder(self.sundayFromLineEdit, self.sundayToLineEdit)
        NewVolunteerDialog.setTabOrder(self.sundayToLineEdit, self.buttonBox)

    def retranslateUi(self, NewVolunteerDialog):
        NewVolunteerDialog.setWindowTitle(QtGui.QApplication.translate("NewVolunteerDialog", "ReadySet Volunteer - First Time Volunteer Login", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.streetLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Street Address", None, QtGui.QApplication.UnicodeUTF8))
        self.cityLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "City ", None, QtGui.QApplication.UnicodeUTF8))
        self.homePhoneLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Home Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.emergFirstLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.emergPhoneLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Emergency Contact Phone ", None, QtGui.QApplication.UnicodeUTF8))
        self.stateLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "State  ", None, QtGui.QApplication.UnicodeUTF8))
        self.zipCodeLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", " Zip Code", None, QtGui.QApplication.UnicodeUTF8))
        self.miLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "MI", None, QtGui.QApplication.UnicodeUTF8))
        self.aptUnitLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Apartment/Unit #", None, QtGui.QApplication.UnicodeUTF8))
        self.altPhoneLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Alternate Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.birthdateLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Birthdate mm/dd/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "E-mail address", None, QtGui.QApplication.UnicodeUTF8))
        self.olderThan18Checkbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "I am 18 or older", None, QtGui.QApplication.UnicodeUTF8))
        self.youngerThan18Checkbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "I am younger  than 18", None, QtGui.QApplication.UnicodeUTF8))
        self.parentGuardianLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Parent/ Legal Guardian ", None, QtGui.QApplication.UnicodeUTF8))
        self.employmentLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Place of Employment", None, QtGui.QApplication.UnicodeUTF8))
        self.empStreetLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Street Address", None, QtGui.QApplication.UnicodeUTF8))
        self.empCityLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "City ", None, QtGui.QApplication.UnicodeUTF8))
        self.empStateLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "State  ", None, QtGui.QApplication.UnicodeUTF8))
        self.empZipCodeLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", " Zip Code", None, QtGui.QApplication.UnicodeUTF8))
        self.EmergencyLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Emergency Contact:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.emergLastLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Last Name ", None, QtGui.QApplication.UnicodeUTF8))
        self.emergRelationshipLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Relationship", None, QtGui.QApplication.UnicodeUTF8))
        self.formTitleLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Rosewood Initiative Volunteer Application</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.iContributeLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "<html><head/><body><p><span style=\" font-weight:600;\">I would like to contribute to </span></p><p><span style=\" font-weight:600;\">Rosewood in the following areas:</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.anywhereCheckbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Anywhere ", None, QtGui.QApplication.UnicodeUTF8))
        self.cafeCheckbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Cafe", None, QtGui.QApplication.UnicodeUTF8))
        self.administrationCheckbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Administration", None, QtGui.QApplication.UnicodeUTF8))
        self.communityCheckbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Community Activities", None, QtGui.QApplication.UnicodeUTF8))
        self.YouthCheckbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Youth Programs", None, QtGui.QApplication.UnicodeUTF8))
        self.otherCheckbox.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Other:", None, QtGui.QApplication.UnicodeUTF8))
        self.areasOfInteresLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "Enter other areas of interest", None, QtGui.QApplication.UnicodeUTF8))
        self.mondayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.mondayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.MondayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Monday", None, QtGui.QApplication.UnicodeUTF8))
        self.tuesdayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Tuesday", None, QtGui.QApplication.UnicodeUTF8))
        self.wednesdayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Wednesday", None, QtGui.QApplication.UnicodeUTF8))
        self.thursdayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Thursday", None, QtGui.QApplication.UnicodeUTF8))
        self.fridayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Friday", None, QtGui.QApplication.UnicodeUTF8))
        self.saturdayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Saturday", None, QtGui.QApplication.UnicodeUTF8))
        self.sundayLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "Sunday", None, QtGui.QApplication.UnicodeUTF8))
        self.TuesdayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.wednesdayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.thursdayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.fridayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.saturdayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.sundayFromLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "From ", None, QtGui.QApplication.UnicodeUTF8))
        self.wednesdayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.tuesdayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.thursdayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.fridayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.saturdayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.sundayToLineEdit.setPlaceholderText(QtGui.QApplication.translate("NewVolunteerDialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.availabilityLabel.setText(QtGui.QApplication.translate("NewVolunteerDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Availability: </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("NewVolunteerDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Employment:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
