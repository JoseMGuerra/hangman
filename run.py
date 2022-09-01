""" Hangman game with Google sheet API - v.1 """


# Imported libraries and modules
import random
import string
import sys
import time
import gspread
from google.oauth2.service_account import Credentials
from headers import print_header
from hangman_pics import hangman_pics
from words import WORDS

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman_users')
worksheet = SHEET.worksheet("details")


def get_random_word(WORDS):
    """ Get a a word from a word list.
    :param: WORDS - words form module words.py
    :return: word.upper()

    Function to generate a random word from a word list.
    """
    word = random.choice(WORDS)

    word = random.choice(WORDS)
    return word.upper()


def quit():
    """ Helper function to exit the application.

    Invokes sys.exit().
    """
    sys.exit()


def clear():
    """ Clear the screen

    Function to clear the clear.

    Invokes print('\\033c').
    """
    print('\033c')


def space():
    """ Prints an empty line.

    Function to creates empty lines for better readability.

    Invokes  print("").
    """
    print("")


def pause(seconds):
    """ Pause the screen for nth seconds.
    :param: seconds - time in seconds.

    Function to pause screen for better user experience.
    Invokes "time.sleep(s)"
    """
    time.sleep(seconds)


def register():
    """ Get username and password inputs from the user.

    Invokes username_valid function passing username input.
    Invokes password_valid function passing password input.
    Invokes is_username_taken function passing username input.

    If all validations has passed:
    Invokes save_inputs function
    passing username and password.
    """
    clear()
    print_header("register")
    space()
    space()
    print(" Type 'menu' to Main Menu")
    space()
    while True:
        # takes user inputs
        username = get_user_input(
            " min 4 characters alphanumeric\n\nEnter you username: \n").title()
        password = get_user_input("""
        min 4 characters
        max 10 characters
        at least 1 UPPERCASE
        at least 1 lowercase
        at least 1 symbol ! @ $ % #
        \nEnter password: """)

        if not username_valid(username):
            print(" ### Invalid  Username !! ###\n")
            continue

        if not (password_valid(password)):
            print(" ### Invalid Password !! ###\n")
            continue
        try:
            if is_username_taken(username):
                space()
                print(" ### Sorry username already taken. ###")
                space()
                pause(1.5)
                continue
        except FileNotFoundError:
            print(FileNotFoundError())

        save_inputs(username, password)
        space()
        print(" Valid username and password.")
        pause(1.1)
        space()
        print(" Registering your details....")
        pause(1.1)
        space()
        print(" Please wait...")
        pause(1.5)
        space()
        print(" Registration completed successfully.")
        pause(1.1)
        space()
        main_menu()
        break


def get_user_input(message):
    """" Get user input.

    :param: message - message changes upon inputs.
    :return: user_input

    Function that sets a general rule for user inputs.
    Allows the user to go to main menu by typing 'menu'
    or to quit by typing 'quit'.
    """
    user_input = input(message + "\n").strip()

    if user_input == "menu":
        main_menu()

    elif user_input == "quit":
        quit()

    return user_input


def username_valid(username):
    """ Function to validate the username input.

    :param: username - from user registration input.
    :return: bool - True if passes validation.

    Function that validates username input.

    I MUST contain:

    Alphanumeric characters.
    Be at least 4 characters long.
    """
    valid = True

    if len(username) < 4:
        print(" length should be at least 4")
        valid = False
    if not any(char.isalpha() for char in username):
        print(" Username should be alphanumeric")
        valid = False

    return valid


def password_valid(password):
    """ Function to validate user password input.

    :param: password - from user registration input.
    :return: bool - True passes validation.

    Function that validates password input.

    It Must contain:

    1 special character.
    1 digit.
    1 UPPERCASE.
    1 lowercase.
    Be at least 4 characters long.
    No more than 10 characters long.

    """

    SP_CHAR = ["!", "@", "$", "%", "#"]

    valid = True

    if len(password) < 4:
        print(" length should be at least 4")
        valid = False

    if len(password) > 10:
        print(" length should be not be greater than 10")
        valid = False

    if not any(char.isdigit() for char in password):
        print(" Password should have at least one digit")
        valid = False

    if not any(char.isupper() for char in password):
        print(" Password should have at least one UPPERCASE letter")
        valid = False

    if not any(char.islower() for char in password):
        print(" Password should have at least one lowercase letter")
        valid = False

    if not any(char in SP_CHAR for char in password):
        print(" Password should have at least one of the symbols ! @ $ % #")
        valid = False

    return valid


def is_username_taken(username):
    """ validates if username if already taken.

    :param: username - from user registration input.
    :return: bool - True if username is taken.

    Function to get username values from details worksheet.
    Compare user input with database and return a bool.
    """

    username_list = worksheet.col_values(1)

    return username in username_list


