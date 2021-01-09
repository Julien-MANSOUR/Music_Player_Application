import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
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
        #######################prog bar###########
        self.progressBar=QProgressBar()
        ######################Button################
        self.addButton=QToolButton()#im using toolbutton bcz it is better to use icons to it
        self.addButton.setIcon(QIcon("images/add.png"))
        self.addButton.setIconSize(QSize(48,48))
        self.addButton.setToolTip("Add a Song")# just adding a hint to my buttons

        self.shuffleButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.shuffleButton.setIcon(QIcon("images/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48, 48))
        self.shuffleButton.setToolTip("Add a Song")  # just adding a hint to my buttons

        self.previousButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.previousButton.setIcon(QIcon("images/previous.png"))
        self.previousButton.setIconSize(QSize(48, 48))
        self.previousButton.setToolTip("Add a Song")  # just adding a hint to my buttons

        self.playButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.playButton.setIcon(QIcon("images/play.png"))
        self.playButton.setIconSize(QSize(48, 48))
        self.playButton.setToolTip("Add a Song")  # just adding a hint to my buttons

        self.nextButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.nextButton.setIcon(QIcon("images/next.png"))
        self.nextButton.setIconSize(QSize(48, 48))
        self.nextButton.setToolTip("Add a Song")  # just adding a hint to my buttons

        self.muteButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.muteButton.setIcon(QIcon("images/mute.png"))
        self.muteButton.setIconSize(QSize(24, 24))
        self.muteButton.setToolTip("Mute")  # just adding a hint to my buttons

    def layouts(self):
        #################creating Layouts#####################
        self.mainLayout=QVBoxLayout()
        self.topMainLayout=QVBoxLayout()
        #if we want to use stylesheet to our layouts we should use a groupe box first
        self.topGroupBox=QGroupBox("Music Player")
        self.topLayout=QHBoxLayout()
        self.middleLayout=QHBoxLayout()
        self.bottomLayout=QVBoxLayout()
        ################Adding Widgets##########################
        ###############Top Layout Widgets#######################
        self.topLayout.addWidget(self.progressBar)
        ###############Middle Layout Widgets#######################
        self.middleLayout.addStretch()
        self.middleLayout.addWidget(self.addButton)
        self.middleLayout.addWidget(self.shuffleButton)
        self.middleLayout.addWidget(self.previousButton)
        self.middleLayout.addWidget(self.playButton)
        self.middleLayout.addWidget(self.nextButton)
        self.middleLayout.addWidget(self.muteButton)
        self.middleLayout.addStretch()

        
        
        
        
        
        
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