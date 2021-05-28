
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 885)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 10, 901, 201))
        self.groupBox.setObjectName("groupBox")
        self.name_last_label = QtWidgets.QLabel(self.groupBox)
        self.name_last_label.setGeometry(QtCore.QRect(90, 110, 161, 31))
        self.name_last_label.setObjectName("name_last_label")
        self.name_last_line = QtWidgets.QLineEdit(self.groupBox)
        self.name_last_line.setGeometry(QtCore.QRect(270, 108, 561, 41))
        self.name_last_line.setObjectName("name_last_line")
        self.id_phone_line = QtWidgets.QLineEdit(self.groupBox)
        self.id_phone_line.setGeometry(QtCore.QRect(270, 40, 561, 41))
        self.id_phone_line.setObjectName("id_phone_line")
        self.id_phone_label = QtWidgets.QLabel(self.groupBox)
        self.id_phone_label.setGeometry(QtCore.QRect(90, 42, 161, 31))
        self.id_phone_label.setObjectName("id_phone_label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 210, 901, 601))
        self.groupBox_2.setObjectName("groupBox_2")
        self.indigirent_text = QtWidgets.QTextEdit(self.groupBox_2)
        self.indigirent_text.setGeometry(QtCore.QRect(10, 140, 541, 371))
        self.indigirent_text.setObjectName("indigirent_text")
        self.number_of_people_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.number_of_people_line.setGeometry(QtCore.QRect(570, 40, 271, 29))
        self.number_of_people_line.setObjectName("number_of_people_line")
        self.food_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.food_line.setGeometry(QtCore.QRect(570, 80, 271,29))
        self.food_line.setObjectName("food_line")
        self.publish_button = QtWidgets.QPushButton(self.groupBox_2)
        self.publish_button.setGeometry(QtCore.QRect(650, 320, 191, 71))
        self.publish_button.setObjectName("publish_button")
        self.check_button = QtWidgets.QPushButton(self.groupBox_2)
        self.check_button.setGeometry(QtCore.QRect(650, 410, 191, 71))
        self.check_button.setObjectName("check_button")
        self.check_button.setText("Check Me")
        self.check_button.clicked.connect(lambda : self.check_me(self.id_phone_line.text()) )

        self.expires_label = QtWidgets.QLabel(self.groupBox_2)
        self.expires_label.setGeometry(QtCore.QRect(600, 130, 181, 51))
        self.expires_label.setObjectName("expires_label")
        self.number_of_people_label = QtWidgets.QLabel(self.groupBox_2)
        self.number_of_people_label.setGeometry(QtCore.QRect(380, 40, 191, 31))
        self.number_of_people_label.setObjectName("number_of_people_label")
        self.food_name = QtWidgets.QLabel(self.groupBox_2)
        self.food_name.setGeometry(QtCore.QRect(380, 40, 191, 101))
        self.food_name.setObjectName("food_name")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeEdit.setGeometry(QtCore.QRect(590, 190, 281, 71))
        self.timeEdit.setObjectName("timeEdit")
        self.indigirent_label = QtWidgets.QLabel(self.groupBox_2)
        self.indigirent_label.setGeometry(QtCore.QRect(30, 70, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.indigirent_label.setFont(font)
        self.indigirent_label.setObjectName("indigirent_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.publish_button.clicked.connect(self.publish_func)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def publish_func(self):
        try:
            # create or open
            conn = sqlite3.connect("housewife.db")
            # create a cursor
            c = conn.cursor()
            # Operation
            c.execute("""CREATE TABLE housewife_info (
                        id integer,
                        name text,
                        number integer,
                        food text,
                        indigirent text,
                        time text


            )""")
            # commit changes
            conn.commit()
            # close the connection
            conn.close()
        except:
            # create or open
            conn = sqlite3.connect("housewife.db")
            # create a cursor
            c = conn.cursor()
            # Operation
            string_time = self.timeEdit.time().toString()

            c.execute("""INSERT INTO housewife_info VALUES(:id,:name,:number,:food,:indigirent,:time)""", {
                "id": int(self.id_phone_line.text()),
                "name": self.name_last_line.text(),
                "number": int(self.number_of_people_line.text()),
                "food": self.food_line.text(),
                "indigirent": self.indigirent_text.toPlainText(),
                "time": string_time
            })
            # commit changes
            conn.commit()
            # close the connection
            conn.close()


    def check_me(self,X):
        # create or open
        conn = sqlite3.connect("housewife.db")
        # create a cursor
        c = conn.cursor()
        # Operation
        c.execute(F"""SELECT * FROM housewife_info WHERE id={X}""")
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
        self.tw.setHeaderLabels(["name food", "number", "expires"])
        for result in results:
            self.l1 = QTreeWidgetItem([f"{result[3]}", f"{result[2]}", f"{result[5]}"])

            self.tw.addTopLevelItem(self.l1)

            self.tw.setColumnCount(3)
        self.w.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HouseWife"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.name_last_label.setText(_translate("MainWindow", "Name/Last"))
        self.id_phone_label.setText(_translate("MainWindow", "ID/Phone No"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.publish_button.setText(_translate("MainWindow", "Publish"))
        self.expires_label.setText(_translate("MainWindow", "Expires :"))
        self.number_of_people_label.setText(_translate("MainWindow", "Number of People :"))
        self.food_name.setText(_translate("MainWindow", "NAme of food :"))
        self.indigirent_label.setText(_translate("MainWindow", "Indigirent >>"))


