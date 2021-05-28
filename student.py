# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from confirm_page import Ui_confirmpage
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 882)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 220, 251, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 270, 431, 501))
        self.listWidget.setObjectName("listWidget")
        self.name_last_label = QtWidgets.QLabel(self.centralwidget)
        self.name_last_label.setGeometry(QtCore.QRect(230, 120, 161, 31))
        self.name_last_label.setObjectName("name_last_label")
        self.id_phone_label = QtWidgets.QLabel(self.centralwidget)
        self.id_phone_label.setGeometry(QtCore.QRect(230, 52, 161, 31))
        self.id_phone_label.setObjectName("id_phone_label")
        self.name_last_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_last_line.setGeometry(QtCore.QRect(410, 118, 561, 41))
        self.name_last_line.setObjectName("name_last_line")
        self.id_phone_line = QtWidgets.QLineEdit(self.centralwidget)
        self.id_phone_line.setGeometry(QtCore.QRect(410, 50, 561, 41))
        self.id_phone_line.setObjectName("id_phone_line")
        self.order_button = QtWidgets.QPushButton(self.centralwidget)
        self.order_button.setGeometry(QtCore.QRect(560, 340, 381, 141))
        self.order_button.setObjectName("order_button")
        self.plate_button = QtWidgets.QPushButton(self.centralwidget)
        self.plate_button.setGeometry(QtCore.QRect(550, 550, 381, 141))
        self.plate_button.setObjectName("plate_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 44))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.check_func()
        self.order_button.clicked.connect(self.order_func)
        self.plate_button.clicked.connect(lambda :self.my_plate(self.id_phone_line.text()))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def my_plate(self,X=None):
        # create or open
        conn = sqlite3.connect("my_plate.db")
        # create a cursor
        c = conn.cursor()

        c.execute(F"""SELECT * FROM student_info WHERE my_id={X}""")
        results = c.fetchall()
        # commit changes
        conn.commit()
        # close the connec
        conn.close()
        print(results)
        self.w = QWidget()
        self.w.resize(510, 210)

        self.tw = QTreeWidget(self.w)
        self.tw.resize(500, 200)
        self.tw.setColumnCount(3)
        self.tw.setHeaderLabels(["id", "name", "food"])
        for result in results:
            self.l1 = QTreeWidgetItem([f"{result[1]}", f"{result[2]}", f"{result[3]}"])

            self.tw.addTopLevelItem(self.l1)

            self.tw.setColumnCount(3)
        self.w.show()


    def order_func(self):
        # create or open
        conn = sqlite3.connect("housewife.db")
        # create a cursor
        c = conn.cursor()
        # Operation
        c.execute("""SELECT * FROM housewife_info""")
        results=c.fetchall()
        # commit changes
        conn.commit()
        # close the connection
        conn.close()
        plain=self.listWidget.currentItem().text()
        list_plain=plain.split(",")


        for i in results:

             if list_plain[0] ==i[3]:
                 food_id=i[0]


        self.confirmpage = QtWidgets.QMainWindow()
        self.ui = Ui_confirmpage()
        self.ui.setupUi(self.confirmpage,food_id,self.id_phone_line.text(),self.name_last_line.text())
        #self.ui.setupUi(self.confirmpage)
        self.confirmpage.show()
    def check_func(self):

        # create or open
        conn = sqlite3.connect("housewife.db")
        # create a cursor
        c = conn.cursor()
        # Operation
        c.execute("""SELECT * FROM housewife_info""")
        results=c.fetchall()
        # commit changes
        conn.commit()
        # close the connection
        conn.close()
        for result in results:
            self.listWidget.addItem(f"{result[3]},        {result[5]}")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student"))
        self.label.setText(_translate("MainWindow", "Dishes"))
        self.name_last_label.setText(_translate("MainWindow", "Name/Last"))
        self.id_phone_label.setText(_translate("MainWindow", "ID/Phone No"))
        self.order_button.setText(_translate("MainWindow", "Order"))
        self.plate_button.setText(_translate("MainWindow", "MY Plate"))

