""" Hangman App """
import random
import string
import sys
import time
import csv
from headers import print_header
from hangman_pics import hangman_pics
from words import WORDS

DETAILS_FILE_PATH = "/workspace/hangman/assets/user_details.csv"


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


def pause(seconds):
    """
    Pause the screen for nth seconds
    better user experience
    "time.sleep(s)"
    """
    time.sleep(seconds)


def register():
    """
    Get username and password input from the user, validates user inputs.
    add user to user_details file or creates new file if it doesn't exits.

    """
    clear()
    print_header("register")
    space()
    space()
    print("Type 'menu' to Main Menu")
    space()
    while True:
        # takes user inputs
        username = get_user_input(
            "min 4 characters alphanumeric\n\nEnter you username: \n").title()
        password = get_user_input("""
        min 4 characters
        max 10 characters
        at least 1 UPPERCASE
        at least 1 lowercase
        at least 1 symbol ! @ $ % #
        \nEnter password: """)

        if not username_valid(username):
            print("### Invalid  Username !! ###\n")
            continue

        if not password_valid(password):
            print("### Invalid Password !! ###\n")
            continue

        try:
            if username_exists(username):
                space()
                print("### Sorry username already taken. ###")
                space()
                pause(1.5)
                continue
        except FileNotFoundError:
            print(FileNotFoundError())

        save_inputs(username, password)
        space()
        print("Valid username and password.")
        pause(1.1)
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
        main_menu()
        break


def get_user_input(message):
    """"
    get user inputs
    """
    user_input = input(message + "\n").strip()

    if user_input == "menu":
        main_menu()

    elif user_input == "quit":
        quit()

    return user_input


def username_valid(username):
    """
    Function to validate the username
    """
    valid = True

    if len(username) < 4:
        print("length should be at least 4")
        valid = False
    if not any(char.isalpha() for char in username):
        print("Username should be alphanumeric")
        valid = False

    return valid


def password_valid(password):
    """
    Function to validate the password
    """

    SPECIAL_CHARACTER = ["!", "@", "$", "%", "#"]

    valid = True

    if len(password) < 4:
        print("length should be at least 4")
        valid = False

    if len(password) > 10:
        print("length should be not be greater than 10")
        valid = False

    if not any(char.isdigit() for char in password):
        print("Password should have at least one digit")
        valid = False

    if not any(char.isupper() for char in password):
        print("Password should have at least one UPPERCASE letter")
        valid = False

    if not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter")
        valid = False

    if not any(char in SPECIAL_CHARACTER for char in password):
        print("Password should have at least one of the symbols ! @ $ % #")
        valid = False

    return valid


def username_exists(username):
    """ validates if username if already taken. """
    usernames = []

    with open(DETAILS_FILE_PATH) as f:

        reader = csv.reader(f, delimiter=",")
        next(reader)

        for row in reader:
            for _ in row:
                usernames.append(row[0])

        return username in usernames


def save_inputs(username, password):
    """
    open the file where users inputs will be appended
    creates a new file if it doesn't exists
    save user inputs to file
    """
    try:
        with open(DETAILS_FILE_PATH, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([username, password])

    except FileNotFoundError:
        print(FileNotFoundError())


def login():
    """
    Get and Validates user login details
    """
    clear()
    print_header("login")
    space()
    print("Please enter Username and Password")
    space()
    print("OR type 'menu' to Main Menu")
    access_granted = False

    while not access_granted:
        space()
        username = get_user_input("Enter your username: \n").title()
        password = get_user_input("Enter your password: \n")

        try:
            with open(DETAILS_FILE_PATH, "r") as file:

                reader = csv.reader(file)

                for row in reader:
                    for cell in row:
                        # username and password provided are valid
                        if cell == username and row[1] == password:
                            access_granted = True
                        else:
                            break
        except FileNotFoundError:
            print("Please, register if you haven't.")
            space()
            print("OR type 'menu' to go to Main Menu")
            print(FileNotFoundError())

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
        1. Press 1 to Play

        2. Press 2 to Quit

        3. Press 3 to Main Menu
        """)
        space()
        choice = get_user_input("What would you like to do? \n")
        space()
        if choice == "" or choice == " ":
            print("Please select one Option")
            pause(10)
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
        if choice == "3":
            main_menu()


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
        user_letter = get_user_input("Guess a letter: \n").upper()

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
    another_round = get_user_input("Would you like to play again : Y / N \n")\
        .upper()
    if another_round == "y" or another_round == "Y":
        play(username)
    else:
        clear()
        space()
        print(f"Thank you for playing, have a nice day {username}!")
        space()
        pause(1.5)
        clear()
        quit()


def main_menu():
    """
    Main menu, register and login.
    """
    clear()
    print_header("main")
    space()
    choice = get_user_input("""
    1. Press 1 to Register

    2. Press 2 to Login

    3. Press 3 to Quit

    \n""")

    space()

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
        main_menu()


if __name__ == "__main__":
    main_menu()
