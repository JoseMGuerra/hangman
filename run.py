# Imported modules
from headers import print_header
from hangman_pics import hangman_pics
from words import WORDS
import random
import string
import sys
import time
import csv

DETAILS_FILE_PATH = "assets/py/user_details.csv"


def get_random_word(WORDS):
    """ Chose a word randomly from the WORDS module """
    word = random.choice(WORDS)

    word = random.choice(WORDS)
    return word.upper()


def quit():
    """
    Helper function to exit the game
    "sys.exit()"
    """
    sys.exit()


def clear():
    """
    Clear the screen
    "print('\\033c')"
    """
    print('\033c')


def space():
    """
    Prints an empty line
    "print("")"
    """
    print("")


def pause(s):
    """
    Pause the screen for nth seconds
    better user experience
    "time.sleep(s)"
    """
    time.sleep(s)


def game_menu(username):
    """
    Game menu where user choices to play or quit the game
    """
    choice = ""
    while True:
        clear()
        print_header("game_menu")
        space()
        print("""
        1. Press 1 to play

        2. Press 2 to Quit
        """)
        space()
        choice = input("What would you like to do? ").strip()
        space()
        if choice == "" or choice == " ":
            print("Try selecting 1 OR 2")
            pause(2)
            continue
        if choice == "1":
            print(f"Excellent {username} , let's play!")
            space()
            print("Loading the game...")
            pause(1.1)
            space()
            pause(1.1)
            print("Please wait...")
            pause(2.1)
            play(username)
        if choice == "2":
            pause(1)
            print(f"Goodbye {username}, have a nice day!")
            space()
            pause(2.5)
            clear()
            quit()


def play(username):
    """
    Game logic function, get a random word and set a secret word
    Add guessed letters to a set so it only displays it just once
    While number of lives > 0 or the word is guessed  will loop.
    """
    clear()
    print_header("hangman")  # prints the hangman header

    word = get_random_word(WORDS)
    alphabet = set(string.ascii_uppercase)

    print(word)  # SECRET WORD### delete THIS ##########******************

    secret_word = set(word)  # letters in the secret word
    guessed_letters = set()  # list of non repeated letters\
    # the user has guessed

    lives = 7  # while loop flag

    while len(secret_word) > 0 and lives > 0:
        space()
        print("You have used these letters: ", " ".join(
            guessed_letters))  # print used letters
        space()
        print(f"You have {lives} lives left.")  # print live left

        # what secret word is ( ie S_CR_T)
        word_list = [
            letter if letter in guessed_letters else "_" for letter in word]
        print(hangman_pics[lives])
        space()
        print("Secret word: ", " ".join(word_list))

        # transform to uppercase so all letters have the same ascii value
        # getting  user guesses
        space()
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in secret_word:
                secret_word.remove(user_letter)
            else:
                lives = lives - 1  # takes away a live

        elif user_letter in guessed_letters:  # check if user already
            # guessed a letter
            space()
            print("You have already used that letter, try another one.")

        else:
            space()
            print("Invalid character, Please try again.")

    # when len(secret_word) == 0 OR when lives ==0 ->
    if lives == 0:
        clear()
        print(hangman_pics[lives])
        space()
        print(f"Sorry, you just died!. The word was {word}")
        play_again(username)  # play again
    else:
        space()
        print(f"Congratulations!!. You nailed {username}!!")
        space()
        print(f"The word is: {word}")
        play_again(username)


def play_again(username):
    """
    Prompt user if would like to play another round
    """
    space()
    another_round = input(
        "Would you like to play again : Y / N ").upper()
    if another_round == "y" or another_round == "Y":
        play(username)
    else:
        clear()
        space()
        print(f"Thank you for playing, have a nice day {username}!")
        space()
        pause(1.1)
        quit()


def register():
    """
    Get username and password input from the user, validates user inputs.
    add user to user_details file or creates new file if it doesn't exits.

    """
    clear()
    print_header("register")
    space()
    while True:
        # takes user inputs
        username = str(
            input("(min 4 characters alphanumeric)\n\nEnter you username:")).strip().title()
        space()
        password = str(
            input("(MUST contain '!')\n\nEnter password: ")).strip()

        # validates if username if already taken.
        usernames = []
        with open(DETAILS_FILE_PATH) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                for field in row:
                    usernames.append(row[0])
        if username in usernames:
            space()
            print("### Sorry username already taken. ###")
            space()
            pause(1.5)
            continue

        # open the file where users details will be appended\n
        #  or creates a new file if it doesn't exits
        with open(DETAILS_FILE_PATH, "a", newline="") as f:
            writer = csv.writer(f)

            if len(username) < 4 and not username.isalpha() or "!" not in password:
                print("Input not valid, please try again.")
                continue

            space()
            print("valid username and password.")
            pause(1.1)

            writer.writerow([username, password])  # write user details to file
            space()
            print("Registering your details....")
            pause(1.1)
            space()
            print("Please wait...")
            pause(1.5)
            space()
            print("Registration completed successfully.")
            pause(1.1)
            space()
            break


def login():
    """
    Get and Validates user login details
    """
    clear()
    print_header("login")
    space()
    print("Please enter Username and Password")
    space()
    access_granted = False

    while access_granted is False:
        with open(DETAILS_FILE_PATH, "r") as f:
            space()

            username = input("Enter your username: ").strip().title()
            password = input("Enter your password: ").strip()

            reader = csv.reader(f)

            for row in reader:
                for cell in row:

                    if cell == username and row[1] == password:
                        access_granted = True
                    else:
                        break

            if access_granted is False:
                print("Wrong username or password, please try again")
            else:
                space()
                print("Access granted.")
                pause(2.1)
                space()
                print(f"Welcome {username}!")
                pause(2.1)
                space()
                print("You are being redirected to our game menu...")
                space()
                pause(2.1)
                print("Please wait...")
                space()
                pause(2.1)
                game_menu(username)


def main_menu():
    """
    Main menu, register and login.
    """
    choice = ""
    while choice != "3":
        clear()
        print_header("main")
        space()
        print("""
    1. Press 1 to Register

    2. Press 2 to Login

    3. Press 3 to Quit
    """)
        space()
        choice = input()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            pause(1)
            print("Goodbye, have a good day!")
            space()
            pause(2.5)
            clear()
            quit()
        else:
            print("Sorry, I didn't understand that. Please try again.")
            pause(2)
            clear()


if __name__ == "__main__":
    main_menu()
