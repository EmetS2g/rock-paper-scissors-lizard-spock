import random

# implementation of the game
class Game():
    def __init__(self):

        # data that records the progress of the game
        self.count = 0
        self.tie = 0
        self.playerWin = 0
        self.playerLose = 0
        # the value of result: 0 means computer wins, 1 means players wins, and 2 means they do same choice
        self.result = 0
        # expression for the ten conditions
        self.condition = ['scissors decapitates lizard.',        #0
                          'scissors cuts paper.',                #1
                          'paper disproves spock.',              #2
                          'paper covers rock.',                  #3
                          'rock crushes scissors.',              #4
                          'rock crushes lizard.',                #5
                          'lizard eats paper.',                  #6
                          'lizard poisons spock.',               #7
                          'spock vaporizes rock.',               #8
                          'spock smashes scissors.',             #9
                          ', it\'s a tie because both chose ']   #10
        # situation of game: win, lose, or tie 
        self.realCondition = ''

    # the random choice of computer
    def random_choice(self):
        self.computerChoice = random.randint(0,4)

    # reset the data after a tournament
    def reset(self):
        self.tie = 0
        self.playerWin = 0
        self.playerLose = 0
        self.count = 0

    # compare two choices and give the result
    def get_result(self, playerChoice):
        self.playerChoice = playerChoice
        self.count=self.count+1

        # 25 situations in total
        if self.computerChoice == 0:
            if self.playerChoice == 0:
                self.result = 2
                self.tie = self.tie + 1
                self.realCondition = self.condition[10]+'Scissors.'
            elif self.playerChoice == 1:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[1]
            elif self.playerChoice ==2:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[4]
            elif self.playerChoice ==3:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[0]
            else:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[9]
        elif self.computerChoice == 1:
            if self.playerChoice ==0:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[1]
            elif self.playerChoice ==1:
                self.result = 2
                self.tie = self.tie + 1
                self.realCondition = self.condition[10]+'Paper.'
            elif self.playerChoice ==2:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[3]
            elif self.playerChoice ==3:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[6]
            else:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[2]
        elif self.computerChoice == 2:
            if self.playerChoice ==0:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[4]
            elif self.playerChoice ==1:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[3]
            elif self.playerChoice ==2:
                self.result = 2
                self.tie = self.tie + 1
                self.realCondition = self.condition[10]+'Rock.'
            elif self.playerChoice ==3:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[5]
            else:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[8]
        elif self.computerChoice == 3:
            if self.playerChoice ==0:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[0]
            elif self.playerChoice ==1:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[6]
            elif self.playerChoice ==2:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[5]
            elif self.playerChoice ==3:
                self.result = 2
                self.tie = self.tie + 1
                self.realCondition = self.condition[10]+'Lizard.'
            else:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[7]
        else:
            if self.playerChoice ==0:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[9]
            elif self.playerChoice ==1:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[2]
            elif self.playerChoice ==2:
                self.result = 0
                self.playerLose = self.playerLose + 1
                self.realCondition = ' loses, because '+self.condition[8]
            elif self.playerChoice ==3:
                self.result = 1
                self.playerWin = self.playerWin + 1
                self.realCondition = ' wins, because '+self.condition[7]
            else:
                self.result = 2
                self.tie = self.tie + 1
                self.realCondition = self.condition[10]+'Spock.'
                

