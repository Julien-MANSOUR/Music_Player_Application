import sys
from PyQt5.QtWidgets import*

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450,150,480,700)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
    def widgets(self):
        pass
    def layouts(self):
        #################creating Layouts#####################
        self.mainLayout=QVBoxLayout()
        self.topMainLayout=QVBoxLayout()
        #if we want to use stylesheet to our layouts we should use a groupe box first
        self.topGroupBox=QGroupBox("Music Player",self)
        self.topLayout=QHBoxLayout()
        self.middleLayout=QHBoxLayout()
        self.bottomLayout=QVBoxLayout()
        ################Adding Widgets##########################
        ###############Top Layout Widgets#######################
        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)
        self.topGroupBox.setLayout(self.topMainLayout)#so now the top and middle layout are now in a single groupe box forming the upper layout of main window
        self.topGroupBox.setStyleSheet("background-color : orange")
        self.mainLayout.addWidget(self.topGroupBox)#topgroupebox is a widget and not a layout
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

def main():
    App=QApplication(sys.argv)
    window=Player()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()