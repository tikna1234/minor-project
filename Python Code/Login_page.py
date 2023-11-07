#login page
import sys
import menu_page
from PyQt5 import QtCore, QtGui, QtWidgets
class Login_page(object):
    def __init__(self, menu_page):
        super().__init__()
        self.menu_page = menu_page
        self.initUI()
    def setupUi(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500,500)
        #username{
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50,50, 151, 30))
        self.label.setText("username")
        self.txt1=QtWidgets.QLineEdit(Dialog)
        self.txt1.setGeometry(QtCore.QRect(160,50,150,30))
        self.txt1.setPlaceholderText("enter username")
        #}
        #password{
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50,90, 151, 30))
        self.label.setText("password")
        self.txt1=QtWidgets.QLineEdit(Dialog)
        self.txt1.setGeometry(QtCore.QRect(160,90,150,30))
        self.txt1.setPlaceholderText("enter password")
        #}
        #login button{
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(100, 150, 90, 30))
        #}
        #Register{
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(250, 150, 90, 30))
        #}
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200,200, 150, 30))
        self.label.setText("")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.loginButton.clicked.connect(self.Login)
    def retranslateUi(self,Dialog):
        _translate=QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Page"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.registerButton.setText(_translate("Dialog", "Register"))
    def Login(self):
        self.label.setText("login successful")
        new_window=menu_page()
        new_window.show()
        self.close

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    menu_window=menu_page()
    Login_page=Login_page(menu_page)
    Login_page.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
