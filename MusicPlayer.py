import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt,QTimer
import os
import random , time
import Style
from pygame import mixer
from mutagen.mp3 import MP3
from mutagen.wave import WAVE #i used wave bcz mp3 isnt working
musicList=[]
muted=False
songLength =0
index=0


#if you want to utilse mixer you should initialise it
mixer.init()#global initialisation outside the classs
count =0 #for timer
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
        self.progressBar.setTextVisible(False)#pour enlever le %
        self.progressBar.setStyleSheet(Style.progressBarStyle())#we use parenthese bcz its is outside of the class
        #####################Labels################
        self.songTimerLabel=QLabel("0:00")
        self.songLengthLabel=QLabel("/ 0:00")

        ######################Button################
        self.addButton=QToolButton()#im using toolbutton bcz it is better to use icons to it
        self.addButton.setIcon(QIcon("images/add.png"))
        self.addButton.setIconSize(QSize(48,48))
        self.addButton.setToolTip("Add a Song")# just adding a hint to my buttons
        self.addButton.clicked.connect(self.addSound)

        self.shuffleButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.shuffleButton.setIcon(QIcon("images/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48, 48))
        self.shuffleButton.setToolTip("Shuffle Songs")  # just adding a hint to my buttons
        self.shuffleButton.clicked.connect(self.shufflePlayList)

        self.previousButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.previousButton.setIcon(QIcon("images/previous.png"))
        self.previousButton.setIconSize(QSize(48, 48))
        self.previousButton.setToolTip("Previous Song")  # just adding a hint to my buttons
        self.previousButton.clicked.connect(self.playPrevious)

        self.playButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.playButton.setIcon(QIcon("images/play.png"))
        self.playButton.setIconSize(QSize(64, 64))
        self.playButton.setToolTip("Play Song")  # just adding a hint to my buttons
        self.playButton.clicked.connect(self.playSounds)

        self.nextButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.nextButton.setIcon(QIcon("images/next.png"))
        self.nextButton.setIconSize(QSize(48, 48))
        self.nextButton.setToolTip("Next Song")  # just adding a hint to my buttons
        self.nextButton.clicked.connect(self.nextSong)

        self.muteButton = QToolButton()  # im using toolbutton bcz it is better to use icons to it
        self.muteButton.setIcon(QIcon("images/mute.png"))
        self.muteButton.setIconSize(QSize(24, 24))
        self.muteButton.setToolTip("Mute")  # just adding a hint to my buttons
        self.muteButton.clicked.connect(self.muteSound)
        ###################Volume Slider##############################
        self.volumeSlider=QSlider(Qt.Horizontal)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.setValue(70)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        mixer.music.set_volume(0.7)#in mixer the min is 0 and max is 1 => so we chose 0.7 to indicate the 70 in slider
        self.volumeSlider.valueChanged.connect(self.setVolume)
        #################Play List###################################
        self.playList=QListWidget()
        self.playList.doubleClicked.connect(self.playSounds)
        self.playList.setStyleSheet(Style.playListStyle())
        ##################Timer##################################3
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateProgressBar)
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
        self.topLayout.addWidget(self.songTimerLabel)
        self.topLayout.addWidget(self.songLengthLabel)
        ###############Middle Layout Widgets#######################
        self.middleLayout.addStretch()
        self.middleLayout.addWidget(self.addButton)
        self.middleLayout.addWidget(self.shuffleButton)
        self.middleLayout.addWidget(self.previousButton)
        self.middleLayout.addWidget(self.playButton)
        self.middleLayout.addWidget(self.nextButton)
        self.middleLayout.addWidget(self.volumeSlider)
        self.middleLayout.addWidget(self.muteButton)
        self.middleLayout.addStretch()
        #################Bottom Layout##################################
        self.bottomLayout.addWidget(self.playList)

        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)
        self.topGroupBox.setLayout(self.topMainLayout)#so now the top and middle layout are now in a single groupe box forming the upper layout of main window
        self.topGroupBox.setStyleSheet(Style.groupBoxStyle())#our homemade function
        self.mainLayout.addWidget(self.topGroupBox,25)#topgroupebox is a widget and not a layout
        self.mainLayout.addLayout(self.bottomLayout,75)
        self.setLayout(self.mainLayout)

    def addSound(self):
        dir=QFileDialog.getOpenFileName(self,"Add Sound","","Sound Files (*.mp3 *.ogg *.wav)")#PyGame can play our sounds : mp3,ogg,wav
        #dir => a tuple : (c:/users/Pc/Sounds/red.mp3 , Sound Files((*.mp3 *.ogg *.wav) )
        fileName=os.path.basename(dir[0])
        #fileName => red.mp3 ,we need just the base name so we can play the song later
        self.playList.addItem(fileName)
        musicList.append(dir[0])#i want to use the url

    def shufflePlayList(self):
        global musicList
        #i need an iterable to use random speciasl function to shuffle
        random.shuffle(musicList)
        #we need to update our list
        self.playList.clear()
        for song in musicList:
            fileName = os.path.basename(song)
            self.playList.addItem(fileName)


    def playSounds(self):
        '''pygame works perfectly with .wav format but not with mp3 on ubunto, it might works on window ,
        but in all cases we can add some lines of code to convert every mp3 files into wav format to avoid any kind of problem'''
        global musicList
        global songLength
        global  count
        global index
        
        count =0 #so our progressbar start freshly from zero and not the last accumulated number
        index=self.playList.currentRow()
        print(index)
        print(musicList[index])
        #we use index for each song so we can play it
        try:
            mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
            mixer.music.load(str(musicList[index]))
            self.progressBar.setValue(0)#start a fresh start
            mixer.music.play()
            self.timer.start()#i should start my timer whenever i start the music
            sound=WAVE(str(musicList[index]))#our song
            songLength=sound.info.length#we took the length
            print(songLength)#songLength=12.84513153 //we need just the unite
            songLength=round(songLength)
            print(songLength)#=>13
            min,sec=divmod(songLength,60)#make division par 60 to find minuts and sec
            #print(min)
            #print(sec)
            self.songLengthLabel.setText("/ {}:{}".format(min,sec))

            self.progressBar.setMaximum(songLength)

        except:
            print("cant")


    def playPrevious(self):
        global musicList
        global songLength
        global count
        global index

        count = 0  # so our progressbar start freshly from zero and not the last accumulated number
        #index = self.playList.currentRow()
        items=self.playList.count()#how many items in the playlist
        print("items",items)
        #bcz when there is no more songs to choose in previous mode we go to the last one de nouveau
        if index == 0:
            index=items #means the last one so we can use previous button de nouveau
        index -=1 #for previous
        print("current index",index)
        # we use index for each song so we can play it
        try:
            mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
            mixer.music.load(str(musicList[index]))
            self.progressBar.setValue(0)  # start a fresh start
            mixer.music.play()
            self.timer.start()  # i should start my timer whenever i start the music
            sound = WAVE(str(musicList[index]))  # our song
            songLength = sound.info.length  # we took the length
            songLength = round(songLength)
            min, sec = divmod(songLength, 60)  # make division par 60 to find minuts and sec
            # print(min)
            # print(sec)
            self.songLengthLabel.setText("/ {}:{}".format(min, sec))

            self.progressBar.setMaximum(songLength)

        except:
            print("cant")

    def nextSong(self):
        global musicList
        global songLength
        global count
        global index

        count = 0  # so our progressbar start freshly from zero and not the last accumulated number
        # index = self.playList.currentRow()
        items = self.playList.count()  # how many items in the playlist
        # bcz when there is no more songs to choose in previous mode we go to the last one de nouveau
        index += 1
        if index == items:
            index = 0
        print("current index",index)
        # we use index for each song so we can play it
        try:
            mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
            mixer.music.load(str(musicList[index]))
            self.progressBar.setValue(0)  # start a fresh start
            mixer.music.play()
            self.timer.start()  # i should start my timer whenever i start the music
            sound = WAVE(str(musicList[index]))  # our song
            songLength = sound.info.length  # we took the length
            songLength = round(songLength)
            min, sec = divmod(songLength, 60)  # make division par 60 to find minuts and sec
            # print(min)
            # print(sec)
            self.songLengthLabel.setText("/ {}:{}".format(min, sec))

            self.progressBar.setMaximum(songLength)

        except:
            print("cant")

    def setVolume(self):
        self.volume=self.volumeSlider.value()
        #print(self.volume)
        mixer.music.set_volume(self.volume/100)#0 and 1 for mixer

    def muteSound(self):
        global muted
        if muted == False:
            mixer.music.set_volume(0.0)
            muted = True
            self.muteButton.setIcon(QIcon("images/unmuted.png"))
            self.muteButton.setToolTip("UnMute")
            self.volumeSlider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.muteButton.setIcon(QIcon("images/mute.png"))
            self.muteButton.setToolTip("Mute")
            self.volumeSlider.setValue(70)
    def updateProgressBar(self):
        global count
        global songLength
        #mutagen package will help us to find the length of our song, so we could know when its over
        count +=1
        self.progressBar.setValue(count)
        ################updating my Label###############
        self.songTimerLabel.setText(time.strftime("%M:%S",time.gmtime(count)))#M for minuts and S for seconds
        ##################################################
        if count == songLength:
            self.timer.stop()

def main():
    App=QApplication(sys.argv)
    window=Player()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()