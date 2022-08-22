![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

![Hm logo](favicon.ico)

# PP3 - Hangman in Python

-----
## About


Hangman is a Python3 Command Line application. It's a guessing game where the User tries to guess a random  word in a certain number of guesses.

The last update to this file was: **August 22, 2022**

[You can find the live project here](https://hangman-py.herokuapp.com/)

-----
## Responsiveness


<details><summary>Am i responsive?</summary>

![Am i responsive](readme_images/Am_i_responsive.webp)
</details>

-----
## How to use the App


[Hangman game wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

-----
## Features


<details><summary>Main menu</summary>

- The main menu is displayed when the application starts. Simple an easy to to understand: 1. New user registration  , 2. User login , 3. Exit.

![main menu](readme_images/main_menu.webp)

- Validation message if user enters other that 1,2 or 3.

![main menu validation](readme_images/main_menu_validation.webp)
</details>

<details><summary>Registration </summary>

- User is prompted to enter username and password that meets the requirements.
![registration prompt](readme_images/registation_prompt.webp)

- Validation message appears if invalid input is entered.
![registration validation](readme_images/register_validation.webp)

- Validation for username already taken.

![username already taken](readme_images/username_already_taken.webp)

- User details stored in  local CSV file.

![csv file](readme_images/details_db.webp)


</details>

<details><summary>Login</summary>

- The user is prompted to enter his/her login credentials.
![login](readme_images/successful-login.webp)

- User credentials validation

![login validation](readme_images/invalid_login.webp)

</details>

<details><summary>Game menu</summary>

- The user is prompted if he/she wants to play of to quit.

![game menu](readme_images/game_menu.webp)

- Validation message

![validation message](readme_images/game_menu_validation.webp)

</details>

<details><summary>Hangman game</summary>

- Features: random word, validates right input, live counting, display already guessed words, graphics.

![hangman screenshot](readme_images/hangman.webp)

</details>

-----
## Design

<details><summary>Flow charts</summary>

- ![application flow chart](readme_images/app_flowchart.webp)
- ![game flow chart](readme_images/game_flowchart.webp)

</details>

-----
## Technologies


<details><summary>Languages, External Libraries and Programs Used</summary>

- [Python 3](https://www.python.org/)
  - High level language used to build this project version 3.8.11
- [Random](https://docs.python.org/3/library/random.html?highlight=random%20choice#random.choice)
  - Return a random element from the non-empty sequence.
- [String](https://docs.python.org/3/library/string.html?highlight=string#module-string)
  - The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
- [Time](https://docs.python.org/3/library/time.html?highlight=time%20sleep#time.sleep)
  - From time this app uses sleep to pause between screens.
- [Csv](https://docs.python.org/3/library/csv.html?highlight=csv)
  - Comma Separated values file reading and writing.
- [Sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys)
  - System-specific parameters and functions.
- [Github](https://github.com/)
  - GitHub is the site used to store the source code for the Website.
- [Git](https://git-scm.com/)
  - Git is the  version control software used to commit and push code to the GitHub repository where the source code is stored.
- [Visual Studio Code](https://code.visualstudio.com/)
  - VS Code for short is the integrated development environment (IDE) software used to build the website.
- [Lucidchart](https://www.lucidchart.com/pages/)
  - Lucidchart was used to create a flowchart of the project.
- [Heroku](https://id.heroku.com)
  - Used to deploy the application and provides an environment where the code can be executed.

</details>

-----
## Testing


[PEP8 validator online check](http://pep8online.com/checkresult)
<details>
<summary> Result for run.py</summary>

- ![PEP8_run.py](readme_images/Pep8_run.py.webp)    
</details>

<details><summary>Testing table</summary>

- ![testing table](readme_images/test_table1.webp)
- ![testing table](readme_images/test_table2.webp)
</details>

-----
## Deployment

-----
### How to deploy to Heroku

<details>

<summary>Steps taken to deploy</summary>

- Create an account if necessary and log in.

- Once in the [Heroku](https://id.heroku.com) dashboard, click on New dropdown menu button (top right side) and Create new App.

- On the Create New App page, enter a name for the application and select your region. Then click Create app.

- You will then be brought to the Application Configuration page for your new app.

- Scroll down the Settings page to Buildpacks:
  - Click Add buildpack, select Python from the pop up window and click on Save changes.
  - Click Add buildpack again, select Node.js click on Save changes. It is important that is done in that order Python first, then Node.js beneath.
  - ![heroku settings](readme_images/Heroku_settings.webp)
- Click on the Deploy tab on the Application Configuration page.
  - Select GitHub as the Deployment Method.
  - Enter your Github username and your Github repository name (in this case https://github.com/JoseMGuerra/hangman) and click on Connect to link up the Heroku app to the GitHub repository code.

- Scroll down the page and there are to options, either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Automatic Deploy was selected.

- The application can be run by clicking on the Open App button at the top of the Application Configuration page.

- The live link for this project is (https://hangman-py.herokuapp.com/)

</details>

-----
## Resources / Credits / Inspiration



- [Python documentation](https://docs.python.org/3/)
- [W3Schools documentation](https://www.w3schools.com/python/default.asp)
- [Love sandwiches project](https://food-market-stock.herokuapp.com/)

-----
## Acknowledgments

- Thank you to my mentor Brian Macharia for guiding me and for his invaluable advice.

-----
## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!