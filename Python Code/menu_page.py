# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from model import Printpred, PrintBranch
import pandas as pd
import numpy as np
import pickle
import sqlite3
import os

def find_file_path(file_name):
    for root, dirs, files in os.walk(os.path.abspath(os.sep)):
        if file_name in files:
            return os.path.join(root, file_name)

    return f"File '{file_name}' not found"

career = pd.read_excel(find_file_path('student_marksheet_final3.xlsx'))
con = sqlite3.connect(find_file_path('Career_Recommedation_System.db'))
class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        self.diploma = {
            "Computer Science and Information Technology (Diploma)":

            ["Diploma in Computer Science",
            "Diploma in Digital Marketing",
            "Diploma in Mobile App Development",
            "Diploma in Cybersecurity",
            "Diploma in Web Development"
            ],

            "Mechanical and Electrical (Diploma)":

            ["Diploma in Mechanical Engineering",
            "Diploma in Electrical Engineering",
            "Diploma in Automobile Engineering",
            "Diploma in Chemical Engineering",
            ],

            "Electronics and Communication (Diploma)":

            "Diploma in Electronics and Communication"
            ,

            "Construction and Design (Diploma)":

            [
            "Diploma in Architecture",
            "Diploma in Civil Engineering",
            "Diploma in Interior Design"
            ],

            "Hospitality and Event Management (Diploma)":

            [
            "Diploma in Hotel Management",
            "Diploma in Event Management",
            "Diploma in Aviation and Hospitality Management"
            ],

            "Life Sciences and Environment (Diploma)":
            [
            "Diploma in Biotechnology",
            "Diploma in Environmental Science",
            "Diploma in Veterinary Science"
            ],
            
            "Arts and Media (Diploma)":
            [
            "Diploma in Animation and Multimedia",
            "Diploma in Film Making and Direction",
            "Diploma in Photography"
            ],

            "Physical Education and Wellness (Diploma)":
            [
            "Diploma in Early Childhood Education",
            "Diploma in Yoga and Wellness"
            ],

            "Finance, Business and Marketing (Diploma)":
            
