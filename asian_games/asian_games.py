from lxml import html
import requests as rq
import matplotlib.pyplot as mp
import py2exe as exe

import sys
from PyQt5 import QtWidgets,QtGui,QtCore,sip

from functools import partial

class Window(QtWidgets.QMainWindow):

    def __init__(self,title,height,height1,height2,height3,country):
        super().__init__()                                           #used for providing control to the inherited module
        self.setGeometry(50,50,300,300)
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.height = height
        self.height1 = height1
        self.height2 = height2
        self.height3 = height3
        self.country = country
        self.title = title
        self.label = "Total Medals"
        self.label1 = "Gold Medals"
        self.label2 = "Silver Medals"
        self.label3 = "Bronze Medals"

        extractAction = QtWidgets.QAction("&Exit",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the tip")
        extractAction.triggered.connect(sys.exit)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        self.home()
        

    def home(self):
        btn = QtWidgets.QPushButton("Total Medals",self)
        btn1 = QtWidgets.QPushButton("Gold Medals",self)
        btn2 = QtWidgets.QPushButton("Silver Medals",self)
        btn3 = QtWidgets.QPushButton("Bronze Medals",self)
        btn.clicked.connect(partial(self.plotMedals,self.height,self.label))
        btn.resize(btn.sizeHint())
        btn.move(100,50)
        btn1.clicked.connect(partial(self.plotMedals,self.height1,self.label1))
        btn1.resize(btn1.sizeHint())
        btn1.move(100,80)
        btn2.clicked.connect(partial(self.plotMedals,self.height2,self.label2))
        btn2.resize(btn2.sizeHint())
        btn2.move(100,110)
        btn3.clicked.connect(partial(self.plotMedals,self.height3,self.label3))
        btn3.resize(btn3.sizeHint())
        btn3.move(100,140)
        self.show()

    def plotMedals(self,height,label):
        mp.figure(figsize=(13, 8))
        mp.bar(list(range(1,13)), height, tick_label = self.country,width = 0.8, color = ['red', 'green'])
        mp.xticks(rotation = 30)
        mp.xlabel('Country')
        mp.ylabel(label) 
        mp.title(self.title)
        mp.show()
        
        
        
       
def run():
    website = 'https://sports.ndtv.com/asian-games-2018/medals-tally'
    page = rq.get(website)
    tree = html.fromstring(page.content)
    rawdata = tree.xpath('//td/text()')
    country = rawdata[1:72:6]
    total_medals = rawdata[5:72:6]
    gold_medals = rawdata[2:72:6]
    silver_medals = rawdata[3:72:6]
    bronze_medals = rawdata[4:72:6]
    height = []
    height1 = []
    height2 = []
    height3 = []
    for i in total_medals:
        height.append(int(i))
    for i in gold_medals:
        height1.append(int(i))
    for i in silver_medals:
        height2.append(int(i))
    for i in bronze_medals:
        height3.append(int(i))
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window("Asian Games",height,height1,height2,height3,country)
    sys.exit(app.exec_())

run()