def save_inputs(username, password):
    """
    Append user inputs to worksheet.

    :param: username - from user registration input.
    :param: password - from user registration input.

    Function to save user inputs to google sheet API worksheet.
    """
    data = [username, password]
    worksheet.append_row(data)


def login():
    """ Get user inputs to grant access to the application.

    Function to get user inputs and compare them with the user
    registration database.
    If the input are correct: access is granted.
    Otherwise access is denied.
    """
    clear()
    print_header("login")
    space()
    print(" Please enter Username and Password")
    space()
    print(" OR type 'menu' to go to Main Menu")
    access_granted = False

    while not access_granted:
        space()
        username = get_user_input(" Enter your username: \n").title()
        password = get_user_input(" Enter your password: \n")

        try:
            username_list = worksheet.col_values(1)
            password_list = worksheet.col_values(2)

            if username in username_list and password in password_list:
                access_granted = True
                space()
                print(" Access granted.")
                pause(2.1)
                space()
                print(f" Welcome {username}!")
                pause(2.1)
                space()
                print(" You are being redirected to our game menu...")
                space()
                pause(2.1)
                print(" Please wait...")
                space()
                pause(2.1)
                game_menu(username)
            else:
                access_granted = False
                if username not in username_list:
                    print(" ### Wrong username ###")
                if password not in password_list:
                    print(" ### Wrong password ###")
                continue

        except FileNotFoundError:

            print(" Please, register if you haven't.")
            space()
            print(" OR type 'menu' to go to Main Menu")
            print(FileNotFoundError())


def game_menu(username):
    """ Game menu with user choices.

    :param: username - used to format text.

    Function that get user input, prompting user to chose between:

    1. Play
    2. Quit
    3. Go to Main Menu
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
        choice = get_user_input(" What would you like to do? \n")
        space()
        if choice == "" or choice == " ":
            print(" Please select one Option")
            pause(10)
            continue
        if choice == "1":
            print(f" Excellent {username} , let's play!")
            space()
            print(" Loading the game...")
            pause(1.1)
            space()
            pause(1.1)
            print(" Please wait...")
            pause(2.1)
            play(username)
        if choice == "2":
            pause(1)
            print(f" Goodbye {username}, have a nice day!")
            space()
            pause(2.5)
            clear()
            quit()
        if choice == "3":
            main_menu()


def play(username):
    """ Hangman game logic.

    :param: username - used to format text.

    Function to get a random word from a word bank.
    Set a secret word that the user has to guess.
    The user has 7 lives/attempts to guess the secret word.
    Already guessed letters and a graphic are displayed.
    While number of lives > 0 or the word is guessed the game will loop.

    Invoke play_again function after every iteration.
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
        print(" You have used these letters: ", " ".join(
            guessed_letters))  # print used letters
        space()
        print(f" You have {lives} lives left.")  # print live left

        # what secret word is ( ie S_CR_T)
        word_list = [
            letter if letter in guessed_letters else "_" for letter in word]
        print(hangman_pics[lives])
        space()
        print(" Secret word: ", " ".join(word_list))

        # transform to uppercase so all letters have the same ascii value
        # getting  user guesses
        space()
        user_letter = get_user_input(" Guess a letter: \n").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in secret_word:
                secret_word.remove(user_letter)
            else:
                lives = lives - 1  # takes away a live

        elif user_letter in guessed_letters:  # check if user already
            # guessed a letter
            space()
            print(" You have already used that letter, try another one.")

        else:
            space()
            print(" Invalid character, Please try again.")

    # when len(secret_word) == 0 OR when lives ==0 ->
    if lives == 0:
        clear()
        print(hangman_pics[lives])
        space()
        print(f" Sorry, you just died!. The word was {word}")
        play_again(username)  # play again
    else:
        space()
        print(f" Congratulations!!. You nailed {username}!!")
        space()
        print(f" The word is: {word}")
        play_again(username)


def play_again(username):
    """ Get user input whether the user wants to play again or not.

    :param: username - used to format text.

    Function to get user input asking for Yes or No and
    invoking the correct function depending on user response.
    """
    space()
    another_round = get_user_input(" Would you like to play again : Y / N \n")\
        .upper()
    if another_round == "y" or another_round == "Y":
        play(username)
    else:
        clear()
        space()
        print(f" Thank you for playing, have a nice day {username}!")
        space()
        pause(1.5)
        clear()
        quit()


def main_menu():
    """ Main menu with user choices.

    1. To invoke 'register' function.
    2. To invoke 'login' function.
    3. To invoke 'quit' function.

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
        print(" Goodbye, have a good day!")
        space()
        pause(2.5)
        clear()
        quit()
    else:
        print(" Sorry, I didn't understand that. Please try again.")
        pause(2)
        clear()
        main_menu()


if __name__ == "__main__":
    main_menu()
