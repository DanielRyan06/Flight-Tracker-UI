from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Flight_Info(object):
    def setupUi(self, Flight_Info):
        Flight_Info.setObjectName("Flight_Info")
        Flight_Info.resize(706, 560)
        Flight_Info.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Flight_Info.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.centralwidget = QtWidgets.QWidget(Flight_Info)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 631, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
"border-top-left-radius: 50px;\n"
"border-bottom-left-radius: 50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 311, 430))
        self.label_2.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 50, 271, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 30pt \"OCR A Extended\";\n"
"color:rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 190, 190, 40))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(134, 134, 134);\n"
"border-bottom-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(400, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(60, 79, 121), stop:1 rgb(98, 130, 199));\n"
"border-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"padding-right:5px;\n"
"padding-bottom: 5px;\n"
"background-color:rgb(134, 134, 134);;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(320, 380, 291, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(320, 410, 251, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(320, 400, 271, 16))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        Flight_Info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Flight_Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 21))
        self.menubar.setObjectName("menubar")
        Flight_Info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Flight_Info)
        self.statusbar.setObjectName("statusbar")
        Flight_Info.setStatusBar(self.statusbar)

        self.retranslateUi(Flight_Info)
        QtCore.QMetaObject.connectSlotsByName(Flight_Info)

    def retranslateUi(self, Flight_Info):
        _translate = QtCore.QCoreApplication.translate
        Flight_Info.setWindowTitle(_translate("Flight_Info", "MainWindow"))
        self.label_3.setText(_translate("Flight_Info", "Flight Info"))
        self.lineEdit.setPlaceholderText(_translate("Flight_Info", " Flight Number:"))
        self.pushButton.setText(_translate("Flight_Info", "Search Flight"))
        self.label_4.setText(_translate("Flight_Info", "Flight info, a project created by Daniel"))
        self.label_5.setText(_translate("Flight_Info", "aircraft currently flying."))
        self.label_6.setText(_translate("Flight_Info", "Ryan in August 2022 to pull data of an"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Flight_Info = QtWidgets.QMainWindow()
    ui = Ui_Flight_Info()
    ui.setupUi(Flight_Info)
    Flight_Info.show()
    sys.exit(app.exec_())
