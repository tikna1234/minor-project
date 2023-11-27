# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from model import Printpred
import pandas as pd
import numpy as np
import pickle
import sqlite3
career = pd.read_excel(r"G:\reps\minor-project\Datasets\student_marksheet_final1.xlsx")
con = sqlite3.connect(r"G:\reps\minor-project\Database\Career_Recommedation_System.db")
class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        self.diploma = {
            "Computer Science and Information Technology":

            ["Diploma in Computer Science",
            "Diploma in Digital Marketing",
            "Diploma in Mobile App Development",
            "Diploma in Cybersecurity",
            "Diploma in Web Development"
            ],

            "Mechanical and Electrical":

            ["Diploma in Mechanical Engineering",
            "Diploma in Electrical Engineering",
            "Diploma in Automobile Engineering",
            "Diploma in Chemical Engineering",
            "Diploma in Mechatronics"
            ],

            "Electronics and Communication":

            ["Diploma in Electronics and Communication Engineering"
            ],

            "Construction and Design":

            [
            "Diploma in Architecture",
            "Diploma in Civil Engineering",
            "Diploma in Interior Design"
            ],

            "Hospitality and Event Management":

            [
            "Diploma in Hotel Management",
            "Diploma in Event Management",
            "Diploma in Aviation and Hospitality Management"
            ],

            "Life Sciences and Environment":
            [
            "Diploma in Biotechnology",
            "Diploma in Environmental Science",
            "Diploma in Veterinary Science"
            ],
            
            "Arts and Media":
            [
            "Diploma in Animation and Multimedia",
            "Diploma in Film Making and Direction",
            "Diploma in Photography"
            ],

            "Physical Education and Wellness":
            [
            "Diploma in Early Childhood Education",
            "Diploma in Yoga and Wellness"
            ],

