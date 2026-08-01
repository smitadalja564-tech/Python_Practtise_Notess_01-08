#MINI PROJECT ROCK,PAPER,SCISSOR GAME
import random
game_list = ["ROCK",'PAPER','SCISSOR']
menu = """
                GAME MENU 
                TYPE "ROCK" FOR ROCK
                TYPE "PAPER" FOR PAPER
                TYPE "SCISSOR" FOR SCISSOR
"""
status = True
while status:
    print(menu)
    user_ch = input("Enter Your Choice : ").upper()
    com_ch = random.choice(game_list)

    print("Computer Choice :: ",com_ch)
    print("User Choice :: ",user_ch)

    if com_ch == "ROCK" and user_ch == "PAPER" or com_ch == "PAPER" and user_ch == "SCISSOR" or com_ch == "SCISSOR" and user_ch == "ROCK":
        print("**** USER WON THIS MATCH ***")
    elif com_ch == "PAPER" and user_ch == "ROCK" or com_ch == "SCISSOR" and user_ch == "PAPER" or com_ch == "ROCK" and user_ch == "SCISSOR":
        print("**** COMPUTER WON THIS MATCH ****")
    else : 
        print("**** TIE ******")
    
    choice = input("Do You Want To Play Again This Game , Press 'y' For YES & Press 'n' For No : ")
    if choice == 'y' or choice == 'YES'.upper():
        status = True
    else:
        status = False
