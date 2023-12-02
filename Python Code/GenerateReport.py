# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateReport.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportWindow(object):
    def setupUi(self, ReportWindow):
        education_stylesheet = """
            QWidget {
                background-color: #C32148; 
                color: white; 
            }
            QLabel {
                font-family: MS Shell Dlg 2;
                font-size: 18px;
                color: white; 
            }
            QLabel#recomjob {
                font-family: MS Shell Dlg 2;
                font-size: 18px;
                color: black; 
            }
            QLabel#WeakLbl {
                font-family: MS Shell Dlg 2;
                font-size: 18px;
                color: black; 
            }
            QLineEdit{
                background-color: #FFFFFF; 
                color: #000000; 
                border: 1px solid #CCCCCC; 
            }
            QComboBox {
                background-color: #FFFFFF; 
                color: #000000; 
                border: 1px solid #CCCCCC; 
            }
            QComboBox QAbstractItemView {
                background-color: #FFFFFF; 
                color: #000000; 
                border: 1px solid #CCCCCC; 
            }
            QComboBox QAbstractItemView::up-arrow, QComboBox QAbstractItemView::down-arrow {
                background-color: #FFFFFF; 
            }
            QComboBox QScrollBar:vertical {
                background-color: #FFFFFF; 
            }
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
            }
            
        """
        ReportWindow.setStyleSheet(education_stylesheet)
        self.sites={"English":["British Council: Offers online courses, study materials, and resources to improve English skills.","Grammarly: Provides grammar tips, exercises, and writing enhancement tools.","BBC Learning English: Offers resources for improving English language skills."],
               "Mathematics":["NCERT Official Website: Provides textbooks and resources aligned with the curriculum.","Khan Academy: Offers video tutorials and practice exercises covering various math topics.","Cuemath: Provides math resources and practice material for students."],
               "Science":["National Science Digital Library (NSDL): Offers a wide range of educational resources related to science.","TopperLearning: Provides study materials, video lessons, and practice tests for science subjects.","Embibe: Offers study materials, practice questions, and tests for science subjects."],
               "Social_Studies":["NCERT Official Website: Provides textbooks and resources for social studies subjects.","BYJU'S: Offers study materials, videos, and interactive content for social studies.","Meritnation: Provides study materials and resources for social studies subjects"],
               "Logical_Reasoning":["TCY Online: Offers practice tests and study material for logical reasoning.","Indiabix: Provides logical reasoning questions and solutions for practice.","Gradeup: Offers practice questions and quizzes for logical reasoning."],
               "Computer":["Codecademy: Offers coding tutorials and exercises for beginners.","Udemy: Provides various computer-related courses at different levels.","GeeksforGeeks: Offers coding challenges, articles, and tutorials related to computer science."]}
        self.ITI = {
            'ITI in Computer Hardware and Networking': [
                'Computer Hardware Technician',
                'Network Technician',
                'IT Support Technician',
                'Field Service Technician',
                'System Administrator'
            ],
            'ITI in Information Technology': [
                'IT Support Specialist',
                'Computer Operator',
                'Data Entry Operator',
                'IT Assistant',
                'Desktop Support Technician'
            ],
            'ITI in Mobile Repair and Maintenance': [
                'Mobile Phone Technician',
                'Cellphone Repair Technician',
                'Mobile Service Technician',
                'Mobile Hardware Specialist',
                'Cellphone Diagnostic Technician'
            ],
            'ITI in Mechanical': [
                'Mechanical Technician',
                'Machinist',
                'Maintenance Technician',
                'Production Assistant',
                'Quality Control Technician'
            ],
            'ITI in Automotive Technology': [
                'Automotive Technician',
                'Automotive Mechanic',
                'Auto Repair Technician',
                'Automobile Service Technician',
                'Automotive Electrician'
            ],
            'ITI in Welding and Fabrication': [
                'Welder',
                'Fabricator',
                'Welding Technician',
                'Structural Welder',
                'Metal Worker'
            ],
            'ITI in Fitter and Turner': [
                'Fitter',
                'Turner',
                'Assembly Technician',
                'Machinist',
                'Machine Operator'
            ],
            'ITI in Machinist': [
                'Machinist',
                'CNC Machinist',
                'Tool and Die Maker',
                'Machining Technician',
                'Lathe Operator'
            ],
            'ITI in Foundry and Pattern Making': [
                'Foundry Technician',
                'Pattern Maker',
                'Metal Casting Technician',
                'Foundry Worker',
                'Molder'
            ],
            'ITI in CNC Operator': [
                'CNC Machine Operator',
                'CNC Programmer',
                'Machine Shop Operator',
                'CNC Technician',
                'CNC Machinist'
            ],
            'ITI in Electronics and Communication': [
                'Electronics Technician',
                'Communication Technician',
                'Electronics Assembler',
                'PCB Designer',
                'Electronics Repair Technician'
            ],
            'ITI in Instrumentation and Control': [
                'Instrumentation Technician',
                'Control Systems Technician',
                'Instrumentation and Control Engineer',
                'Calibration Technician',
                'Process Control Technician'
            ],
            'ITI in Plumbing and Pipefitting': [
                'Plumber',
                'Pipefitter',
                'Plumbing Technician',
                'Pipe Welder',
                'Gas Fitter'
            ],
            'ITI in Carpentry and Woodworking': [
                'Carpenter',
                'Woodworker',
                'Cabinet Maker',
                'Furniture Designer',
                'Joinery Technician'
            ],
            'ITI in Beauty and Wellness': [
                'Beautician',
                'Hair Stylist',
                'Makeup Artist',
                'Spa Therapist',
                'Skin Care Specialist'
            ]
        }
        self.Diploma = {
            'Diploma in Computer Science': [
                'Software Developer',
                'Network Administrator',
                'Database Administrator',
                'Web Developer',
                'Systems Analyst',
                'IT Support Specialist',
                'Cybersecurity Analyst'
            ],
            'Diploma in Digital Marketing': [
                'Digital Marketing Specialist',
                'Social Media Manager',
                'SEO Specialist',
                'Content Marketing Manager',
                'Email Marketing Specialist',
                'PPC Specialist'
            ],
            'Diploma in Mobile App Development': [
                'Mobile App Developer',
                'App Tester',
                'App Designer',
                'UI/UX Designer',
                'Mobile App Support Technician'
            ],
            'Diploma in Cybersecurity': [
                'Cybersecurity Analyst',
                'Security Consultant',
                'Incident Responder',
                'Security Engineer',
                'Penetration Tester'
            ],
            'Diploma in Web Development': [
                'Web Developer',
                'Front-End Developer',
                'Back-End Developer',
                'UI/UX Designer',
                'Web Content Manager'
            ],
            'Diploma in Mechanical Engineering': [
                'Mechanical Engineer',
                'Maintenance Technician',
                'CAD Technician',
                'Quality Control Technician',
                'Production Supervisor'
            ],
            'Diploma in Civil Engineering': [
                'Civil Engineer',
                'Construction Supervisor',
                'Surveyor',
                'CAD Technician',
                'Site Engineer'
            ],
            'Diploma in Electrical Engineering': [
                'Electrical Engineer',
                'Electrician',
                'Electrical Technician',
                'Control Panel Designer',
                'Power Plant Technician'
            ],
            'Diploma in Automobile Engineering': [
                'Automotive Engineer',
                'Automotive Technician',
                'Service Advisor',
                'Quality Control Engineer',
                'Automotive Designer'
            ],
            'Diploma in Chemical Engineering': [
                'Chemical Engineer',
                'Process Technician',
                'Quality Control Technician',
                'Laboratory Technician',
                'Production Supervisor'
            ],
            'Diploma in Electronics and Communication': [
                'Electronics Technician',
                'Telecommunication Technician',
                'Electronic Equipment Assembler',
                'Broadcast Technician',
                'Electronics Engineer'
            ],
            'Diploma in Architecture': [
                'Architectural Drafter',
                'Architectural Assistant',
                'Building Inspector',
                'CAD Technician',
                'Construction Supervisor'
            ],
            'Diploma in Interior Design': [
                'Interior Designer',
                'Interior Decorator',
                'Furniture Designer',
                'Retail Store Designer',
                'Set Designer'
            ],
            'Diploma in Hotel Management': [
                'Hotel Manager',
                'Front Office Executive',
                'Food and Beverage Manager',
                'Restaurant Manager',
                'Guest Relations Manager'
            ],
            'Diploma in Event Management': [
                'Event Planner',
                'Event Coordinator',
                'Wedding Planner',
                'Conference Manager',
                'Exhibition Organizer'
            ],
            'Diploma in Aviation and Hospitality Management': [
                'Airport Ground Staff',
                'Cabin Crew',
                'Airport Operations Manager',
                'Airline Customer Service Agent',
                'Hotel Front Desk Officer'
            ],
            'Diploma in Biotechnology': [
                'Laboratory Technician',
                'Biotechnician',
                'Research Assistant',
                'Quality Control Analyst',
                'Bioprocess Operator'
            ],
            'Diploma in Environmental Science': [
                'Environmental Technician',
                'Environmental Consultant',
                'Sustainability Specialist',
                'Water Quality Analyst',
                'Ecosystem Manager'
            ],
            'Diploma in Veterinary Science': [
                'Veterinary Assistant',
                'Animal Health Technician',
                'Veterinary Technician',
                'Pet Groomer',
                'Wildlife Rehabilitator'
            ],
            'Diploma in Animation and Multimedia': [
                'Animator',
                'Graphic Designer',
                'Video Editor',
                'Multimedia Artist',
                'Motion Graphics Designer'
            ],
            'Diploma in Film Making and Direction': [
                'Film Director',
                'Screenwriter',
                'Film Producer',
                'Cinematographer',
                'Film Editor'
            ],
            'Diploma in Photography': [
                'Photographer',
                'Photojournalist',
                'Photo Editor',
                'Studio Manager',
                'Photography Instructor'
            ],
            'Diploma in Early Childhood Education': [
                'Preschool Teacher',
                'Childcare Worker',
                'Early Childhood Educator',
                'Curriculum Developer',
                'Child Development Specialist'
            ],
            'Diploma in Yoga and Wellness': [
                'Yoga Instructor',
                'Wellness Coach',
                'Holistic Health Practitioner',
                'Fitness Trainer',
                'Meditation Instructor'
            ],
            'Diploma in Financial Accounting': [
                'Accounts Assistant',
                'Junior Accountant',
                'Bookkeeper',
                'Tax Assistant',
                'Audit Assistant'
            ]
        }
        self.Vocational = {
            'Vocational Training in Data Entry and Office Automation': [
                'Data Entry Operator',
                'Office Assistant',
                'Administrative Assistant'
            ],
            'Vocational Training in Computer Programming': [
                'Junior Programmer',
                'Software Developer',
                'Web Developer',
                'Application Developer'
            ],
            'Vocational Training in Mobile App Development': [
                'Mobile App Developer',
                'App Tester',
                'App Designer',
                'UI/UX Designer',
                'Mobile App Support Technician'
            ],
            'Vocational Training in Web Development': [
                'Web Developer',
                'Front-End Developer',
                'Back-End Developer',
                'UI/UX Designer',
                'Web Content Manager'
            ],
            'Vocational Training in Computer Hardware and Networking': [
                'IT Support Technician',
                'Network Technician',
                'Hardware Technician',
                'System Administrator',
                'Network Administrator'
            ],
            'Vocational Training in Mobile Phone Repair Technician': [
                'Mobile Phone Technician',
                'Cellphone Repair Technician',
                'Mobile Service Technician',
                'Mobile Hardware Specialist'
            ],
            'Vocational Training in Welding Technician': [
                'Welder',
                'Fabricator',
                'Welding Technician'
            ],
            'Vocational Training in Automotive Technician': [
                'Automotive Technician',
                'Automotive Mechanic',
                'Auto Repair Technician',
                'Automobile Service Technician',
                'Automotive Electrician'
            ],
            'Vocational Training in Electrician': [
                'Electrician',
                'Electrical Technician',
                'Control Panel Designer',
                'Power Plant Technician'
            ],
            'Vocational Training in AutoCAD and Drafting Certification': [
                'CAD Technician',
                'Draftsman',
                'Design Engineer'
            ],
            'Vocational Training in Robotics and Automation Workshop': [
                'Robotics Technician',
                'Automation Technician',
                'Robotics Programmer'
            ],
            'Vocational Training in Machinist and CNC Operator': [
                'Machinist',
                'CNC Machine Operator',
                'Machine Shop Operator'
            ],
            'Vocational Training in HVAC Technician': [
                'HVAC Technician',
                'Heating and Cooling Technician'
            ],
            'Vocational Training in Plumbing and Pipefitting': [
                'Plumber',
                'Pipefitter',
                'Pipe Welder',
                'Gas Fitter'
            ],
            'Vocational Training in Carpentry and Woodworking': [
                'Carpenter',
                'Woodworker',
                'Cabinet Maker',
                'Furniture Designer'
            ],
            'Vocational Training in Hospitality and Customer Service': [
                'Hotel Front Desk Officer',
                'Guest Service Agent',
                'Customer Service Representative'
            ],
            'Vocational Training in Healthcare Assistant Training': [
                'Healthcare Assistant',
                'Nursing Assistant'
            ],
            'Vocational Training in Basic First Aid and Safety Training': [
                'First Aid Responder',
                'Safety Officer'
            ],
            'Vocational Training in Retail Sales and Customer Service': [
                'Retail Sales Associate',
                'Customer Service Representative'
            ],
            'Vocational Training in Graphic Design Essentials': [
                'Graphic Designer',
                'Visual Designer'
            ],
            'Vocational Training in Digital Marketing Certification': [
                'Digital Marketing Specialist',
                'Social Media Manager',
                'SEO Specialist'
            ],
            'Vocational Training in Photography and Videography Course': [
                'Photographer',
                'Videographer',
                'Photo Editor'
            ],
            'Vocational Training in Fashion Design and Tailoring': [
                'Fashion Designer',
                'Tailor',
                'Clothing Designer'
            ],
            'Vocational Training in Language Proficiency Course': [
                'Translator',
                'Language Instructor'
            ],
            'Vocational Training in Beauty and Makeup Artistry': [
                'Makeup Artist',
                'Beauty Consultant'
            ],
            'Vocational Training in Entrepreneurship and Business Skills': [
                'Entrepreneur',
                'Small Business Owner',
                'Business Consultant'
            ],
            'Vocational Training in Culinary Arts and Cooking': [
                'Cook',
                'Chef',
                'Sous Chef'
            ],
            'Vocational Training in Baking and Pastry Arts': [
                'Baker',
                'Pastry Chef'
            ],
            'Vocational Training in Food Safety and Hygiene Certification': [
                'Food Safety Inspector',
                'Food Safety Coordinator'
            ]
        }
        self.Branch = 0
        self.User_id = ""
        self.weaksubs = []
        ReportWindow.setObjectName("ReportWindow")
        ReportWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(ReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.StrtMsgLbl = QtWidgets.QLabel(self.centralwidget)
        self.StrtMsgLbl.setGeometry(QtCore.QRect(30, 60, 351, 31))
        self.StrtMsgLbl.setObjectName("StrtMsgLbl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 500, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.recomjob = QtWidgets.QLabel(self.centralwidget)
        self.recomjob.setGeometry(QtCore.QRect(570, 280, 311, 191))
        self.recomjob.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.recomjob.setObjectName("recomjob")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 290, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.RecomCB = QtWidgets.QComboBox(self.centralwidget)
        self.RecomCB.setGeometry(QtCore.QRect(550, 200, 331, 22))
        self.RecomCB.setObjectName("RecomCB")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.addItem("")
        self.RecomCB.currentIndexChanged.connect(self.genjobs)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(360, 440, 93, 28))
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(lambda: self.backtomenu(ReportWindow))
        self.RecomendLbl = QtWidgets.QLabel(self.centralwidget)
        self.RecomendLbl.setGeometry(QtCore.QRect(20, 120, 720, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RecomendLbl.setFont(font)
        self.RecomendLbl.setObjectName("RecomendLbl")
        self.WeakButton = QtWidgets.QPushButton(self.centralwidget)
        self.WeakButton.setGeometry(QtCore.QRect(180, 430, 93, 28))
        self.WeakButton.setObjectName("WeakButton")
        self.WeakButton.clicked.connect(lambda: self.Tips_page(ReportWindow))
        self.WeakLbl = QtWidgets.QLabel(self.centralwidget)
        self.WeakLbl.setGeometry(QtCore.QRect(260, 290, 171, 101))
        self.WeakLbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WeakLbl.setObjectName("WeakLbl")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 160, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        ReportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReportWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 26))
        self.menubar.setObjectName("menubar")
        ReportWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReportWindow)
        self.statusbar.setObjectName("statusbar")
        ReportWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReportWindow)
        QtCore.QMetaObject.connectSlotsByName(ReportWindow)

    def retranslateUi(self, ReportWindow):
        _translate = QtCore.QCoreApplication.translate
        ReportWindow.setWindowTitle(_translate("ReportWindow", "Career Report"))
        self.label.setText(_translate("ReportWindow", "Career Report"))
        self.RecomCB.setItemText(0,"Select Your Course")
        self.StrtMsgLbl.setText(_translate("ReportWindow", "Dear, "))
        self.label_2.setText(_translate("ReportWindow", "We Recommend that you the following Courses:"))
        self.recomjob.setText(_translate("ReportWindow", "Job List"))
        self.label_5.setText(_translate("ReportWindow", "Jobs:"))
        self.label_3.setText(_translate("ReportWindow", "Look at your weakness:"))
        self.BackButton.setText(_translate("ReportWindow", "Back To Menu"))
        self.RecomendLbl.setText(_translate("ReportWindow", "You have been recommended, "))
        self.WeakButton.setText(_translate("ReportWindow", "Go!"))
        self.WeakLbl.setText(_translate("ReportWindow", "TextLabel"))
        self.label_4.setText(_translate("ReportWindow", "For tips look here:"))

    def genjobs(self):
        select = self.RecomCB.currentText()
        recommended_jobs = ""
        if self.Branch == 0:
            for j in self.Diploma.keys():
                if j == select:
                    recommended_jobs = "\n".join(self.Diploma[j])
        elif self.Branch == 1:
            for j in self.ITI.keys():
                if j == select:
                    recommended_jobs = "\n".join(self.ITI[j])
        elif self.Branch == 2:
            for j in self.Vocational.keys():
                if j == select:
                    recommended_jobs = "\n".join(self.Vocational[j])
        self.recomjob.setText(recommended_jobs)

    def backtomenu(self, ReportWindow):
        from menu_page import Ui_MenuWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.window.show()
        ReportWindow.hide()

    def GenTips_websites(self):
        for i in self.weaksubs:
            if i in self.sites.keys():
                self.sites[i]

    def Tips_page(self, ReportWindow):
        from Guide_page import Ui_GuideWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GuideWindow()
        self.ui.setupUi(self.window)
        self.ui.User_id = self.User_id
        self.window.show()
        ReportWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportWindow = QtWidgets.QMainWindow()
    ui = Ui_ReportWindow()
    ui.setupUi(ReportWindow)
    ReportWindow.show()
    sys.exit(app.exec_())
