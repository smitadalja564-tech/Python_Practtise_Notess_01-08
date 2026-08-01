"""
                    NUMBER HOISE ::
                        56 78 90 34 2 12 10 34 89 24 22 20
                    Enter  
                    Player 1 : 57 34 2 12 10 20
                    Player 2 : 79 90 34 89 24 22

                    Enter 
                            20

                    Player 1 : 57 34 2 12 10
                    Player 2: 79 90 34 89 24 22
"""
import random

number_hoise = [56,78,90,34,2,12,10,34,89,24,22,20]
user_ch_n1 = [56,34,2,12,20,10]
user_ch_n2 = [78,90,34,89,24,22]

status = True

while status:
    cam_ch_n = random.choice(number_hoise)

    print(f"Player1 : {user_ch_n1}")
    print(f"Player2 : {user_ch_n2}")
    print(f"Number Call : {cam_ch_n}")

    if cam_ch_n in user_ch_n1:  
        user_ch_n1.remove(cam_ch_n)
        print(f"Playr1 match ! upadte the number : {user_ch_n1}")
    elif cam_ch_n in user_ch_n2:
        user_ch_n2.remove(cam_ch_n)
        print(f"Playr2 match ! upadte the number : {user_ch_n2}")
    else:
        print("don't found the number")

    print("\n")
    if len(user_ch_n1) == 0:
        print("*** Player1 WON THIS MATCH ***")
        break
    elif len(user_ch_n2) == 0:
        print("*** Player2 WON THIS MATCH ***")
        break
    else:
        print("*** TIE THIS MATCH ***")

    choice = input("Do You Want To Play Again This Game , Press 'y' For YES & Press 'n' For No : ")
    if choice == 'y':
        status = True
    else:
        status = False
