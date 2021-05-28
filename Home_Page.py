

from PyQt5 import QtCore, QtGui, QtWidgets
from housewife_window import Ui_MainWindow_1
from student import Ui_MainWindow_2
import sqlite3
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 884)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 411, 481))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("student_button")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 250, 411, 481))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("housewife_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 130, 871, 71))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(lambda: self.call_it(1))
        self.pushButton.clicked.connect(lambda :self.call_it(2))
        self.time_check()



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #x is for either open student page or house wife page
    def call_it(self,x=None):
        if x==1:
            #call housewife Page
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_1()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
        elif x==2:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_2()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FooD CompanY"))
        self.pushButton.setText(_translate("MainWindow", "STUDENT"))
        self.pushButton_2.setText(_translate("MainWindow", "HOUSEWIFE"))
        self.label.setText(_translate("MainWindow", ":CHOOSE YOUR HERO:"))

    def time_check(self):
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
        my_time_list=[]
        for result in results:
            food_time=result[5]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            cur = datetime.strptime(f"{current_time[:2]}:{current_time[3:5]}:{current_time[6:8]}", "%H:%M:%S")
            foo = datetime.strptime(f"{food_time[:2]}:{food_time[3:5]}:{food_time[6:8]}", "%H:%M:%S")
            if len(str(foo-cur))>8:
                print(str(foo-cur))
                print(result[0])


                # create or open
                conn = sqlite3.connect("housewife.db")
                # create a cursor
                c = conn.cursor()
                # Operation
                c.execute(f"""DELETE FROM housewife_info WHERE id={result[0]}""")


                results = c.fetchall()
                # commit changes
                conn.commit()
                # close the connection
                conn.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
