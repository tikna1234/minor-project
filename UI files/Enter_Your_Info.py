# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Enter Your Info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterInfoWindow(object):
    def setupUi(self, EnterInfoWindow):
        EnterInfoWindow.setObjectName("EnterInfoWindow")
        EnterInfoWindow.resize(798, 611)
        self.centralwidget = QtWidgets.QWidget(EnterInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnterInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterInfoButton.setGeometry(QtCore.QRect(150, 460, 93, 28))
        self.EnterInfoButton.setObjectName("EnterInfoButton")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(390, 460, 93, 28))
        self.BackButton.setObjectName("BackButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 115, 71, 16))
        self.label_2.setObjectName("label_2")
        self.EnglishLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EnglishLineEdit.setGeometry(QtCore.QRect(190, 110, 113, 22))
        self.EnglishLineEdit.setObjectName("EnglishLineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 185, 81, 16))
        self.label_3.setObjectName("label_3")
        self.MathsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MathsLineEdit.setGeometry(QtCore.QRect(190, 180, 113, 22))
        self.MathsLineEdit.setObjectName("MathsLineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 255, 91, 16))
        self.label_4.setObjectName("label_4")
        self.SstLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SstLineEdit.setGeometry(QtCore.QRect(190, 250, 113, 22))
        self.SstLineEdit.setObjectName("SstLineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 115, 55, 16))
        self.label_5.setObjectName("label_5")
        self.ScienceLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ScienceLineEdit.setGeometry(QtCore.QRect(560, 110, 113, 22))
        self.ScienceLineEdit.setObjectName("ScienceLineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 185, 61, 16))
        self.label_6.setObjectName("label_6")
        self.ComputerLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ComputerLineEdit.setGeometry(QtCore.QRect(560, 180, 113, 22))
        self.ComputerLineEdit.setObjectName("ComputerLineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 340, 171, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.InterestsCB = QtWidgets.QComboBox(self.centralwidget)
        self.InterestsCB.setGeometry(QtCore.QRect(280, 335, 331, 22))
        self.InterestsCB.setObjectName("InterestsCB")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.InterestsCB.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 510, 581, 41))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        EnterInfoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EnterInfoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        EnterInfoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EnterInfoWindow)
        self.statusbar.setObjectName("statusbar")
        EnterInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EnterInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(EnterInfoWindow)

    def retranslateUi(self, EnterInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        EnterInfoWindow.setWindowTitle(_translate("EnterInfoWindow", "Information_Page"))
        self.EnterInfoButton.setText(_translate("EnterInfoWindow", "ENTER INFO"))
        self.BackButton.setText(_translate("EnterInfoWindow", "Back"))
        self.label.setText(_translate("EnterInfoWindow", "Enter your Details"))
        self.label_2.setText(_translate("EnterInfoWindow", "English:"))
        self.label_3.setText(_translate("EnterInfoWindow", "Mathematics:"))
        self.label_4.setText(_translate("EnterInfoWindow", "Social Studies:"))
        self.label_5.setText(_translate("EnterInfoWindow", "Science:"))
        self.label_6.setText(_translate("EnterInfoWindow", "Computer:"))
        self.label_7.setText(_translate("EnterInfoWindow", "what are you interested in:"))
        self.label_8.setText(_translate("EnterInfoWindow", "Enter your class 10 marks below:"))
        self.InterestsCB.setItemText(0, _translate("EnterInfoWindow", "Computer Science and Information Technology"))
        self.InterestsCB.setItemText(1, _translate("EnterInfoWindow", "Mechanical and Electrical"))
        self.InterestsCB.setItemText(2, _translate("EnterInfoWindow", "Electronics and Communication"))
        self.InterestsCB.setItemText(3, _translate("EnterInfoWindow", "Construction and Design"))
        self.InterestsCB.setItemText(4, _translate("EnterInfoWindow", "Hospitality and Event Management"))
        self.InterestsCB.setItemText(5, _translate("EnterInfoWindow", "Life Sciences and Environment"))
        self.InterestsCB.setItemText(6, _translate("EnterInfoWindow", "Arts and Media"))
        self.InterestsCB.setItemText(7, _translate("EnterInfoWindow", "Physical Education and Wellness"))
        self.InterestsCB.setItemText(8, _translate("EnterInfoWindow", "FInance, Bussiness and Marketing"))
        self.InterestsCB.setItemText(9, _translate("EnterInfoWindow", "Culinary Studies and Cooking"))
        self.label_9.setText(_translate("EnterInfoWindow", "Note: if you are not satisfied with your marks in certain subject then feel free to give a test for them! Note: Please Give a Test for Logical Reasoning from the Menu before checking your Report!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterInfoWindow = QtWidgets.QMainWindow()
    ui = Ui_EnterInfoWindow()
    ui.setupUi(EnterInfoWindow)
    EnterInfoWindow.show()
    sys.exit(app.exec_())