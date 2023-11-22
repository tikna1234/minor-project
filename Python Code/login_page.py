# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
con = sqlite3.connect("G:\minorproject\Database\Career_Recommedation_System.db")

class Ui_loginWindow(object):
    def OpenRegistration(self, loginWindow):
        from registration_page import Ui_RegistrationWIndow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegistrationWIndow()
        self.ui.setupUi(self.window)
        self.window.show()
        loginWindow.hide()
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(422, 343)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UserIDLbl = QtWidgets.QLabel(self.centralwidget)
        self.UserIDLbl.setGeometry(QtCore.QRect(70, 90, 71, 16))
        self.UserIDLbl.setObjectName("UserIDLbl")
        self.UserIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserIDLineEdit.setGeometry(QtCore.QRect(150, 85, 113, 22))
        self.UserIDLineEdit.setObjectName("UserIDLineEdit")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(30, 200, 93, 28))
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(lambda: self.Login(loginWindow))
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(290, 200, 93, 28))
        self.RegisterButton.setObjectName("RegisterButton")
        self.RegisterButton.clicked.connect(lambda: self.OpenRegistration(loginWindow))
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 26))
        self.menubar.setObjectName("menubar")
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login_Page"))
        self.UserIDLbl.setText(_translate("loginWindow", "User ID:"))
        self.LoginButton.setText(_translate("loginWindow", "Login"))
        self.RegisterButton.setText(_translate("loginWindow", "Register"))

    def gotomenu(self, loginWindow, message):
        from menu_page import Ui_MenuWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.ui.LoginMsgLbl.setText(message)
        self.window.show()
        loginWindow.hide()

    def LoginMsg(self, loginWindow, message):
        from after_registration import Ui_MsgWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MsgWindow()
        self.ui.setupUi(self.window)
        self.ui.RegistrationMsgLbl.setText(message)
        self.window.show()
        loginWindow.hide()

    def fetchname(self, user_id):
        statement = f"SELECT First_name from user_info WHERE User_id='{user_id}';"
        self.cur.execute(statement)
        result = self.cur.fetchone()
        name = result[0] if result else ""
        return name

    def Login(self, loginWindow):
        user_id = self.UserIDLineEdit.text()
        statement = f"SELECT User_id from user_info WHERE User_id='{user_id}';"
        self.cur.execute(statement)
        if not self.cur.fetchone():
            self.LoginMsg(loginWindow, "Login failed")
        else:
            name = self.fetchname(user_id)
            self.gotomenu(loginWindow, f"Welcome, {name}. Please enter your information here:")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
