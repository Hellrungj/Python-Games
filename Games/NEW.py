import random

def Rock(otherinput):
    if otherinput == "Rock":
        print "Tie"
    elif otherinput == "Paper":
        print "Player 2 Wins"
    elif otherinput == "Scissors":
        print "Player 1 Wins"
    elif otherinput == "Lizard":
        print "Player 1 Wins"
    elif otherinput == "Spock":
        print "Player 2 Wins"
    else:
        print "Error"
def Paper(otherinput):
    if otherinput == "Rock":
        print "Player 1 Wins"
    elif otherinput == "Paper":
         print "Tie"
    elif otherinput == "Scissors":
        print "Player 2 Wins"
    elif otherinput == "Lizard":
        print "Player 2 Wins"
    elif otherinput == "Spock":
        print "Player 1 Wins"
    else:
        print "Error"
def Scissors(otherinput):
    if otherinput == "Rock":
        print "Player 2 Wins"
    elif otherinput == "Paper":
        print "Player 1 Wins"
    elif otherinput == "Scissors":
        print "Tie"
    elif otherinput == "Lizard":
        print "Player 1 Wins"
    elif otherinput == "Spock":
        print "Player 2 Wins"
    else:
        print "Error"
def Lizard(otherinput):
    if otherinput == "Rock":
        print "Player 2 Wins"
    elif otherinput == "Paper":
        print "Player 1 Wins"
    elif otherinput == "Scissors":
        print "Player 2 Wins"
    elif otherinput == "Lizard":
         print "Tie"
    elif otherinput == "Spock":
        print "Player 1 Wins"
    else:
        print "Error"
def Spock(otherinput): 
    if otherinput == "Rock":
        print "Player 1 Wins"
    elif otherinput == "Paper":
        print "Player 2 Wins"
    elif otherinput == "Scissors":
        print "Player 1 Wins"
    elif otherinput == "Lizard":
        print "Player 2 Wins"
    elif otherinput == "Spock":
        print "Tie"
    else:
        print "Error"
#===============================================================================
def Computer_vsUser():
    """"""
    UserChoice = raw_input("pick Rock, Paper, Scissors, Lizard, Spock")
    ComputerChoice = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
    if UserChoice == "Rock":
        Rock(ComputerChoice)
    elif UserChoice == "Paper":
        Paper(ComputerChoice)
    elif UserChoice == "Scissors":
        Scissors(ComputerChoice)
    elif UserChoice == "Lizard":
        Lizard(ComputerChoice)
    elif UserChoice == "Spock":
        Spock(ComputerChoice)
    else:
        print "Error"
def User_vsUser():
    """"""
    User1Choice = raw_input("player 1 pick Rock, Paper, Scissors, Lizard, Spock")
    User2Choice = raw_input("player 2 pick Rock, Paper, Scissors, Lizard, Spock")
    if User1Choice == "Rock":
        Rock(User2Choice)
    elif User1Choice == "Paper":
        Paper(User2Choice)
    elif User1Choice == "Scissors":
        Scissors(User2Choice)
    elif User1Choice == "Lizard":
        Lizard(User2Choice)
    elif User1Choice == "Spock":
        Spock(User2Choice)
    else:
        print "Error"
#===============================================================================    
def Promted():
    """"""
    userchoice = raw_input("do you want to play with the computer or the another user.(computer or user)")
    if userchoice == "computer":
        Computer_vsUser()
    elif userchoice == "user":
        User_vsUser()
    else:
        print "Error"
#--------------------------------------------------------------------------------
def main():
    """Main function"""
    UserInput = raw_input("How are you?")
    if UserInput != "bad".lower: 
        print("Great, I feel the same.")
        UserInput2 = raw_input("Do you want to play Rock, Paper, Scissors.")
        Mood = "Great"
    else:
        print("Well, thats unfortunate.")
        UserInput2 = raw_input("How about a game of Rock, Paper, Scissors.")
        Mood = "Bad"
    if UserInput2 == "yes":
        Promted()
    else:
        print("Sorry, hope you have a better day.")
    
if __name__ == '__main__':
    main()