# Imported modules
import sys
import time
import csv

DETAILS_FILE_PATH = "assets/py/user_details.csv"


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
    clear()
    # game_menu_header()  # prints the game menu header

    print("""

        1. Press 1 to play
        2. Press 2 to Quit

    """)
    choice = input(f"What would you like to do? ").strip()
    space()

    if choice == "1":
        print(f"Excellent {username} , let's play!")
        space()
        print("Loading the game...")
        pause(1.1)
        space()
        pause(1.1)
        print("Please wait...")
        pause(2.1)
        # play(username)
    elif choice == "2":
        pause(1)
        print(f"Goodbye {username}, have a nice day!")
        quit()
    else:
        print("Enter a valid choice.")  # validates user choice

def register():
    """
    Get username and password input from the user, validates user inputs.
    add user to user_details file or creates new file if it doesn't exits.

    """
    clear()
    # register_header()
    space()
    # open the file where users details will be appended or creates a new file if it doesn't exits
    with open(DETAILS_FILE_PATH, "a", newline="") as f:
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
            break
        else:  # TODO -> DOESN'T VALIDATE PROPERLY, Y GOES BACK TO MAIN MENU ????
            print(
                "Username MUST be at least 4 characters and Password MUST contain '#' key .")


def login():
    """
    Get and Validates user login details
    """
    clear()
    # login_header()
    space()
    print("Please enter Username and Password")
    space()
    access_granted = False

    while access_granted == False:
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

            if access_granted == False:
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
                # game_menu(username)


def main_menu():
    """
    Main menu, register and login.
    """
    # main_menu_header()
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
