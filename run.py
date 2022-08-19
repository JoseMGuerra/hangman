# Imported modules
import sys
import time
import csv

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
    clear()
    space()
    # open the file where users details will be appended or creates a new file if it doesn't exits
    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)

        # takes user inputs
        username = str(input("Enter you username: ")).strip().title()
        password = str(input("Enter password: ")).strip()

        while len(username) >= 4 and "#" in password:
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
            # print("Please restart the program for changes to take effect.")
            # space()
            # quit()
            break
        else:  # TODO -> DOESN'T VALIDATE PROPERLY, Y GOES BACK TO MAIN MENU ????
            print(
                "Username MUST be at least 4 characters and Password MUST contain '#' key .")


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
