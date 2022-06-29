import random
import sys
attempts_list = []

name = input("enter the name of player: ")
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's your turn to choose number!!!!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello", name ," Welcome to the number guessing game !")
    wanna_play = input("Would you like to play the guessing game? (Enter Yes/No) ")
    #Where the show_score function USED to be
    attempts = 0 #initiating attempts = 0
    show_score()
    
    while wanna_play.lower() == "yes":
        if attempts < 6:  #controling attempts
            try:
                guess = input("Pick a number between 1 and 10: ")
                if int(guess) < 1 or int(guess) > 10:
                    raise ValueError("Please guess a number within the given range: ")
                if int(guess) == random_number:
                    print("Nice! You got it!")
                    attempts += 1
                    attempts_list.append(attempts)
                    print("You got right guessing in {} attempts".format(attempts))
                    play_again = input("Would you like to play again? (Enter Yes/No): ")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))
                    if play_again.lower() == "no":
                        print("That's cool, Good bye!!")
                        break
                elif int(guess) > random_number:
                    print("Your guess is higher then the number")
                    attempts += 1
                elif int(guess) < random_number:
                    print("Your guess is lower then the number")
                    attempts += 1
                elif attempts == 6:
                    print("out of attempts")
                
            except ValueError as err:
                print("The input number is not a valid number. Try again...")
                print("({})".format(err))
        else:
            print("you are out of attempts.")
            break
            
    else:
        print("That's cool, you don't wanna play this game")
        
       
   
if __name__ == '__main__':
    start_game()
