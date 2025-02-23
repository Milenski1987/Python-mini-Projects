from random import randint
from time import sleep


def choose_difficulty() -> int:
    number_limit = 0
    while True: # user can choose difficulty of the game
        print("Choose difficulty")
        sleep(1)
        print("Easy: Number range 1 - 100")
        sleep(0.5)
        print("Medium: Number range 1 - 500")
        sleep(0.5)
        print("Hard: Number range 1 - 1000")
        sleep(0.5)
        difficulty = input("Please select Easy, Medium or Hard: ")

        if difficulty == "Easy":
            number_limit = 100
            break
        elif difficulty == "Medium":
            number_limit = 500
            break
        elif difficulty == "Hard":
            number_limit = 1000
            break
        else:
            print("Invalid selection. Try again...")
    return number_limit


def choose_number_of_tries() -> int:
    number_of_tries = 0
    while True:  # user can choose number of tries
        how_many_tries = input("How many tries you want?: ")
        if how_many_tries.isdigit() and int(how_many_tries) > 0:
            number_of_tries = int(how_many_tries)
            break
        else:
            print("Invalid input. Try again...")
    return number_of_tries


def main():
    print("Wellcome to Guess a Number mini game. Try to guess a random number between 1 and 100 in 10 tries")
    sleep(1)
    max_number_based_on_difficulty = choose_difficulty()
    tries = choose_number_of_tries()

    tries_count = 0
    number_to_guess = randint(1, max_number_based_on_difficulty) #computer set random number


    while tries_count < tries:
        players_guess = input(f"Guess the number from 1 to {max_number_based_on_difficulty}: ") #read player's guess

        if int(players_guess) not in range(1, max_number_based_on_difficulty + 1): #check player's guess for range of input
            print("Your number is out of range.")
            continue

        elif not players_guess.isdigit(): #check player's guess for type of input
            print("Invalid input! Try again...")
            continue

        players_guess = int(players_guess)

        if players_guess == number_to_guess:
            print("You guess it and won the game!")
            break

        elif players_guess > number_to_guess:
            print("Your number is higher!")

        elif players_guess < number_to_guess:
            print("Your number is lower!")

        tries_count += 1

    else:
        print("Sorry, no more tries. You lost")


main()
