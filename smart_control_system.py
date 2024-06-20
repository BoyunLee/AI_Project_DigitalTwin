from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QDateTime, QUrl, QCoreApplication,QFileInfo
import sys
import cv2
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings
import subprocess
from PyQt5.QtCore import QThread
import sqlite3
from datetime import datetime

######################################################################################
dongdaemungu = ""
jonro1 = ""
seodaemungu =""
jungu = ""
jonro2 = ""
#####################################################################################
image_files1=""
image_files2=""
image_files3=""
image_files4=""
image_files5=""
image_files6=""
image_files7=""
image_files8=""
image_files9=""
#####################################################################################

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow           
        self.MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(QtGui.QPixmap("cctv.jpg"))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(515, 32, 408, 275))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(986, 32, 408, 275))
        self.label_2.setObjectName("label_2")      
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1460, 32, 408, 275))
        self.label_4.setObjectName("label_4")   
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(515, 374, 408, 275))
        self.label_5.setObjectName("label_5")   
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(986, 374, 408, 275))
        self.label_6.setObjectName("label_6")   
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1460, 374, 408, 275))
        self.label_7.setObjectName("label_7")   
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(515, 726, 408, 275))
        self.label_8.setObjectName("label_8")   
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(986, 726, 408, 275))
        self.label_9.setObjectName("label_9")   
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1460, 726, 408, 275))
        self.label_10.setObjectName("label_10")   
        
        self.web_label = WebLabel(MainWindow)
        self.web_label.setGeometry(QtCore.QRect(18, 298, 426, 754))
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 315, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("pushButton")
        self.pushButton.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton.clicked.connect(self.open1)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1142, 315, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("pushButton")
        self.pushButton_2.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_2.clicked.connect(self.open1)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1620, 315, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("pushButton")
        self.pushButton_3.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_3.clicked.connect(self.open3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(670, 658, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("pushButton")
        self.pushButton_4.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_4.clicked.connect(self.open2)

        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1142, 658, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("pushButton")
        self.pushButton_5.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_5.clicked.connect(self.open2)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1620, 658, 91, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("pushButton")
        self.pushButton_6.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_6.clicked.connect(self.open4)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(670, 1010, 91, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("pushButton")
        self.pushButton_7.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_7.clicked.connect(self.open5)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1142, 1010, 91, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setText("pushButton")
        self.pushButton_8.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_8.clicked.connect(self.open5)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1620, 1010, 91, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setText("pushButton")
        self.pushButton_9.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_9.clicked.connect(self.open5)

        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(0,0,458,206))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.pushButton_10.clicked.connect(self.recoding)
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1890,1,30,26))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setStyleSheet("color: red; background-color: rgba(0, 0, 0, 0.0); border: none; font-size:20pt;font-weight:bold;")
        self.pushButton_11.setText('X')
        self.pushButton_11.clicked.connect(QCoreApplication.instance().quit)
        
        self.isrunnigs = False
        self.start_thread()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def recoding(self):
        text1 = 'rtsp://210.99.70.120:1935/live/cctv010.stream'
        text2=text1.split('/')
        text3=text2[-1].split('.')
        text4=text3[0]

        text5 = 'rtsp://210.99.70.120:1935/live/cctv011.stream'
        text6=text5.split('/')
        text7=text6[-1].split('.')
        text8=text7[0]

        s1 = "37.590059,127.055832"
        w1 = s1.split(',')
        lat1 = w1[0]
        long1 = w1[1]
             
        text9 = 'rtsp://210.99.70.120:1935/live/cctv012.stream'
        text10=text9.split('/')
        text11=text10[-1].split('.')
        text12=text11[0]
        s2 = "37.586208,126.946906"
        w2 = s2.split(',')
        lat2 = w2[0]
        long2 = w2[1]
        
        
        text13 = 'rtsp://210.99.70.120:1935/live/cctv019.stream'
        text14=text13.split('/')
        text15=text14[-1].split('.')
        text16=text15[0]
        
        text17 = 'rtsp://210.99.70.120:1935/live/cctv020.stream'
        text18=text17.split('/')
        text19=text18[-1].split('.')
        text20=text19[0]
        
        s3 = "37.575474,126.982693"
        w3 = s3.split(',')
        lat3 = w3[0]
        long3 = w3[1]
        
        text21 = 'rtsp://210.99.70.120:1935/live/cctv015.stream'
        text22=text21.split('/')
        text23=text22[-1].split('.')
        text24=text23[0]
        
        text25 = 'rtsp://210.99.70.120:1935/live/cctv024.stream'
        text26=text25.split('/')
        text27=text26[-1].split('.')
        text28=text27[0]
        
        s4 = "37.575474,126.982693"
        w4 = s4.split(',')
        lat4 = w4[0]
        long4 = w4[1]
        
        text29 = 'rtsp://210.99.70.120:1935/live/cctv026.stream'
        text30=text29.split('/')
        text31=text30[-1].split('.')
        text32=text31[0]
        
        text33 = 'rtsp://210.99.70.120:1935/live/cctv016.stream'
        text34=text33.split('/')
        text35=text34[-1].split('.')
        text36=text35[0]
        
        s5 = "37.575474,126.982693"
        w5 = s5.split(',')
        lat5 = w5[0]
        long5 = w5[1]

        con = sqlite3.connect('rtsp.db',check_same_thread=False)
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS rtsp (ID INTEGER PRIMARY KEY, name text, rtsp_path text, save_path text, lat text, long text)')
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text4,text1,lat1,long1))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text8,text5,lat1,long1))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text12,text9,lat2,long2))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text16,text13,lat3,long3))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text20,text17,lat3,long3))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text24,text21,lat4,long4))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text28,text25,lat5,long5))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text32,text29,lat5,long5))
        cur.execute("INSERT OR IGNORE INTO rtsp (name,rtsp_path,lat,long) VALUES (?,?,?,?);", (text36,text33,lat5,long5))
        con.commit()
        con.close() 

        self.th10 = Thread10(self)
        self.th10.start() 

    def start_thread(self):
        self.isrunnigs=True
        self.th = Thread(self)  # 스레드 생성 및 시작
        self.th.changePixmap.connect(self.label.setPixmap)
        self.th.start()
        self.label.show()
        
        self.th2 = Thread2(self)  # 스레드 생성 및 시작
        self.th2.changePixmap.connect(self.label_2.setPixmap)
        self.th2.start()
        self.label_2.show()
        
        self.th3 = Thread3(self)  # 스레드 생성 및 시작
        self.th3.changePixmap.connect(self.label_4.setPixmap)
        self.th3.start()
        self.label_4.show()

        self.th4 = Thread4(self)  # 스레드 생성 및 시작
        self.th4.changePixmap.connect(self.label_5.setPixmap)
        self.th4.start()
        self.label_5.show()
        

        self.th5 = Thread5(self)  # 스레드 생성 및 시작
        self.th5.changePixmap.connect(self.label_6.setPixmap)
        self.th5.start()
        self.label_6.show()        
        
        self.th6 = Thread6(self)  # 스레드 생성 및 시작
        self.th6.changePixmap.connect(self.label_7.setPixmap)
        self.th6.start()
        self.label_7.show()        
        

        self.th7 = Thread7(self)  # 스레드 생성 및 시작
        self.th7.changePixmap.connect(self.label_8.setPixmap)
        self.th7.start()
        self.label_8.show()        

        self.th8 = Thread8(self)  # 스레드 생성 및 시작
        self.th8.changePixmap.connect(self.label_9.setPixmap)
        self.th8.start()
        self.label_9.show()   
        
        self.th9 = Thread9(self)  # 스레드 생성 및 시작
        self.th9.changePixmap.connect(self.label_10.setPixmap)
        self.th9.start()
        self.label_10.show()    
        
    def open1(self):
        global dongdaemungu
        if self.isrunnigs:
            dongdaemungu ="37.590059,127.055832"
            self.window = QtWidgets.QWidget()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()
          
    def open2(self):
        global jonro1
        if self.isrunnigs:
            jonro1 = "37.575474,126.982693"
            self.window = QtWidgets.QWidget()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()
     
    def open3(self):
        global seodaemungu
        if self.isrunnigs:
            seodaemungu ="37.586208,126.946906"
            self.window = QtWidgets.QWidget()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def open4(self):
        global jungu
        if self.isrunnigs:
            jungu="37.559111,127.005753"
            self.window = QtWidgets.QWidget()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def open5(self):
        global jonro2
        if self.isrunnigs:
            jonro2 ="37.5755901,127.0232426"
            self.window = QtWidgets.QWidget()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class WebLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.web_view.setUrl(QUrl.fromLocalFile(QFileInfo('./map/filename.html').absoluteFilePath()))
        self.web_view.loadFinished.connect(self.load_finished)
        self.web_view.loadStarted.connect(self.load_started)
        self.web_view.urlChanged.connect(self.url_changed)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.web_view)
        self.setLayout(layout)

    def load_finished(self):
        print("Web content loaded successfully")
    def load_started(self):
        print("Web content loading started")
    def url_changed(self, url):
        print(f"URL changed: {url.toString()}")
    def load_error(self, error):
        print(f"Error loading web content: {error}")
    
