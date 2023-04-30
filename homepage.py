# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aksh\Downloads\homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.resize(300, 533)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HomePage.sizePolicy().hasHeightForWidth())
        HomePage.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(HomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 140, 300, 340))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.medicineSchedule = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.medicineSchedule.sizePolicy().hasHeightForWidth())
        self.medicineSchedule.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.medicineSchedule.setFont(font)
        self.medicineSchedule.setStyleSheet("border-radius:15px ;border:1px solid rgb(135,206,235); background-color:rgb(135,206,235);padding-top:6%;padding-bottom:6%;padding-left:6%;padding-right:6%;")
        self.medicineSchedule.setObjectName("medicineSchedule")
        self.horizontalLayout.addWidget(self.medicineSchedule)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:15px ;border:1px solid rgb(135,206,235); background-color:rgb(135,206,235);padding-top:6%;padding-bottom:6%;padding-left:6%;padding-right:6%;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:15px ;border:1px solid rgb(135,206,235); background-color:rgb(135,206,235);padding-top:6%;padding-bottom:6%;padding-left:6%;padding-right:6%;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:15px ;border:1px solid rgb(135,206,235); background-color:rgb(135,206,235);padding-top:6%;padding-bottom:6%;padding-left:6%;padding-right:6%;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        HomePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow"))
        self.label.setText(_translate("HomePage", "Welcome!"))
        self.medicineSchedule.setText(_translate("HomePage", "Medicine Schedule"))
        self.pushButton.setText(_translate("HomePage", "Status Update"))
        self.pushButton_2.setText(_translate("HomePage", "Checklist"))
        self.pushButton_3.setText(_translate("HomePage", "Contacts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomePage = QtWidgets.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.show()
    sys.exit(app.exec_())