            "Finance, Business and Marketing":
            [
            "Diploma in Financial Accounting"
            ]

            }



        self.iti = {
            "Computer Science and Information Technology ":

            [
            "ITI in Computer Hardware and Networking",
            "ITI in Information Technology",
            "ITI in Mobile Repair and Maintenance"
            ],

            "Mechanical and Electrical":
            [
             "ITI in Mechanical",
            "ITI in Automotive Technology",
            "ITI in Welding and Fabrication",
            " ITI in Fitter and Turner",
            "ITI in Machinist",
            "ITI in Foundry and Pattern Making",
            "ITI in CNC Operator"
            ],

            "Electronics and Communication":
            [
            "ITI in Electronics and Communication",
            "ITI in Instrumentation and Control",
            ],

            "Construction and Design":
            [
            "ITI in Plumbing and Pipefitting",
            "ITI in Carpentry and Woodworking"
            ],
            
            "Physical Education and Wellness":
            [
            "ITI in Beauty and Wellness"
            ]

            }
            


        self.vocational = {"Computer Science and Information Technology ":

            [
            "Vocational Training in Data Entry and Office Automation",
            "Vocational Training in Computer Programming",
            "Vocational Training in Mobile App Development",
            "Vocational Training in Web Development",
            "Vocational Training in Computer Hardware and Networking",
            "Vocational Training in Mobile Phone Repair Technician"
            ],

            "Mechanical and Electrical":
            [
            "Vocational Training in Welding Technician",
            "Vocational Training in Automotive Technician",
            "Vocational Training in Electrician",
            "Vocational Training in AutoCAD and Drafting Certification",
            "Vocational Training in Robotics and Automation Workshop",
            "Vocational Training in Machinist and CNC Operator",
            " Vocational Training in HVAC Technician"
            ],
            
            "Construction and Design":
            [
            "Vocational Training in Welding Technician",
            "Vocational Training in Plumbing and Pipefitting",
            "Vocational Training in Carpentry and Woodworking"
            ],

            "Hospitality and Event Management":
            [
            "Vocational Training in Hospitality and Customer Service",
            "Vocational Training in Healthcare Assistant Training",
            "Vocational Training in Basic First Aid and Safety Training",
            "Vocational Training in Retail Sales and Customer Service"
            ],

            "Arts and Media":
            [
            "Vocational Training in Graphic design Essentials",
            "Vocational Training in Digital Marketing Certification",
            "Vocational Training in Photography and Videography Course",
            "Vocational Training in Fashion Design and Tailoring",
            "Vocational Training in Language Proficiency Course"
            ],
            
            "Physical Education and Wellness":
            [
            "Vocational Training in Beauty and Makeup Artistry"
            ],

            "Finance, Business and Marketing":
            [
            "Vocational Training in Digital Marketing Certification",
            "Vocational Training in Entrepreneurship and Business Skills"
            ],

            "Culinary Studies and Cooking":
            [
            "Vocational Training in Culinary arts and Cooking",
            "Vocational Training in Baking and Pastry Arts",
            "Vocational Training in Food Safety and Hygiene Certification"
            ]
                 }
        
        self.ITIReq = {"Computer Science and Information Technology":[60,70,70,65,70],
          "Mechanical and Electrical":[60,70,70,65,65],
          "Electronics and Communication":[60,65,65,65,65],
          "Construction and Design":[55,60,55,60,55],
          "Physical Education and Wellness":[55,55,55,55,55]}
        self.DiplomaReq = {"Computer Science and Information and technology":[75,80,80,75,80,85] ,
              "Mechanical and Electrical":[75,85,80,75,80,80],
              "Electronics and Communication":[75,80,80,75,80,85],
              "Construction and Design":[75,80,75,80,85,80],
              "Hospitality and Event Management":[85,80,75,80,80,80],
              "Life Sciences and Environment":[80,80,85,75,80,75],
              "Arts and Media":[85,75,80,80,80,80],
              "Physical Education and Wellness":[80,75,85,75,80,80],
              "Finance, Business and Marketing":[80,80,75,75,85,80]}
        education_stylesheet = """
            QWidget {
                background-color: #FDDC5C; 
                color: #333333; 
            }
            QLabel {
                font-family: MS Shell Dlg 2;
                font-size: 14px;
                font-weight: bold;
                color: #000000;
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
        self.LoginMsgLbl.setText(_translate("MenuWindow", "Enter your required details:"))
        self.EnterButton.setText(_translate("MenuWindow", "Enter"))
        self.TakeTestButton.setText(_translate("MenuWindow", "Take Test"))
        self.GenerateReportButton.setText(_translate("MenuWindow", "Generate Report"))

    def fetchsubjects(self):
        user_id = self.User_id
        statement = f"SELECT English, Mathematics, Social_Studies, Science, Computer, Interests, counter from User_Marks WHERE User_id='{user_id}';"
        try:
            self.cur.execute(statement)
            result = self.cur.fetchone()
            if result:
                english, mathematics, social_studies, science, computer, interests, counter = result
            else:
                english, mathematics, social_studies, science, computer, interests, counter = 0, 0, 0, 0, 0, "Select", 0
            return english, mathematics, social_studies, science, computer, interests, counter
        except sqlite3.Error as e:
            error_message = f"Database error: {e}"
            QMessageBox.critical(None, "Error", error_message, QMessageBox.Ok)
            return 0, 0, 0, 0, 0, "Select", 0
        
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
        english, mathematics, social_studies, science, computer, interests, counter = self.fetchsubjects()
        self.ui.EnglishLineEdit.setText(f"{english}")
        self.ui.MathsLineEdit.setText(f"{mathematics}")
        self.ui.SstLineEdit.setText(f"{social_studies}")
        self.ui.ScienceLineEdit.setText(f"{science}")
        self.ui.ComputerLineEdit.setText(f"{computer}")
        self.ui.InterestsCB.setCurrentText(f"{interests}")
        self.ui.counter = counter
        self.window.show()
        MenuWindow.hide()

    def ChooseSub(self, MenuWindow):
        from Choose_Subject import Ui_SubjectWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SubjectWindow()
        self.ui.User_id = self.User_id
        self.ui.setupUi(self.window)
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
        if branch == 1:
            weaksubs = self.CheckRequirementsITI(interests,ITIsubs)
        self.GenReport(MenuWindow, recommend, courses, branch, weaksubs)
        
    
    def Gencourses(self):
        english, mathematics, science, social_studies, logical_reasoning, computer, interests = self.fetchallsubjects()
        avg = (english+mathematics+science+social_studies+logical_reasoning+computer)/6*100
        if avg>=75:
            branch = 0
        elif avg>=55:
            branch = 1
        else:
            branch = 2
        recommend = Printpred(english, mathematics, science, social_studies, logical_reasoning, computer, branch)
        courses = []
        if branch == 0:
            if recommend == "Computer Science and Information Technology":
                for i in self.diploma['Computer Science and Information Technology']:
                    courses.append(i)
            elif recommend == "Mechanical and Electrical":
                for i in self.diploma['Mechanical and Electrical']:
                    courses.append(i)
            elif recommend == "Electronics and Communication":
                for i in self.diploma['Electronics and Communication']:
                    courses.append(i)
            elif recommend == "Construction and Design":
                for i in self.diploma['Construction and Design']:
                    courses.append(i)
            elif recommend == "Hospitality and Event Management":
                for i in self.diploma['Hospitality and Event Management']:
                    courses.append(i)
            elif recommend == "Life Sciences and Environment":
                for i in self.diploma['Life Sciences and Environment']:
                    courses.append(i)
            elif recommend == "Arts and Media":
                for i in self.diploma['Arts and Media']:
                    courses.append(i)
            elif recommend == "Physical Education and Wellness":
                for i in self.diploma['Physical Education and Wellness']:
                    courses.append(i)
            elif recommend == "Finance, Business and Marketing":
                for i in self.diploma['Finance, Business and Marketing']:
                    courses.append(i)

        elif branch == 1:
            if recommend == "Computer Science and Information Technology":
                for i in self.iti['Computer Science and Information Technology']:
                    courses.append(i)
            elif recommend == "Mechanical and Electrical":
                for i in self.iti['Mechanical and Electrical']:
                    courses.append(i)
            elif recommend == "Electronics and Communication":
                for i in self.iti['Electronics and Communication']:
                    courses.append(i)
            elif recommend == "Construction and Design":
                for i in self.iti['Construction and Design']:
                    courses.append(i)
            elif recommend == "Physical Education and Wellness":
                for i in self.iti['Physical Education and Wellness']:
                    courses.append(i)

        else:
            if recommend == "Computer Science and Information Technology":
                for i in self.vocational['Computer Science and Information Technology']:
                    courses.append(i)
            elif recommend == "Mechanical and Electrical":
                for i in self.vocational['Mechanical and Electrical']:
                    courses.append(i)
            elif recommend == "Construction and Design":
                for i in self.vocational['Construction and Design']:
                    courses.append(i)
            elif recommend == "Hospitality and Event Management":
                for i in self.vocational['Hospitality and Event Management']:
                    courses.append(i)
            elif recommend == "Arts and Media":
                for i in self.vocational['Arts and Media']:
                    courses.append(i)
            elif recommend == "Physical Education and Wellness":
                for i in self.vocational['Physical Education and Wellness']:
                    courses.append(i)
            elif recommend == "Finance, Business and Marketing":
                for i in self.vocational['Finance, Business and Marketing']:
                    courses.append(i)
            elif recommend == "Culinary Studies and Cooking":
                for i in self.vocational['Culinary Studies and Cooking']:
                    courses.append(i)
                    
        return str(recommend), courses, branch

    def CheckRequirementsITI(self,interest,subs):
        weaksubs = []
        for i in range(5):
            if self.ITIreq[interest][i] > subs[i]:
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
        for i in range(len(courses)):
            self.ui.RecomCB.setItemText(i+1,f"{courses[i]}")
        for i in range(len(weaksubs)):
            temp = "\n".join(weaksubs)
        self.ui.WeakLbl.setText(temp)
        self.ui.Branch = branch
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
