# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'take test all other questions.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random as rndm
import pandas as pd
import numpy as np
import sqlite3
import os

def find_file_path(file_name):
    for root, dirs, files in os.walk(os.path.abspath(os.sep)):
        if file_name in files:
            return os.path.join(root, file_name)

    return f"File '{file_name}' not found in the current directory "

con = sqlite3.connect(find_file_path('Career_Recommedation_System.db'))
class Ui_TakeTestWindow(object):
    def setupUi(self, TakeTestWindow):
        education_stylesheet = """
            QWidget {
                background-color: #C32148; 
                color: white; 
            }
            QLabel {
                font-family: MS Shell Dlg 2;
                font-size: 14px;
                color: white; 
            }
            QRadioButton {
                background-color: #C32148; 
                color: white; 
            }
            QPushButton {
                background-color: #4CAF50; 
                color: #FFFFFF; 
            }
            QPushButton:hover {
                background-color: #6495ED; 
            }
            
        """
        TakeTestWindow.setStyleSheet(education_stylesheet)
        self.cur = con.cursor()
        self.User_id = ""
        self.marks = 0
        self.finished = False
        self.ans = []
        self.selected_answer = ""
        self.count = 0
        self.English = []
        self.Mathematics = []
        self.Social_Studies = []
        self.Science = []
        self.Logical_Reasoning = []
        self.Computer = []
        font = QtGui.QFont()
        font.setFamily("Noto Sans") 
        font.setPointSize(9)
        TakeTestWindow.setObjectName("TakeTestWindow")
        TakeTestWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TakeTestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Option2Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Option2Button.setGeometry(QtCore.QRect(40, 230, 731, 31))
        self.Option2Button.setObjectName("Option2Button")
        self.AnswerbuttonGroup = QtWidgets.QButtonGroup(TakeTestWindow)
        self.AnswerbuttonGroup.setObjectName("AnswerbuttonGroup")
        self.AnswerbuttonGroup.addButton(self.Option2Button)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 781, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.Option4Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Option4Button.setGeometry(QtCore.QRect(40, 330, 741, 31))
        self.Option4Button.setObjectName("Option4Button")
        self.AnswerbuttonGroup.addButton(self.Option4Button)
        self.Option1Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Option1Button.setGeometry(QtCore.QRect(40, 180, 721, 31))
        self.Option1Button.setObjectName("Option1Button")
        self.AnswerbuttonGroup.addButton(self.Option1Button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setGeometry(QtCore.QRect(620, 460, 93, 28))
        self.NextButton.setObjectName("NextButton")
        self.NextButton.clicked.connect(lambda: self.nextButtonClicked(TakeTestWindow))
        self.Option3Button = QtWidgets.QRadioButton(self.centralwidget)
        self.Option3Button.setGeometry(QtCore.QRect(40, 280, 741, 31))
        self.Option3Button.setObjectName("Option3Button")
        self.AnswerbuttonGroup.addButton(self.Option3Button)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(80, 460, 93, 28))
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(lambda: self.back_button_clicked(TakeTestWindow))
        TakeTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TakeTestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TakeTestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TakeTestWindow)
        self.statusbar.setObjectName("statusbar")
        TakeTestWindow.setStatusBar(self.statusbar)
        self.Option2Button.setFont(font)
        self.label_2.setFont(font)
        self.Option4Button.setFont(font)
        self.Option1Button.setFont(font)
        self.label.setFont(font)
        self.NextButton.setFont(font)
        self.Option3Button.setFont(font)
        self.BackButton.setFont(font)
        self.retranslateUi(TakeTestWindow)
        QtCore.QMetaObject.connectSlotsByName(TakeTestWindow)

    def retranslateUi(self, TakeTestWindow):
        _translate = QtCore.QCoreApplication.translate
        TakeTestWindow.setWindowTitle(_translate("TakeTestWindow", "Test_Page"))
        self.Option2Button.setText(_translate("TakeTestWindow", "Option2"))
        self.label_2.setText(_translate("TakeTestWindow", "Question"))
        self.Option4Button.setText(_translate("TakeTestWindow", "Option4"))
        self.Option1Button.setText(_translate("TakeTestWindow", "Option1"))
        self.label.setText(_translate("TakeTestWindow", "Question NO. 0"))
        self.NextButton.setText(_translate("TakeTestWindow", "Next"))
        self.Option3Button.setText(_translate("TakeTestWindow", "Option3"))
        self.BackButton.setText(_translate("TakeTestWindow", "Back"))

    def back_button_clicked(self, TakeTestWindow):
        if self.count > 1:
            self.marks -= 4
            self.count -= 2
            self.RenderQ(self.count)
        if self.count == 1:
            self.backtomenu(TakeTestWindow)

    def backtomenu(self, TakeTestWindow):
        from menu_page import Ui_MenuWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.window.show()
        TakeTestWindow.hide()    

    def get_question_data(self, data, subject_list, count):
        question = data.iloc[subject_list[count], 0]
        a = data.iloc[subject_list[count], 1]
        b = data.iloc[subject_list[count], 2]
        c = data.iloc[subject_list[count], 3]
        d = data.iloc[subject_list[count], 4]
        return question, a, b, c, d

    def get_selected_answer(self):
        if self.Option1Button.isChecked():
            return "A"
        elif self.Option2Button.isChecked():
            return "B"
        elif self.Option3Button.isChecked():
            return "C"
        elif self.Option4Button.isChecked():
            return "D"
        else:
            return ""
        
    def checkAns(self):
        if self.selected_answer == self.ans[self.count - 1]:
            self.marks += 4
        elif self.selected_answer == "":
            pass
        self.marks = min(self.marks, 100)
        
    def nextButtonClicked(self, TakeTestWindow):
        if not self.finished:
            self.NextButton.setEnabled(False)
            self.reset_selection()
            self.selected_answer = self.get_selected_answer()
            self.checkAns()
            self.RenderQ(self.count)
        else:
            self.finish(TakeTestWindow)
        
    def RenderQ(self, count):
        english_file = find_file_path('english_questions.xlsx')
        mathematics_file = find_file_path('Mathematics_questions.xlsx')
        social_studies_file = find_file_path('Social_Studies_questions.xlsx')
        science_file = find_file_path('Science_questions.xlsx')
        logical_reasoning_file = find_file_path('Logical_Reasoning_questions.xlsx')
        computer_file = find_file_path('Computer_questions.xlsx')
        data = None
        question, a, b, c, d = "", "", "", "", ""
        if len(self.English) > 0:
            data = pd.read_excel(english_file)
            question, a, b, c, d = self.get_question_data(data, self.English, count)
        elif len(self.Mathematics) > 0:
            data = pd.read_excel(mathematics_file)
            question, a, b, c, d = self.get_question_data(data, self.Mathematics, count)
        elif len(self.Social_Studies) > 0:
            data = pd.read_excel(social_studies_file)
            question, a, b, c, d = self.get_question_data(data, self.Social_Studies, count)
        elif len(self.Science) > 0:
            data = pd.read_excel(science_file)
            question, a, b, c, d = self.get_question_data(data, self.Science, count)
        elif len(self.Logical_Reasoning) > 0:
            data = pd.read_excel(logical_reasoning_file)
            question, a, b, c, d = self.get_question_data(data, self.Logical_Reasoning, count)
        elif len(self.Computer) > 0:
            data = pd.read_excel(computer_file)
            question, a, b, c, d = self.get_question_data(data, self.Computer, count)
        else: self.label_2.setText("error")
        if data is not None:
            self.count += 1
            self.label.setText(f"Question NO. {self.count}")
            self.label_2.setText(question)
            self.Option1Button.setText(str(a))
            self.Option2Button.setText(str(b))
            self.Option3Button.setText(str(c))
            self.Option4Button.setText(str(d))
        else:
            self.label_2.setText("error")
        self.NextButton.setEnabled(True)
        if self.count >= 25:
            self.finished = True
            self.NextButton.setText("Finish")

    def fetchpreviousmarks(self):
        if len(self.English) > 0:
            try:
                statement= f"SELECT English from User_marks WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                previousmarks = self.cur.fetchone()
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Mathematics) > 0:
            try:
                statement= f"SELECT Mathematics from User_marks WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                previousmarks = self.cur.fetchone()
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Social_Studies) > 0:
            try:
                statement= f"SELECT Social_Studies from User_marks WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                previousmarks = self.cur.fetchone()
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Science) > 0:
            try:
                statement= f"SELECT Science from User_marks WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                previousmarks = self.cur.fetchone()
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Logical_Reasoning) > 0:
            try:
                statement= f"SELECT Logical_Reasoning from User_marks WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                previousmarks = self.cur.fetchone()
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Computer) > 0:
            try:
                statement= f"SELECT Computer from User_marks WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                previousmarks = self.cur.fetchone()
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        else: self.label_2.setText("error")
        return previousmarks

    def addmarkstodatabase(self):
        if len(self.English) > 0:
            try:
                statement= f"UPDATE User_Marks SET English = {self.marks}  WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Mathematics) > 0:
            try:
                statement= f"UPDATE User_Marks SET Mathematics = {self.marks}  WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Social_Studies) > 0:
            try:
                statement= f"UPDATE User_Marks SET Social_Studies = {self.marks} WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Science) > 0:
            try:
                statement= f"UPDATE User_Marks SET Science = {self.marks}  WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Logical_Reasoning) > 0:
            try:
                statement= f"UPDATE User_Marks SET Logical_Reasoning = {self.marks}  WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        elif len(self.Computer) > 0:
            try:
                statement= f"UPDATE User_Marks SET Computer = {self.marks}  WHERE User_id = '{self.User_id}'"
                self.cur.execute(statement)
                con.commit()
            except sqlite3.Error as e:
                self.label.setText(f"SQLite error: {e}")
        else: self.label_2.setText("error")
        
    def reset_selection(self):
        self.AnswerbuttonGroup.setExclusive(False)
        for button in self.AnswerbuttonGroup.buttons():
            button.setChecked(False)
        self.AnswerbuttonGroup.setExclusive(True)

    def finish(self, TakeTestWindow):
        from Results import Ui_ResultWindow
        result=self.marks
        previousmarks = self.fetchpreviousmarks()
        previousmarks = int(''.join(map(str,previousmarks)))
        if previousmarks < result :
            self.addmarkstodatabase()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        if len(self.English) > 0:
            self.ui.EngMarksLbl.setText(f"{result}")
        elif len(self.Mathematics) > 0:
            self.ui.MathMarksLbl.setText(f"{result}")
        elif len(self.Social_Studies) > 0:
            self.ui.SstMarksLbl.setText(f"{result}")
        elif len(self.Science) > 0:
            self.ui.SciLbl.setText(f"{result}")
        elif len(self.Logical_Reasoning) > 0:
            self.ui.LgRnLbl.setText(f"{result}")
        elif len(self.Computer) > 0:
            self.ui.CompLbl.setText(f"{result}")
        else: self.label_2.setText("error")
        self.window.show()
        TakeTestWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TakeTestWindow = QtWidgets.QMainWindow()
    ui = Ui_TakeTestWindow()
    ui.setupUi(TakeTestWindow)
    TakeTestWindow.show()
    sys.exit(app.exec_())
