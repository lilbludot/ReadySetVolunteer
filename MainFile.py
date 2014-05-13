from PySide.QtCore import *
from PySide.QtGui import *

import sys

import FirstGui
import ProjectGui
import loginGui
import newVolunteerGui
import volunteerLoginGui


class Window1(QMainWindow, FirstGui.Ui_firstWindow):
    """ The first window (QMainWindow) that opens as the ReadySet Volunteer program is run.
    """

    def __init__(self, parent = None):
        super(Window1, self).__init__(parent)
        self.setupUi(self)


        #connecting the two main buttons:
        self.connect(self.projectMngmntQToolButton, SIGNAL("clicked()"), self.projectPopup)
        self.connect(self.loginLogoutqToolButton, SIGNAL("clicked()"), self.loginPopup)

        #connecting the menubar items:
        self.connect(self.actionExit, SIGNAL("triggered()"), SLOT("close()"))


    #defining the methods for the buttons and other items in the window:

    def projectPopup(self):
        self.x = ProjectsWindow()
        self.x.show()

    def loginPopup(self):
        self.y = LoginWindow()
        self.y.show()

    def exitWindow(self):
        self.close()





class ProjectsWindow(QMainWindow, ProjectGui.Ui_projectWindow):
    """ This QMainWindow window contains the volunteer projects in a table.
    """

    def __init__(self, parent = None):
        super(ProjectsWindow, self).__init__(parent)
        self.setupUi(self)

        #connecting the menubar items:
        self.connect(self.actionExit, SIGNAL("triggered()"), SLOT("close()"))

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Sample"))

    def exitWindow(self):
        self.close()

class LoginWindow(QDialog, loginGui.Ui_loginDialog):
    """ This QDialog window contains the login options: volunteer, first time volunteer and guest.
    """

    def __init__(self, parent = None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)

        #connecting the three main buttons and the cancel button:
        self.connect(self.cancelButton, SIGNAL("clicked()"), self.exitWindow)
        self.connect(self.volunteerButton, SIGNAL("clicked()"), self.volunteerLoginPopup)
        self.connect(self.newVolunteerButton, SIGNAL("clicked()"), self.newVolunteerLoginPopup)

    def exitWindow(self):
        self.close()

    def volunteerLoginPopup(self):
        self.y = VolunteerLoginWindow()
        self.y.show()

    def newVolunteerLoginPopup(self):
        self.y = NewVolunteerLoginWindow()
        self.y.show()


class VolunteerLoginWindow(QDialog, volunteerLoginGui.Ui_volunteerDialog):
    """
    This Qdialog window deals with volunteer login.
    """

    def __init__(self, parent = None):
        super(VolunteerLoginWindow, self).__init__(parent)
        self.setupUi(self)

        #connecting the cancel button:
        self.connect(self.cancelButton, SIGNAL("clicked()"), self.exitWindow)

    def exitWindow(self):
        self.close()

class NewVolunteerLoginWindow(QDialog, newVolunteerGui.Ui_NewVolunteerDialog):
    """
    This QDialog Window deals with registering the first time volunteers.
    """

    def __init__(self, parent = None):
        super(NewVolunteerLoginWindow, self).__init__(parent)
        self.setupUi(self)

        #connecting the cancle and ok buttons:
        self.connect(self.buttonBox, SIGNAL("accepted()"), self.saveform)
        self.connect(self.buttonBox, SIGNAL("rejected()"), SLOT("reject()"))



    def saveform(self):
        firstName = self.firstNameLineEdit.text()
        lastName = self.lastNameLineEdit.text()
        mi = self.miLineEdit.text()
        street = self.streetLineEdit.text()
        birthdate = self.birthdateLineEdit.text()
        aptNumber = self.aptUnitLineEdit.text()
        city = self.cityLineEdit.text()
        state = self.stateLineEdit.text()
        zipCode = self.zipCodeLineEdit.text()
        homePhone = self.homePhoneLineEdit.text()
        altPhone = self.altPhoneLineEdit.text()
        email = self.emailLineEdit.text()
        parentGuardian = self.parentGuardianLineEdit.text()
        employment = self.employmentLineEdit.text()
        empStreet = self.empStreetLineEdit.text()
        empCity = self.empCityLineEdit.text()
        empState = self.empStateLineEdit.text()
        empZipCode = self.empZipCodeLineEdit.text()
        emergencyContactFirstName = self.emergFirstLineEdit.text()
        emergencyContactLastName = self.emergLastLineEdit.text()
        emergencyContactRelationship = self.emergRelationshipLineEdit.text()
        emergencyContactPhone = self.emergPhoneLineEdit.text()



        if firstName == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out First Name!")
            self.firstNameLineEdit.setFocus()
        elif lastName == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Last Name")
            self.lastNameLineEdit.setFocus()
        elif birthdate == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Birthdate")
            self.birthdateLineEdit.setFocus()
        elif self.youngerThan18Checkbox.isChecked() and parentGuardian == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Parent/ Legal Guardian Name")
            self.parentGuardianLineEdit.setFocus()
        elif street == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Street Address")
            self.streetLineEdit.setFocus()
        elif city == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out City")
            self.cityLineEdit.setFocus()
        elif state == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out State")
            self.stateLineEdit.setFocus()
        elif zipCode == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Zip Code")
            self.zipCodeLineEdit.setFocus()
        elif homePhone == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Home Phone")
            self.homePhoneLineEdit.setFocus()
        elif emergencyContactFirstName == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Emergency Contact's First Name")
            self.emergFirstLineEdit.setFocus()
        elif emergencyContactLastName == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Emergency Contact's Last Name")
            self.emergLastLineEdit.setFocus()
        elif emergencyContactPhone == "":
            QMessageBox.information(self, "Incomplete information", "Please fill out Emergency Contact Phone Number")
            self.emergPhoneLineEdit.setFocus()

        else:
            self.close()

app = QApplication(sys.argv)
form = Window1()
form.show()
app.exec_()




