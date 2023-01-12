from tkinter import *
from tkinter import messagebox
from game import Game
import tkinter.font as tkFont

# set an initial name for players
playerName='Player'
option = {0:"Scissors",1:"Paper",2:"Rock",3:"Lizard",4:"Spock"}

# the frame for start page
class StartWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        
        self.set_wedgets()
    # create wedgets
    def set_wedgets(self):

        # follow labels have no meaning, just for layout
        # id don't do that other wedgets can't be seen
        for i in range(5):
            self.emptyLabel = Label(self, text='',height= 5,width= 12)
            self.emptyLabel.grid(row=i,column=i)
        
        self.helloLabel = Label(self, text='Hi, welcome to Special Computer Game! \n What is your name?'
                                  ,font=f_title)
        self.helloLabel.place(x=35,y=60)
        # enter player's name
        self.varName = StringVar()
        self.nameEntry = Entry(self,textvariable=self.varName)
        self.nameEntry.place(x=90,y=155)

        # comfirm button and start the game
        self.nameButton = Button(self, text='Comfirm', width= 12,font=f_b1,command=self.next_frame)
        self.nameButton.place(x=270,y=150)
        # exit button to close the window
        self.exitButton = Button(self, text='Exit', width= 12, font=f_b1, command=root.destroy)
        self.exitButton.place(x=345,y=320)


    # if player click the comfirm button, the interface will change to the one for game
    def next_frame(self):
        global playerName
        # if player don't enter anything, playerName will keep the initial value: Player
        if self.nameEntry.get() != '':
            playerName = self.nameEntry.get()
        # close the start page
        self.destroy()
        GameWindow(master=root)

# the frame for game page
class GameWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=0,y=25)
        self.game = Game()
        
        self.set_wedgets()

    def set_wedgets(self):
        # welcome words with player's name
        self.helloLabel = Label(self, text='Welcome %s' % playerName,width= 45, font=f_title)
        self.helloLabel.grid(row=0, columns=5)
        
        # it has no meaning, just for layout
        for i in range(1,5):
            self.emptyLabel = Label(self, text='',height= 5,width= 12)
            self.emptyLabel.grid(row=i,column=i)

        # make a single selection menu
        self.var = IntVar()
        self.var.set(0)
        for x, y in option.items():
            Radiobutton(self, text=y, value=x,font=f_radio, variable=self.var).place(x=420,y=(70+x*30))

        # comfirm button
        self.comfirmButton = Button(self, text='I decide',width= 12,font=f_b1, command=self.get_result)
        self.comfirmButton.place(x=420,y=240)
        # exit button
        self.exitButton = Button(self, text='Exit',width= 12,font=f_b1, command=root.destroy)
        self.exitButton.place(x=420,y=280)


        self.messageLabel = Label(self, text='Don\'t know the rule? No worry, just try it!', font=f_b1)
        self.messageLabel.place(x=180,y=35)

        # show current score
        self.scoreLabel = Label(self, text='WIN: 0      TIE: 0      LOSE: 0        TOTAL:0/5',font=f_message)
        self.scoreLabel.place(x=65,y=70)
        # display the choices of both parties and result
        self.choiceLabel = Label(self, text='',font=f_message)
        self.choiceLabel.place(x=65,y=105)
        self.resultLabel = Label(self, text='',font=f_message)
        self.resultLabel.place(x=65,y=130)
        # show the final result
        self.finalResultLabel = Label(self, text='',font=f_underline)
        self.finalResultLabel.place(x=65,y=180)

    # instantiate game class and get the result for current game
    def get_result(self):
        self.game.random_choice()
        self.game.get_result(self.var.get())
        # update the score and other information
        self.scoreLabel.configure(text='WIN: %d      TIE: %d      LOSE: %d        TOTAL:%d/5'
                                  %(self.game.playerWin, self.game.tie,
                                  self.game.playerLose, self.game.count))
        self.choiceLabel.configure(text=playerName+':  '+option[self.var.get()]+
                                   ';        Computer:  '+option[self.game.computerChoice])
        self.resultLabel.configure(text=playerName+self.game.realCondition)
        # play a tournament of five games
        if self.game.count == 5:
            if self.game.playerWin > self.game.playerLose:
                self.finalResultLabel.configure(text="Congratulation! You win the game!")
            elif self.game.playerWin < self.game.playerLose:
                self.finalResultLabel.configure(text="Sorry, you lose the game.")
            else:
                self.finalResultLabel.configure(text="It\'s a tie. Try again?")
            # reset the data of game and change the butoon
            self.game.reset()
            self.comfirmButton.destroy()
            self.nextButton = Button(self, text='Next', width= 12,font=f_b1,command=self.go_result_frame)
            self.nextButton.place(x=420,y=240)

    # go to a new page
    def go_result_frame(self):
        self.destroy()
        ResultWindow(master=root)

# the frame for final page
class ResultWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.place(x=60,y=20)
        
        self.set_wedgets()

    def set_wedgets(self):
        # enter player's name
        self.helloLabel = Label(self, text='Start another tournament ?',height=8,width= 35,font=f_title)
        self.helloLabel.grid(row=0, column=0)


        self.newGameButton = Button(self, text='Yes', command=self.next_frame,width= 12,font=f_b1)
        self.newGameButton.place(x=190,y=140)
        self.exitButton = Button(self, text='Exit', command=root.destroy,width= 12,font=f_b1)
        self.exitButton.place(x=190,y=180)

    # back to game page
    def next_frame(self):  
        self.destroy()
        GameWindow(master=root)


if __name__ == '__main__':
    
    root = Tk()
    # set some font for text
    f_title = tkFont.Font(family='Times New Roman', size=18)
    f_radio = tkFont.Font(family='Times New Roman', size=14)
    f_b1 = tkFont.Font(family='Times New Roman', size=10)
    f_message = tkFont.Font(family='Times New Roman', size=12)
    f_underline = tkFont.Font(family='Times New Roman', size=14)
    f_underline.configure(underline = True)
    # keep the window position in the middle of the screen
    width = 600
    height = 400
    x = (root.winfo_screenwidth() - width)/2
    y = (root.winfo_screenheight() - height)/2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.title('SpecialComputerGame')
    
    StartWindow(master=root)

    root.mainloop()
