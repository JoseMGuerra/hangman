# Imported modules
import sys
import time

FILE_PATH = "assets/py/user_details.csv"


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


def register():
    """
    Get username and password input from the user, validates user inputs.
    add user to user_details file or creates new file if it doesn't exits.

    """
    pass


def login():
    """
    Get and Validates user login details
    """
    pass


def main_menu():
    """
    Main menu, register and login.
    """
    choice = ""
    while choice != "3":
        print("""
        1. Press 1 to Register
        2. Press 2 to Login
        3. Press 3 to Quit
        """)
        choice = input()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            quit()
        else:
            print("Sorry, that's not a valid option. Please try again.")


if __name__ == "__main__":
    main_menu()
