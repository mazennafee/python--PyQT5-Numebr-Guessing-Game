# import necessary libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
import random
import sys


# create class for our window
class Window(QMainWindow):
    # initiate when start
    def __init__(self):
        # initiate window from parent class
        super().__init__()
        # set fixed size
        self.setFixedSize(400, 400)
        # setting geometry
        self.setGeometry(0, 0, 400, 400)
        # setting Title for our window
        self.setWindowTitle("Number Guessing Game")
        # setting background color
        self.setStyleSheet("background-color : #59B4C3;")
        # assign head 
        self.head()
        # assign info label to be down in our window
        update = "Welcome to start game click start button"
        self.info(update)
        #assign start button to main window
        self.start()
        # set default value to upper bound
        self.upper_bound = 0
        # set default value for lower bound
        self.lower_bound = 0
        # st default value for program guess
        self.pc_guess = 0
        # create attempts 
        self.attempts = 0
        # to count played attempts 
        self.count = 0
        # restart button
        self.rest()
        
        
        # show window
        self.show()
        
    # in function head we will add label to interface showing information
    def head(self):
        # create label and add message and assign it to work on our window
        h = QLabel("Welcome To Number Guessing Game", self)
        # setting head geometry in our window
        h.setGeometry(20, 10, 360, 100)
        # setting font for head and size
        font = QFont("Comic Sans MS", 20)
        # set font to be bold
        font.setBold(True)
        # set underline
        font.setUnderline(False)
        # set italic
        font.setItalic(False)
        # assign font to head label
        h.setFont(font)
        # set text wrap
        h.setWordWrap(True)
        # set color to our label
        h.setStyleSheet("color : #FF8911;")
        # set align to be middle
        h.setAlignment(Qt.AlignCenter)
    # in function info we will add label to interface showing information
    def info(self, update):
        # create label and add message and assign it to work on our window
        info = QLabel(update, self)
        # setting head geometry in our window
        info.setGeometry(20, 380, 360, 30)
        # setting font for head and size
        font = QFont("Comic Sans MS", 8)
        # set font to be bold
        font.setBold(True)
        # set underline
        font.setUnderline(False)
        # set italic
        font.setItalic(False)
        # assign font to head label
        info.setFont(font)
        # set text wrap
        info.setWordWrap(False)
        # set color to our label
        info.setStyleSheet("border : 2px solid #59B4C3 ; color : #211C6A ; background-color : #59B4C3 ;")
        # set align to be middle
        info.setAlignment(Qt.AlignLeft)
        

    def start(self):
        # add button to our window
        start = QPushButton("Start", self)
        #set geometry for our button
        start.setGeometry(90, 200, 100, 40)
        # set style
        #"border-width : 2px ;" "border-style : outset ;""border-radius : 10px;" "border : #59B4C3 ;"
        start.setStyleSheet("QPushButton" "{" 
                            "background-color : #74E291 ;"
                            "color : #211C6A ;"
                            "font : bold 14px ;"
                            "}" )
        start.clicked.connect(self.getint)
    # getint will ask user to enter upper bound and lower bound  and let pc calculate random number 
    def getint(self):
        self.count = 0
        # get upper input in new dialog from user
        i , okpressed = QInputDialog.getInt(self,"Upper Bound", "Please enter upper bound (0:100000): ", 0, 2, 100000, 1)
        if okpressed:
            # if user input integer number for upper bound ask for lower bound in new dialog
            self.upper_bound = i
            x, ok = QInputDialog.getInt(self,"Lower Bound","please enter lower bound (0:99999): ", 0, 0, 100000, 1 )
            #if lower is greater than or equal upper range ask him to renter it again
            while x >= i and ok:
                x, ok = QInputDialog.getInt(self,"Lower Bound","please enter lower bound (0:99999): ", 0, 0, 99999, 1 )
                # if got right number assigning to lower bound and calculate random number for pc
            if ok:
                #if got right number assigning to lower bound
                self.lower_bound = x
                # calculate random number for pc
                self.pc_guess = random.randint(self.lower_bound, self.upper_bound)
                # calculate attempts for player
                self.attempts = round(math.log(self.upper_bound - self.lower_bound + 1, 2) - 2)
                self.inf = QLabel("Guess number between {} and {}: ".format(self.lower_bound, self.upper_bound), self)
                self.inf.setGeometry(20, 380, 360, 30)
                font = QFont("Comic Sans MS", 8)
                # set font to be bold
                font.setBold(True) 
                # set underline
                font.setUnderline(False)
                # set italic
                font.setItalic(False)
                # assign font to head label
                self.inf.setFont(font)
                # set text wrap
                self.inf.setWordWrap(False)
                # set color to our label
                self.inf.setStyleSheet("border : 2px solid #59B4C3 ; color : #211C6A ; background-color : #59B4C3 ;")
                # set align to be middle
                self.inf.setAlignment(Qt.AlignLeft)
                self.inf.show()
                self.spin_box = QSpinBox(self)
                # set spin range lower and upper bound
                self.spin_box.setRange(self.lower_bound, self.upper_bound)
                # setting geometry to be above start button
                self.spin_box.setGeometry(90, 200, 100, 40)
                # setting font
                self.spin_box.setFont(QFont("Comic Sans MS", 15))
                self.spin_box.show()
                self.player_guess = QPushButton("Ok", self)
                # setting geometry to be above start button
                self.player_guess.setGeometry(160, 200, 35, 40)
                # set style
                self.player_guess.setStyleSheet("QPushButton" "{" 
                            "background-color : #74E291 ;"
                            "color : #211C6A ;"
                            "font : bold 14px ;"
                            "}" )
                # adding action to the check button
                self.player_guess.clicked.connect(self.check)
                self.player_guess.show()
                
                self.inf = QLabel("You have only {} attempts to play ".format(self.attempts), self)
                self.inf.setGeometry(20, 120, 360, 60)
                font = QFont("Comic Sans MS", 8)
                # set font to be bold
                font.setBold(True) 
                # set underline
                font.setUnderline(False)
                # set italic
                font.setItalic(False)
                # assign font to head label
                self.inf.setFont(font)
                # set text wrap
                self.inf.setWordWrap(False)
                self.inf.setAlignment(Qt.AlignCenter)
                # set color to our label
                self.inf.setStyleSheet("border : 2px solid #59B4C3 ; color : #211C6A ; background-color : #59B4C3 ;")
                # set align to be middle
                self.inf.setAlignment(Qt.AlignLeft)
                self.inf.show()
                
    
        # create button
        
    # create check function to check win or lose
    def check(self):
        player_guessing = self.spin_box.value()
        self.count += 1
        if self.count < self.attempts:
            if player_guessing == self.pc_guess:
                self.inf = QLabel("Congratulations You Won! ", self)
                self.inf.setGeometry(20, 120, 360, 60)
                font = QFont("Comic Sans MS", 15)
                # set font to be bold
                font.setBold(True) 
                # set underline
                font.setUnderline(False)
                # set italic
                font.setItalic(False)
                # assign font to head label
                self.inf.setFont(font)
                # set text wrap
                self.inf.setWordWrap(False)
                self.inf.setAlignment(Qt.AlignCenter)
                # set color to our label
                self.inf.setStyleSheet("border : 2px solid #59B4C3 ; ")
                color_green = QGraphicsColorizeEffect()
                color_green.setColor(Qt.green)
                self.inf.setGraphicsEffect(color_green)  
                # set align to be middle
                self.inf.setAlignment(Qt.AlignLeft)
                self.inf.show()
                # add restart button or exit
            elif player_guessing > self.pc_guess or player_guessing < self.pc_guess :
                self.inf = QLabel("You Used  {} from {} attempts ".format(self.count, self.attempts), self)
                self.inf.setGeometry(20, 120, 360, 60)
                font = QFont("Comic Sans MS", 8)
                # set font to be bold
                font.setBold(True) 
                # set underline
                font.setUnderline(False)
                # set italic
                font.setItalic(False)
                # assign font to head label
                self.inf.setFont(font)
                # set text wrap
                self.inf.setWordWrap(False)
                self.inf.setAlignment(Qt.AlignCenter)
                # set color to our label
                self.inf.setStyleSheet("border : 2px solid #59B4C3 ; color : #211C6A ; background-color : #59B4C3 ;")
                # set align to be middle
                self.inf.setAlignment(Qt.AlignLeft)
                self.inf.show()
        if self.count >= self.attempts :
            self.inf = QLabel("You Used  all {} attempts \nnumber was {} \ngood luck next Time".format(self.count, self.pc_guess), self)
            self.inf.setGeometry(20, 120, 360, 60)
            font = QFont("Comic Sans MS", 8)
            # set font to be bold
            font.setBold(True) 
            # set underline
            font.setUnderline(False)
            # set italic
            font.setItalic(False)
            # assign font to head label
            self.inf.setFont(font)
            # set text wrap
            self.inf.setWordWrap(True)
            self.inf.setAlignment(Qt.AlignCenter)
            # set color to our label
            self.inf.setStyleSheet("border : 2px solid #59B4C3 ;  ")
            color_red = QGraphicsColorizeEffect()
            color_red.setColor(Qt.red)
            self.inf.setGraphicsEffect(color_red)
            # set align to be middle
            self.inf.setAlignment(Qt.AlignLeft)
            self.inf.show()
            self.player_guess.hide()
            self.spin_box.hide()
    def rest(self):
        rest = QPushButton("rest", self)
        #set geometry for our button
        rest.setGeometry(200, 200, 100, 40)
        # set style
        #"border-width : 2px ;" "border-style : outset ;""border-radius : 10px;" "border : #59B4C3 ;"
        rest.setStyleSheet("QPushButton" "{" 
                            "font : bold 14px ;"
                            "}" )
        color_red = QGraphicsColorizeEffect()
        color_red.setColor(Qt.red)
        rest.setGraphicsEffect(color_red)
        
        rest.clicked.connect(self.getint)
        
        

# create application from qt5
app = QApplication(sys.argv)
#create instance of our window
window = Window()
#start application
sys.exit(app.exec())