#Guess the number from 1 to 10

def chk_int(I):
    try:
        I = int(I)
    except ValueError:
        print("Not a valid input. ")
        return(False)
    else:
        return(True)

def chk_int_in_range(I):
    if chk_int(I) == True:        
        if int(I) in range(1, 11):
            return (True)
        else:
            print("Number not in range.")
            return (False)
    else:
        return(False)


print(" _____                    _____ _          _   _                 _               \n")
print("|  __ \                  |_   _| |        | \ | |               | |              \n")
print("| |  \/_   _  ___  ___ ___ | | | |__   ___|  \| |_   _ _ __ ___ | |__   ___ _ __ \n")
print("| | __| | | |/ _ \/ __/ __|| | | '_ \ / _ \ . ` | | | | '_ ` _ \| '_ \ / _ \ '__|\n")
print("| |_\ \ |_| |  __/\__ \__ \| | | | | |  __/ |\  | |_| | | | | | | |_) |  __/ |   \n")
print(" \____/\__,_|\___||___/___/\_/ |_| |_|\___\_| \_/\__,_|_| |_| |_|_.__/ \___|_|   \n")

import random
repeat = "y"

if input("In this game you have to guess a random number in the range (1 to 10).\nDo you wanna play it? (y or n) ") == "y":
    while repeat == "y":
        secret_num = random.randint(1, 10)
        print(secret_num)
        i = 3
        while i != 0:
            if i == 1:
                guess = input("\nLast chance!\n")
                if chk_int_in_range(guess) == True:    
                    if int(guess) != secret_num:
                        print("Wrong.")
                        i -= 1
                    else:
                        print("You've got it!")
                        i = 0
            else:
                guess = input("\nYou've got " + str(i) +" shots.\n")
                if chk_int_in_range(guess) == True:    
                    if int(guess) != secret_num:
                        print("Wrong.")
                        i -= 1
                    else:
                        print("You've got it!")
                        i = 0

        repeat = input("The number was " + str(secret_num) + ". Would you like to play it again? (y or n) ")
    else:
        print("Closing...")
else:
    print("Exiting...")