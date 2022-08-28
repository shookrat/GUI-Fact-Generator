import os
import sys
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QToolButton, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect
from PyQt5.QtGui import QFont, QCursor, QMovie, QIcon, QPixmap, QFontDatabase, QFont
import random as r
import copy
from my.paletteModule import paletteConfig
from my.factListModule import factlist


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        def resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)
            
        ###################################################################################################

        paletteConfig(self)

        ###################################################################################################

        self.dejavu_font = resource_path("./fonts/DejaVuSans.ttf")
        QFontDatabase.addApplicationFont(self.dejavu_font)
        font = QFont("DejaVu Sans")
        font.setFamily("DejaVu Sans")
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 450)        
        MainWindow.setBaseSize(QSize(800, 450))        
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)

        ###################################################################################################

        self.icon_path = resource_path("./images/space-icon.ico")
        icon = QIcon()
        icon.addPixmap(QPixmap(self.icon_path), QIcon.Normal, QIcon.On)
        #icon.addPixmap(QPixmap("images/space-icon.ico"), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QSize(16, 16))
         
        ###################################################################################################
               
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setGeometry(QRect(0, 0, 800, 450))
        self.centralwidget.setMinimumSize(QSize(800, 450))
        self.centralwidget.setMaximumSize(QSize(800, 450))

        ###################################################################################################

        self.nimbus_font = resource_path("./fonts/NimbusSansNarrowRegular.ttf")
        QFontDatabase.addApplicationFont(self.nimbus_font)
        font = QFont("Nimbus Sans Narrow")
        self.Fact_Output = QLabel(self.centralwidget)
        font.setFamily("Nimbus Sans Narrow")
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(75)
        font.setKerning(True)
        self.Fact_Output.setFont(font)
        self.Fact_Output.setPalette(self.palette)
        self.Fact_Output.setAlignment(Qt.AlignCenter)
        self.Fact_Output.setEnabled(True)
        self.Fact_Output.setGeometry(QRect(100, 80, 600, 241))
        self.Fact_Output.setCursor(QCursor(Qt.IBeamCursor))
        self.Fact_Output.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Fact_Output.setAcceptDrops(True)
        self.Fact_Output.setLayoutDirection(Qt.LayoutDirectionAuto)
        self.Fact_Output.setFrameShape(QFrame.NoFrame)
        self.Fact_Output.setFrameShadow(QFrame.Plain)
        self.Fact_Output.setTextFormat(Qt.AutoText)
        self.Fact_Output.setScaledContents(True)
        self.Fact_Output.setAlignment(Qt.AlignCenter)
        self.Fact_Output.setWordWrap(True)
        self.Fact_Output.setTextInteractionFlags(Qt.TextSelectableByMouse)

        ###################################################################################################
        
        self.tlwg_font = resource_path("./fonts/TlwgTypistBold.ttf")
        QFontDatabase.addApplicationFont(self.tlwg_font)       
        font = QFont("Tlwg Typist")
        self.Generat_Fact = QToolButton(self.centralwidget)
        font.setFamily("Tlwg Typist")
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.Generat_Fact.setFont(font)
        self.Generat_Fact.setPalette(self.palette)
        self.Generat_Fact.setGeometry(QRect(240, 20, 331, 51))
        self.Generat_Fact.setEnabled(True)
        self.Generat_Fact.setText("Generate Fact")       
        self.Generat_Fact.setCursor(QCursor(Qt.PointingHandCursor))
        self.Generat_Fact.setFocusPolicy(Qt.TabFocus)
        self.Generat_Fact.setContextMenuPolicy(Qt.NoContextMenu)
        self.Generat_Fact.setAcceptDrops(True)
        self.Generat_Fact.setAutoFillBackground(True)
        self.Generat_Fact.setPopupMode(QToolButton.InstantPopup)
        self.Generat_Fact.setAutoRaise(True)

        self.Generat_Fact.clicked.connect(self.get_Fact) #<-- Connects the "get_Fact" function to the "Generate_Fact" GUI button.        

        ###################################################################################################

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 800, 450))
        self.label.setMinimumSize(QSize(800, 450))
        self.label.setMaximumSize(QSize(800, 450))
        # self.label.setPixmap(QtGui.QPixmap(":/newPrefix/space.gif"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gif_path = resource_path("./images/space.gif")
        self.gif = QMovie(self.gif_path)
        self.label.setMovie(self.gif)
  
        self.startAnimation()

        self.label.raise_()
        self.Fact_Output.raise_()
        self.Generat_Fact.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        ###################################################################################################

        self.sampled = []
        self.notsampled = factlist
        self.emptylist = []
        
    #######################################################################################################

    def startAnimation(self):
        """Loops .gif image in the background."""
        self.gif.start()    

    def remove_Duplicates(self):
        """Removes duplicate facts, if any, and appends them to "sampled" list."""
        while self.samplefact in self.notsampled:            
            self.notsampled.remove(self.samplefact)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fact Generator"))
        self.Fact_Output.setText(_translate("MainWindow", ""))
        self.Generat_Fact.setText(_translate("MainWindow", "Generate Fact"))

    #######################################################################################################

    def get_Fact(self):
        """Iterates 1050 facts. It's shuffled each session and never in the same order. 
        Once a fact is viewed, it's removed from the list of facts to choose 
        from. Once all facts have been viewed, the same process is repeated."""
        
        r.shuffle(self.notsampled)
        
        try:
            if len(self.notsampled) >= 1:
                self.samplefact = r.choice(self.notsampled) 
                self.newsamplefact = self.samplefact.strip("['\n]")                

        finally:                
            if len(self.notsampled) > 1:
                self.Fact_Output.setText(f"<span style='background-color: #39017d;'>{str(self.newsamplefact)}</p>")                
                self.sampled.append(self.samplefact)
                self.notsampled.remove(self.samplefact) 

            if len(self.notsampled) == 1:                
                self.sampled.append(self.samplefact)
                self.Fact_Output.setText(f"<span style='background-color: #39017d;'>{str(self.notsampled.pop())}</p>")               

            self.remove_Duplicates()

            if len(self.notsampled) == 0:
                self.notsampled = copy.deepcopy(self.sampled)
                self.sampled = copy.deepcopy(self.emptylist)
                
                self.samplefact = r.choice(self.notsampled)
                self.newsamplefact = self.samplefact.strip("['\n]")
                self.Fact_Output.setText(f"<span style='background-color: #39017d;'>{str(self.newsamplefact)}</p>")
                self.sampled.append(self.samplefact)
                self.notsampled.remove(self.samplefact)

###########################################################################################################
            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())