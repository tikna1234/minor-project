# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tips_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TipsWindow(object):
    def setupUi(self, TipsWindow):
        TipsWindow.setObjectName("TipsWindow")
        TipsWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TipsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 751, 511))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        TipsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TipsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        TipsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TipsWindow)
        self.statusbar.setObjectName("statusbar")
        TipsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TipsWindow)
        QtCore.QMetaObject.connectSlotsByName(TipsWindow)

    def retranslateUi(self, TipsWindow):
        _translate = QtCore.QCoreApplication.translate
        TipsWindow.setWindowTitle(_translate("TipsWindow", "Tips_Page"))
        self.label.setText(_translate("TipsWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TipsWindow = QtWidgets.QMainWindow()
    ui = Ui_TipsWindow()
    ui.setupUi(TipsWindow)
    TipsWindow.show()
    sys.exit(app.exec_())