            "Diploma in Financial Accounting"
            

            }



        self.iti = {
            "Computer Science and Information Technology (ITI)":

            [
            "ITI in Computer Hardware and Networking",
            "ITI in Information Technology",
            "ITI in Mobile Repair and Maintenance"
            ],

            "Mechanical and Electrical (ITI)":
            [
             "ITI in Mechanical",
            "ITI in Automotive Technology",
            "ITI in Welding and Fabrication",
            "ITI in Fitter and Turner",
            "ITI in Machinist",
            "ITI in Foundry and Pattern Making",
            "ITI in CNC Operator"
            ],

            "Electronics and Communication (ITI)":
            [
            "ITI in Electronics and Communication",
            "ITI in Instrumentation and Control",
            ],

            "Construction and Design (ITI)":
            [
            "ITI in Plumbing and Pipefitting",
            "ITI in Carpentry and Woodworking"
            ],
            
            "Physical Education and Wellness (ITI)":
            
            "ITI in Beauty and Wellness"
            

            }
            


        self.vocational = {"Computer Science and Information Technology (Vocational)":

            [
            "Vocational Training in Data Entry and Office Automation",
            "Vocational Training in Computer Programming",
            "Vocational Training in Mobile App Development",
            "Vocational Training in Web Development",
            "Vocational Training in Computer Hardware and Networking",
            "Vocational Training in Mobile Phone Repair Technician"
            ],

            "Mechanical and Electrical (Vocational)":
            [
            "Vocational Training in Welding Technician",
            "Vocational Training in Automotive Technician",
            "Vocational Training in Electrician",
            "Vocational Training in AutoCAD and Drafting Certification",
            "Vocational Training in Robotics and Automation Workshop",
            "Vocational Training in Machinist and CNC Operator",
            " Vocational Training in HVAC Technician"
            ],
            
            "Construction and Design (Vocational)":
            [
            "Vocational Training in Welding Technician",
            "Vocational Training in Plumbing and Pipefitting",
            "Vocational Training in Carpentry and Woodworking"
            ],

            "Hospitality and Event Management (Vocational)":
            [
            "Vocational Training in Hospitality and Customer Service",
            "Vocational Training in Healthcare Assistant Training",
            "Vocational Training in Basic First Aid and Safety Training",
            "Vocational Training in Retail Sales and Customer Service"
            ],

            "Arts and Media (Vocational)":
            [
            "Vocational Training in Graphic design Essentials",
            "Vocational Training in Digital Marketing Certification",
            "Vocational Training in Photography and Videography Course",
            "Vocational Training in Fashion Design and Tailoring",
            "Vocational Training in Language Proficiency Course"
            ],
            
            "Physical Education and Wellness (Vocational)":
            
            "Vocational Training in Beauty and Makeup Artistry"
            ,

            "Finance, Business and Marketing (Vocational)":
            [
            "Vocational Training in Digital Marketing Certification",
            "Vocational Training in Entrepreneurship and Business Skills"
            ],

            "Culinary Studies and Cooking (Vocational)":
            [
            "Vocational Training in Culinary arts and Cooking",
            "Vocational Training in Baking and Pastry Arts",
            "Vocational Training in Food Safety and Hygiene Certification"
            ]
                 }
        
        self.ITIReq = {"Computer Science and Information Technology":[60,65,60,40,60,65],
          "Mechanical and Electrical":[60,65,65,40,60,60],
          "Electronics and Communication":[60,65,65,40,56,60],
          "Construction and Design":[60,65,65,40,60,56],
          "Physical Education and Wellness":[65,60,65,40,60,56]}
        self.DiplomaReq = {"Computer Science and Information Technology":[75,81,75,40,75,81] ,
              "Mechanical and Electrical":[75,81,81,40,75,75],
              "Electronics and Communication":[75,75,81,40,75,81],
              "Construction and Design":[75,75,75,81,81,75],
              "Hospitality and Event Management":[81,40,40,81,75,75],
              "Life Sciences and Environment":[75,75,81,40,40,40],
              "Arts and Media":[81,40,40,81,75,75],
              "Physical Education and Wellness":[81,40,81,40,75,75],
              "Finance, Business and Marketing":[81,81,40,40,81,75]}
        education_stylesheet = """
            QWidget {
                background-color: #C32148; 
                color: white; 
            }
            QLabel {
                font-family: MS Shell Dlg 2;
                font-size: 14px;
                font-weight: bold;
                color: white;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
            }
            
           
        """
        MenuWindow.setStyleSheet(education_stylesheet)
        self.cur = con.cursor()
        self.User_id = ""
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(518, 391)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        MenuWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(276, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.LoginMsgLbl = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LoginMsgLbl.setFont(font)
        self.LoginMsgLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginMsgLbl.setObjectName("LoginMsgLbl")
        self.EnterButton = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.EnterButton.setFont(font)
        self.EnterButton.setObjectName("EnterButton")
        self.EnterButton.clicked.connect(lambda: self.infopage(MenuWindow))
        self.verticalLayout.addWidget(self.splitter_2)
        spacerItem1 = QtWidgets.QSpacerItem(269, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.TakeTestButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.TakeTestButton.setFont(font)
        self.TakeTestButton.setObjectName("TakeTestButton")
        self.TakeTestButton.clicked.connect(lambda: self.ChooseSub(MenuWindow))
        self.GenerateReportButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.GenerateReportButton.setFont(font)
        self.GenerateReportButton.setObjectName("GenerateReportButton")
        self.GenerateReportButton.clicked.connect(lambda: self.clicked_generate_report(MenuWindow))
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 26))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "Menu_page"))
        self.label.setText(_translate("MenuWindow", "MENU"))
        self.LoginMsgLbl.setText(_translate("MenuWindow", "Enter your class 10 marks here :"))
        self.EnterButton.setText(_translate("MenuWindow", "Enter"))
        self.TakeTestButton.setText(_translate("MenuWindow", "Take Test"))
        self.GenerateReportButton.setText(_translate("MenuWindow", "Generate Report"))

    def fetchsubjects(self):
        user_id = self.User_id
        statement = f"SELECT English, Hindi, Mathematics, Social_Studies, Science, Computer, Interests, counter from User_Marks WHERE User_id='{user_id}';"
        try:
            self.cur.execute(statement)
            result = self.cur.fetchone()
            if result:
                english, hindi, mathematics, social_studies, science, computer, interests, counter = result
            else:
                english, hindi, mathematics, social_studies, science, computer, interests, counter = 0, 0, 0, 0, 0, 0, "Select", 0
            return english, hindi, mathematics, social_studies, science, computer, interests, counter
        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
            QMessageBox.critical(None, "Error", error_message, QMessageBox.Ok)
            return 0, 0, 0, 0, 0, 0, "Select", 0
        
    def fetchallsubjects(self):
        user_id = self.User_id
        statement = f"SELECT English, Mathematics, Science, Social_Studies, Logical_Reasoning, Computer, Interests from User_Marks WHERE User_id='{user_id}';"
        try:
            self.cur.execute(statement)
            result = self.cur.fetchone()
            if result:
                english, mathematics, science, social_studies, logical_reasoning, computer, interests = result
            else:
                english, mathematics, science, social_studies, logical_reasoning, computer, interests = 0, 0, 0, 0, 0, 0, "Select"
            return english, mathematics, science, social_studies, logical_reasoning, computer, interests
        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
            QMessageBox.critical(None, "Error", error_message, QMessageBox.Ok)
            return 0, 0, 0, 0, 0, 0, "Select"
        
    def infopage(self, MenuWindow):
        from Enter_Your_Info import Ui_EnterInfoWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EnterInfoWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        english, hindi, mathematics, social_studies, science, computer, interests, counter = self.fetchsubjects()
        self.ui.EnglishLineEdit.setText(f"{english}")
        self.ui.HindiLineEdit.setText(f"{hindi}")
        self.ui.MathsLineEdit.setText(f"{mathematics}")
        self.ui.SstLineEdit.setText(f"{social_studies}")
        self.ui.ScienceLineEdit.setText(f"{science}")
        self.ui.InterestsCB.setCurrentText(f"{interests}")
        self.ui.counter = counter
        self.window.show()
        MenuWindow.hide()

    def ChooseSub(self, MenuWindow):
        from Choose_Subject import Ui_SubjectWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SubjectWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.window.show()
        MenuWindow.hide()

    def fetchname(self, user_id):
        statement = f"SELECT First_name from user_info WHERE User_id='{user_id}';"
        self.cur.execute(statement)
        result = self.cur.fetchone()
        name = result[0] if result else ""
        return name

    def clicked_generate_report(self, MenuWindow):
        recommend = ""
        courses = []
        branch = 0
        ITIsubs = []
        Diplomasubs = []
        weaksubs = []
        english, mathematics, science, social_studies, logical_reasoning, computer, interests = self.fetchallsubjects()
        ITIsubs = [english,mathematics,science,logical_reasoning,computer]
        Diplomasubs = [english,mathematics,science,social_studies,logical_reasoning,computer]
        recommend, courses, branch = self.Gencourses()
        if branch == 0:
            weaksubs = self.CheckRequirementsDiploma(interests,Diplomasubs)
        elif branch == 1 and interests in self.ITIReq:
            weaksubs = self.CheckRequirementsITI(interests,ITIsubs)
        else:
            weaksubs = []
        self.GenReport(MenuWindow, recommend, courses, branch, weaksubs)
        
    
    def Gencourses(self):
        english, mathematics, science, social_studies, logical_reasoning, computer, interests = self.fetchallsubjects()
        branch = PrintBranch(english, mathematics, science, social_studies, logical_reasoning, computer)
        recommend = Printpred(english, mathematics, science, social_studies, logical_reasoning, computer, branch)
        recommend = str(recommend).strip("['']")
        courses = []
        if "(Diploma)" in recommend:
            if recommend in self.diploma:
                courses = self.diploma[recommend]
        elif "(ITI)" in recommend:
            if recommend in self.iti:
                courses = self. iti[recommend]
        else:
            if recommend in self.vocational:
                courses =self. vocational[recommend]
        return recommend, courses, branch

    def CheckRequirementsITI(self,interest,subs):
        weaksubs = []
        for i in range(5):
            if self.ITIReq[interest][i] > subs[i]:
                if i == 0:
                    weaksubs.append("English")
                if i == 1:
                    weaksubs.append("Mathematics")
                if i == 2:
                    weaksubs.append("Science")
                if i == 3:
                    weaksubs.append("Logical_Reasoning")
                if i == 4:
                    weaksubs.append("Computer")
        return weaksubs

    def CheckRequirementsDiploma(self,interest,subs):
        weaksubs = []
        for i in range(6):
            if self.DiplomaReq[interest][i] > subs[i]:
                if i == 0:
                    weaksubs.append("English")
                if i == 1:
                    weaksubs.append("Mathematics")
                if i == 2:
                    weaksubs.append("Science")
                if i == 3:
                    weaksubs.append("Social_Studies")
                if i == 4:
                    weaksubs.append("Logical_Reasoning")
                if i == 5:
                    weaksubs.append("Computer")
        return weaksubs
        

    def GenReport(self, MenuWindow, recommend, courses, branch, weaksubs):
        from GenerateReport import Ui_ReportWindow
        temp = ""
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReportWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        name = self.fetchname(self.User_id)
        self.ui.StrtMsgLbl.setText(f"Dear, {name}")
        self.ui.RecomendLbl.setText(f"You have been recommended,{recommend}")
        '''for i in courses:
            temp = "\n".join(i)
        self.ui.label.setText(f"{temp}")'''
        if type(courses) is list:
            for i in range(len(courses)):
                self.ui.RecomCB.setItemText(i+1,f"{courses[i]}")
        else:
            self.ui.RecomCB.setItemText(1,f"{courses}")
        for i in range(len(weaksubs)):
            temp = "\n".join(weaksubs)
        self.ui.WeakLbl.setText(temp)
        self.ui.Branch = branch
        self.ui.weaksubs = weaksubs
        self.window.show()
        MenuWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())
