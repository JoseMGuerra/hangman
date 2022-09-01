# game headers

HEADERS = {
    "main": "MAIN MENU",
    "register": "  REGISTER",
    "login": "  LOGIN",
    "game_menu": "GAME MENU",
    "hangman": "WELCOME TO HANGMAN"
}


def print_header(header):
    """
    prints menu headers
    """
    if header not in HEADERS:
        raise ValueError("Invalid menu option.")
    header_text = HEADERS[header]
    for i in range(12):
        print("*-*", end="")
    print("")
    print(f"""
            {header_text.upper()}
    """)
    for i in range(12):
        print("*-*", end="")
    print("")