class WebLabel1(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        if dongdaemungu:
            self.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/동대문구.html").absoluteFilePath()))
        elif seodaemungu:
            self.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/서대문구.html").absoluteFilePath()))
        elif jonro1:
            self.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구.html").absoluteFilePath()))
        elif jonro2:
            self.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구2.html").absoluteFilePath()))
        elif jungu:
            self.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/중구.html").absoluteFilePath()))
        self.web_view.loadFinished.connect(self.load_finished)
        self.web_view.loadStarted.connect(self.load_started)
        self.web_view.urlChanged.connect(self.url_changed)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.web_view)
        self.setLayout(layout)

    def load_finished(self):
        print("Web content loaded successfully")
    def load_started(self):
        print("Web content loading started")
    def url_changed(self, url):
        print(f"URL changed: {url.toString()}")
    def load_error(self, error):
        print(f"Error loading web content: {error}")

class Ui_SecondWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        global dongdaemungu, seodaemungu, jungu, jonro1, jonro2
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow = MainWindow
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap("Main_7.jpg"))
        
        self.datetime = QDateTime.currentDateTime()
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(55, 566, 391, 52))
        self.label2.setObjectName("label2")
        self.label2.setText(self.datetime.toString(Qt.DefaultLocaleLongDate))
        self.label2.setStyleSheet('font-size : 17pt;')
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(41, 258, 391, 50))
        self.label3.setObjectName("label3")
        self.label3.setStyleSheet('font-size : 17pt;')
        
        self.lat =""
        self.lot =""
        if dongdaemungu:
            dongdaemungu1 = dongdaemungu.split(',')
            self.lat = dongdaemungu1[0]
            self.lot = dongdaemungu1[1]
            self.label3.setText(self.lat)
        elif seodaemungu:
            seodaemungu1 = seodaemungu.split(',')
            self.lat = seodaemungu1[0]
            self.lot = seodaemungu1[1]
            self.label3.setText(self.lat)
        elif jonro2:
            jonro2_1 = jonro2.split(',')
            self.lat = jonro2_1[0]
            self.lot = jonro2_1[1]
            self.label3.setText(self.lat)
        elif jonro1:
            jonro1_1 = jonro1.split(',')
            self.lat = jonro1_1[0]
            self.lot = jonro1_1[1]
            self.label3.setText(self.lat)
        elif jungu:
            jungu1 = jungu.split(',')
            self.lat = jungu1[0]
            self.lot = jungu1[1]
            self.label3.setText(self.lat)
        
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(41, 411, 391, 50))
        self.label4.setObjectName("label4")
        self.label4.setStyleSheet('font-size : 17pt;')
        
        if dongdaemungu:
            self.label4.setText(self.lot)
        elif seodaemungu:
            self.label4.setText(self.lot)
        elif jonro2:
            self.label4.setText(self.lot)
        elif jonro1:
            self.label4.setText(self.lot)
        elif jungu:
            self.label4.setText(self.lot)

        self.web_label = WebLabel1(MainWindow)
        self.web_label.setGeometry(QtCore.QRect(468, 93, 1450, 985))
        
        self.btn = QPushButton(self.centralwidget)
        self.btn.setGeometry(1, 1, 368, 87)
        self.btn.setObjectName("PushButton")
        self.btn.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.btn.clicked.connect(self.open)
        

        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setGeometry(161, 735, 65, 65)
        self.btn1.setObjectName("PushButton1")
        self.btn1.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.btn1.clicked.connect(self.weather_rainy)
        
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setGeometry(246, 733, 65, 65)
        self.btn2.setObjectName("PushButton2")
        self.btn2.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.btn2.clicked.connect(self.weather_sunny)
        
        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setGeometry(39,901,392,52)
        self.btn3.setObjectName("PushButton3")
        self.btn3.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0.0); border: none;")
        self.btn3.clicked.connect(self.change)
        
        self.rainy=False
        self.sunny=False
        self.MainWindow = MainWindow    
        self.MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
    
    def open(self):
        global dongdaemungu, seodaemungu, jonro1, jonro2, jungu
        # self.main_window = QtWidgets.QMainWindow()
        # self.main_ui = Ui_MainWindow()
        # self.main_ui.setupUi(self.main_window)
        self.MainWindow.destroy()
        dongdaemungu = ""
        seodaemungu = ""
        jonro1 = ""
        jonro2 = ""
        jungu = ""
    
    def weather_rainy(self):
        self.rainy=True
        self.sunny=False
    def weather_sunny(self):
        self.rainy=False
        self.sunny=True
    
    def change(self):
        self.datetime1 = self.datetime.toString('HH')
        # 동대문구
        if dongdaemungu and (int(self.datetime1)<12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/동대문구_이문로.html").absoluteFilePath()))   
        elif dongdaemungu and (int(self.datetime1)>=12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/동대문구_망우로.html").absoluteFilePath()))
        elif dongdaemungu and (int(self.datetime1)<12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/동대문구_회기로.html").absoluteFilePath()))   
        elif dongdaemungu and (int(self.datetime1)>=12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/동대문구_이문로.html").absoluteFilePath()))
        
        # 종로구    
        elif jonro1 and (int(self.datetime1)<12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구_새문안로.html").absoluteFilePath()))   
        elif jonro1 and (int(self.datetime1)>=12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구_율곡로.html").absoluteFilePath()))
        elif jonro1 and (int(self.datetime1)<12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구_사직로.html").absoluteFilePath()))   
        elif jonro1 and (int(self.datetime1)>=12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구_새문안로.html").absoluteFilePath()))   
        
        # 서대문구    
        elif seodaemungu and (int(self.datetime1)<12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/서대문구_모래내로.html").absoluteFilePath()))   
        elif seodaemungu and (int(self.datetime1)>=12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/서대문구_통일로.html").absoluteFilePath()))
        elif seodaemungu and (int(self.datetime1)<12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/서대문구_통일로.html").absoluteFilePath()))   
        elif seodaemungu and (int(self.datetime1)>=12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/서대문구_모래내로.html").absoluteFilePath()))    
        
        # 중구    
        elif jungu and (int(self.datetime1)<12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/중구_동호로.html").absoluteFilePath()))   
        elif jungu and (int(self.datetime1)>=12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/중구_장춘단로.html").absoluteFilePath()))
        elif jungu and (int(self.datetime1)<12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/중구_장춘단로.html").absoluteFilePath()))   
        elif jungu and (int(self.datetime1)>=12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/중구_동호로.html").absoluteFilePath()))  
        
        # 종로구2    
        elif jonro2 and (int(self.datetime1)<12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구2_왕산로.html").absoluteFilePath()))   
        elif jonro2 and (int(self.datetime1)>=12) and self.sunny:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구2_종로.html").absoluteFilePath()))
        elif jonro2 and (int(self.datetime1)<12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구2_대학로.html").absoluteFilePath()))   
        elif jonro2 and (int(self.datetime1)>=12) and self.rainy:
            self.web_label.web_view.setUrl(QUrl.fromLocalFile(QFileInfo("./map/종로구2_안암로.html").absoluteFilePath()))            
          
class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self,parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True


    def run(self):
        try:
            image_files1 = 'rtsp://210.99.70.120:1935/live/cctv010.stream'
            cap = cv2.VideoCapture(image_files1)

            if cap.isOpened() is False:
                self.isRunning = False
            else :
                self.isRunning = True
     
            while self.isRunning:
                ret, frame = cap.read()
                if ret:
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                    convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                    p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                    self.changePixmap.emit(p)
                else:
                    self.isRunning = False  
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread2(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True


    def run(self):
        image_files2 = 'rtsp://210.99.70.120:1935/live/cctv011.stream'
        cap = cv2.VideoCapture(image_files2)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True
            
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
            else:
                self.isRunning = False             
        cap.release()
        cv2.destroyAllWindows()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False

class Thread3(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True


    def run(self):
        image_files3 = 'rtsp://210.99.70.120:1935/live/cctv012.stream'
        cap = cv2.VideoCapture(image_files3)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True

        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread4(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True

    def run(self):
        image_files4 = 'rtsp://210.99.70.120:1935/live/cctv019.stream'
        cap = cv2.VideoCapture(image_files4)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread5(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)

    def run(self):
        image_files5 = 'rtsp://210.99.70.120:1935/live/cctv020.stream'
        cap = cv2.VideoCapture(image_files5)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True

        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread6(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True


    def run(self):
        image_files6 = 'rtsp://210.99.70.120:1935/live/cctv015.stream'
        cap = cv2.VideoCapture(image_files6)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True
         
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)

            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()


    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread7(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True


    def run(self):
        image_files7 = 'rtsp://210.99.70.120:1935/live/cctv024.stream'
        cap = cv2.VideoCapture(image_files7)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True

        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()


    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread8(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True


    def run(self):    
        image_files8 = 'rtsp://210.99.70.120:1935/live/cctv026.stream'
        cap = cv2.VideoCapture(image_files8)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False
        
class Thread9(QThread):
    changePixmap = pyqtSignal(QPixmap)
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True

    def run(self):
        image_files9 = 'rtsp://210.99.70.120:1935/live/cctv018.stream'
        cap = cv2.VideoCapture(image_files9)
        
        if cap.isOpened() is False:
            self.isRunning = False
        else :
            self.isRunning = True
            
        while self.isRunning:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(408, 275, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)

            else:
                self.isRunning = False

        cap.release()
        cv2.destroyAllWindows()            

    def resume(self):
        self.isRunning = True

    def stop(self):
        cv2.destroyAllWindows()
        self.isRunning = False

class Thread10(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        
    def run(self):
        subprocess.call("./output/save_file2/save_file2.exe")      

        
if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)
    MainWindow.show() 
    sys.exit(app.exec_())
