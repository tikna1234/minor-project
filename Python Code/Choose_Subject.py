# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choose Subject.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random as rndm
import pandas as pd
import numpy as np

class Ui_SubjectWindow(object):
    def setupUi(self, SubjectWindow):
        self.User_id = ""
        SubjectWindow.setObjectName("SubjectWindow")
        SubjectWindow.resize(371, 428)
        self.centralwidget = QtWidgets.QWidget(SubjectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnglishButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnglishButton.setGeometry(QtCore.QRect(50, 70, 93, 28))
        self.EnglishButton.setObjectName("EnglishButton")
        self.EnglishButton.clicked.connect(lambda: self.EngTest(SubjectWindow))
        self.ScienceButton = QtWidgets.QPushButton(self.centralwidget)
        self.ScienceButton.setGeometry(QtCore.QRect(230, 70, 93, 28))
        self.ScienceButton.setObjectName("ScienceButton")
        self.ScienceButton.clicked.connect(lambda: self.SciTest(SubjectWindow))
        self.MathsButton = QtWidgets.QPushButton(self.centralwidget)
        self.MathsButton.setGeometry(QtCore.QRect(50, 150, 93, 28))
        self.MathsButton.setObjectName("MathsButton")
        self.MathsButton.clicked.connect(lambda: self.MathTest(SubjectWindow))
        self.LogicalReasoningButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogicalReasoningButton.setGeometry(QtCore.QRect(230, 150, 121, 28))
        self.LogicalReasoningButton.setObjectName("LogicalReasoningButton")
        self.LogicalReasoningButton.clicked.connect(lambda: self.LGTest(SubjectWindow))
        self.SSTButton = QtWidgets.QPushButton(self.centralwidget)
        self.SSTButton.setGeometry(QtCore.QRect(50, 230, 93, 28))
        self.SSTButton.setObjectName("SSTButton")
        self.SSTButton.clicked.connect(lambda: self.SStTest(SubjectWindow))
        self.ComputerButton = QtWidgets.QPushButton(self.centralwidget)
        self.ComputerButton.setGeometry(QtCore.QRect(230, 230, 93, 28))
        self.ComputerButton.setObjectName("ComputerButton")
        self.ComputerButton.clicked.connect(lambda: self.CompTest(SubjectWindow))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(140, 310, 93, 28))
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(lambda: self.Back(SubjectWindow))
        SubjectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubjectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 26))
        self.menubar.setObjectName("menubar")
        SubjectWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubjectWindow)
        self.statusbar.setObjectName("statusbar")
        SubjectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubjectWindow)
        QtCore.QMetaObject.connectSlotsByName(SubjectWindow)

    def retranslateUi(self, SubjectWindow):
        _translate = QtCore.QCoreApplication.translate
        SubjectWindow.setWindowTitle(_translate("SubjectWindow", "Choose Subject"))
        self.EnglishButton.setText(_translate("SubjectWindow", "English"))
        self.ScienceButton.setText(_translate("SubjectWindow", "Science"))
        self.MathsButton.setText(_translate("SubjectWindow", "Mathematics"))
        self.LogicalReasoningButton.setText(_translate("SubjectWindow", "Logical Reasoning"))
        self.SSTButton.setText(_translate("SubjectWindow", "Social Studies"))
        self.ComputerButton.setText(_translate("SubjectWindow", "Computer"))
        self.label.setText(_translate("SubjectWindow", "Click the Subject you to Take a Test In"))
        self.BackButton.setText(_translate("SubjectWindow", "Back"))

    def Back(self, SubjectWindow):
        from menu_page import Ui_MenuWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        SubjectWindow.hide()

    def EngTest(self, SubjectWindow):
        from take_test_all_other_questions import Ui_TakeTestWindow
        data = pd.read_excel(r"G:\reps\minor-project\Datasets\english_questions.xlsx")
        Questions = []
        ans=[]
        while(len(Questions)!=25):
            r = rndm.randint(0,50)
            if(r not in Questions):
                Questions.append(r)
            else:
                continue
        for i in Questions:
            ans.append(data.iloc[i,5])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.ui.English = Questions
        self.ui.ans = ans
        self.ui.RenderQ(0)
        self.window.show()
        SubjectWindow.hide()

    def MathTest(self, SubjectWindow):
        from take_test_all_other_questions import Ui_TakeTestWindow
        data = pd.read_excel(r"G:\reps\minor-project\Datasets\Mathematics_questions.xlsx")
        Questions = []
        ans=[]
        while(len(Questions)!=25):
            r = rndm.randint(0,53)
            if(r not in Questions):
                Questions.append(r)
            else:
                continue
        for i in Questions:
            ans.append(data.iloc[i,5])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.ui.Mathematics = Questions
        self.ui.ans = ans
        self.ui.RenderQ(0)
        self.window.show()
        SubjectWindow.hide()

    def SStTest(self, SubjectWindow):
        from take_test_all_other_questions import Ui_TakeTestWindow
        data = pd.read_excel(r"G:\reps\minor-project\Datasets\Social_Studies_questions.xlsx")
        Questions = []
        ans=[]
        while(len(Questions)!=25):
            r = rndm.randint(0,51)
            if(r not in Questions):
                Questions.append(r)
            else:
                continue
        for i in Questions:
            ans.append(data.iloc[i,5])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.ui.Social_Studies = Questions
        self.ui.ans = ans
        self.ui.RenderQ(0)
        self.window.show()
        SubjectWindow.hide()

    def SciTest(self, SubjectWindow):
        from take_test_all_other_questions import Ui_TakeTestWindow
        data = pd.read_excel(r"G:\reps\minor-project\Datasets\Science_questions.xlsx")
        Questions = []
        ans=[]
        while(len(Questions)!=25):
            r = rndm.randint(0,50)
            if(r not in Questions):
                Questions.append(r)
            else:
                continue
        for i in Questions:
            ans.append(data.iloc[i,5])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.ui.Science = Questions
        self.ui.ans = ans
        self.ui.RenderQ(0)
        self.window.show()
        SubjectWindow.hide()

    def LGTest(self, SubjectWindow):
        from take_test_all_other_questions import Ui_TakeTestWindow
        data = pd.read_excel(r"G:\reps\minor-project\Datasets\Logical_Reasoning_questions.xlsx")
        Questions = []
        ans=[]
        while(len(Questions)!=25):
            r = rndm.randint(0,50)
            if(r not in Questions):
                Questions.append(r)
            else:
                continue
        for i in Questions:
            ans.append(data.iloc[i,5])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.ui.Logical_Reasoning = Questions
        self.ui.ans = ans
        self.ui.RenderQ(0)
        self.window.show()
        SubjectWindow.hide()

    def CompTest(self, SubjectWindow):
        from take_test_all_other_questions import Ui_TakeTestWindow
        data = pd.read_excel(r"G:\reps\minor-project\Datasets\Computer_questions.xlsx")
        Questions = []
        ans=[]
        while(len(Questions)!=25):
            r = rndm.randint(0,42)
            if(r not in Questions):
                Questions.append(r)
            else:
                continue
        for i in Questions:
            ans.append(data.iloc[i,5])
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TakeTestWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.ui.Computer = Questions
        self.ui.ans = ans
        self.ui.RenderQ(0)
        self.window.show()
        SubjectWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubjectWindow = QtWidgets.QMainWindow()
    ui = Ui_SubjectWindow()
    ui.setupUi(SubjectWindow)
    SubjectWindow.show()
    sys.exit(app.exec_())
