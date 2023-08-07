# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):

    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        self.breakdown = ""
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.breakdownButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.breakdownBox.setText(self.breakdown))
        self.breakdownButton.setGeometry(QtCore.QRect(1053, 30, 500, 70))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.breakdownButton.setFont(font)
        self.breakdownButton.setObjectName("breakdownButton")

        self.breakdownHideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.breakdownBox.setText(""))
        self.breakdownHideButton.setGeometry(QtCore.QRect(1053, 760, 500, 70))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.breakdownHideButton.setFont(font)
        self.breakdownHideButton.setObjectName("breakdownHideButton")

        self.breakdownBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.breakdownBox.setGeometry(QtCore.QRect(1053, 130, 500, 700))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.breakdownBox.setFont(font)
        self.breakdownBox.setObjectName("breakdownBox")
        self.allergyBox = QtWidgets.QTextEdit(self.centralwidget)
        self.allergyBox.setGeometry(QtCore.QRect(353, 130, 500, 700))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.allergyBox.setFont(font)
        self.allergyBox.setObjectName("allergyBox")
        self.allergyHeader = QtWidgets.QLabel(self.centralwidget)
        self.allergyHeader.setGeometry(QtCore.QRect(353, 30, 350, 70))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.allergyHeader.setFont(font)
        self.allergyHeader.setObjectName("allergyHeader")
        self.label_close = QtWidgets.QLabel(self.centralwidget)
        self.label_close.setGeometry(QtCore.QRect(699, 900, 508, 70))
        self.label_close.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()    
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label_close.setFont(font)
        self.label_close.setObjectName("label_close")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.allergyHeader.setText(_translate("SecondWindow", "Possible Allergies"))
        self.breakdownButton.setText(_translate("SecondWindow", "View Breakdown"))
        self.breakdownHideButton.setText(_translate("SecondWindow", "Hide Breakdown"))
        self.label_close.setText(_translate("MainWindow", "Please close window when finished."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())