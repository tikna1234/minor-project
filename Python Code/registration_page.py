# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from after_registration import Ui_MsgWindow
import sqlite3
con = sqlite3.connect("G:\minorproject\Database\Career_Recommedation_System.db")

class Ui_RegistrationWIndow(object):
    def setupUi(self, RegistrationWIndow):
        self.cur = con.cursor()
        RegistrationWIndow.setObjectName("RegistrationWIndow")
        RegistrationWIndow.resize(339, 440)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        RegistrationWIndow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(RegistrationWIndow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.RegistrationLbl = QtWidgets.QLabel(self.splitter)
        self.RegistrationLbl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.RegistrationLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.RegistrationLbl.setObjectName("RegistrationLbl")
        self.verticalLayout.addWidget(self.splitter)
        self.FirstNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.FirstNameLbl.setObjectName("FirstNameLbl")
        self.verticalLayout.addWidget(self.FirstNameLbl)
        self.FirstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstNameLineEdit.setObjectName("FirstNameLineEdit")
        self.verticalLayout.addWidget(self.FirstNameLineEdit)
        self.LastNameLbl = QtWidgets.QLabel(self.centralwidget)
        self.LastNameLbl.setObjectName("LastNameLbl")
        self.verticalLayout.addWidget(self.LastNameLbl)
        self.LastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LastNameLineEdit.setObjectName("LastNameLineEdit")
        self.verticalLayout.addWidget(self.LastNameLineEdit)
        self.UserIdLbl = QtWidgets.QLabel(self.centralwidget)
        self.UserIdLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UserIdLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UserIdLbl.setObjectName("UserIdLbl")
        self.verticalLayout.addWidget(self.UserIdLbl)
        self.UserIdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserIdLineEdit.setObjectName("UserIdLineEdit")
        self.verticalLayout.addWidget(self.UserIdLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setObjectName("RegisterButton")
        self.RegisterButton.clicked.connect(lambda: self.Register(RegistrationWIndow))
        self.verticalLayout.addWidget(self.RegisterButton)
        RegistrationWIndow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWIndow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 26))
        self.menubar.setObjectName("menubar")
        RegistrationWIndow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWIndow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWIndow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrationWIndow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWIndow)

    def retranslateUi(self, RegistrationWIndow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWIndow.setWindowTitle(_translate("RegistrationWIndow", "Registration_Page"))
        self.RegistrationLbl.setText(_translate("RegistrationWIndow", "Registration"))
        self.FirstNameLbl.setText(_translate("RegistrationWIndow", "First Name"))
        self.LastNameLbl.setText(_translate("RegistrationWIndow", "Last Name"))
        self.UserIdLbl.setText(_translate("RegistrationWIndow", "User ID"))
        self.RegisterButton.setText(_translate("RegistrationWIndow", "Register"))

    def RegistrationMsg(self, RegistrationWIndow, message):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MsgWindow()
        self.ui.setupUi(self.window)
        self.ui.RegistrationMsgLbl.setText(message)
        self.window.show()
        RegistrationWIndow.hide()
    
    def Register(self,RegistrationWIndow):
        try:
            firstname=self.FirstNameLineEdit.text()
            lastname=self.LastNameLineEdit.text()
            userid=self.UserIdLineEdit.text()
            statement= f"INSERT INTO user_info VALUES('{userid}', '{firstname}', '{lastname}')"
            self.cur.execute(statement)
            con.commit()
            self.RegistrationMsg(RegistrationWIndow, "Your Registration was successful")
        except Exception as e:
            errmsg=f"Error during registration: {str(e)}"
            self.RegistrationMsg(RegistrationWIndow, errmsg)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWIndow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWIndow()
    ui.setupUi(RegistrationWIndow)
    RegistrationWIndow.show()
    sys.exit(app.exec_())