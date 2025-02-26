
# Hi, I'm Salle-Njume Brian! 👋

# Python Projects for Beginners
The below are 16 Python projects I took time to work on, with the aim of enhancing my problem-solving skills. You'll see in each how I decomposed the overall solution into smaller-manageable parts(that is seperating variables, functions and control flow , so as to help ease understanding of the reason behind each seperation).
After each project explanation, I displayed the results I got from my end(after execution) to prove the program is working smoothly. 

You'll see clearly as well how I interact with the program but trying as well invalid inputs, to see if my program reacts correctly according to the instructions I gave to it(in the form of Python programming language obvioulsy) to give the same error meassage I placed in my code.

Some of the projects(where most sensible) have their __better form__ modularized/refactored form while some few others have the DRY(Don't repeat yourself) form, aside from their intial-more general program which still runs smoothly when executed.

# Project List
Below is the project list of the projects I'll be explaining, alongside their increasing level of difficulty.
![Image](https://github.com/user-attachments/assets/8f3acccf-4484-4cfb-8acc-e71be7f23d25)

# Project 1: Dice Rolling Game
I created a program that mimics the rolling of two dice.  The program should, upon execution, generate two random integers, each within the range of 1 to 6 (inclusive), to represent the outcome of each die roll.  These results should then be displayed to the user.  After displaying the results, the program should prompt the user to determine if they wish to roll the dice again. Below was how my own results looked like:

![Image](https://github.com/user-attachments/assets/2179c447-8079-4151-9005-91e1c88155b6)

# Project 2: Number Guessing Game
I designed a number guessing game.  The computer randomly chooses a secret integer between 1 and 100 (inclusive). The player should then be prompted to input their guess.  The program should provide feedback to the player, indicating whether their guess is too high or too low, until the player correctly guesses the computer's secret number.

![Image](https://github.com/user-attachments/assets/2b928875-421f-4bd3-8550-4b4c6c03b924)

# Project 3: Rock, Paper, Scissors Game
I created from scratch this popular a Rock, Paper, Scissors game in Python.  The program:

Prompts the user to input their choice (rock, paper, or scissors)  using the letters '1', '2', or '3' respectively.

Has the computer randomly select its own choice (rock, paper, or scissors).

Display both the user's and the computer's choices using appropriate emojis (e.g., ⛰ for rock, 📄 for paper, ✂ for scissors).

Determines the winner based on the classic Rock, Paper, Scissors rules (rock beats scissors, scissors beats paper, paper beats rock).

Clearly announces the winner (or a tie).

![Image](https://github.com/user-attachments/assets/c0ffd5c3-2ab6-4f3c-8c32-ced00da7bcdf)

# Project 4: QR Code Generator
Created a program that takes user-provided data, like text or a website address, and generates a QR code.  The program should then save this QR code as a picture file, suitable for scanning with a mobile device.
The below was what I ended up doing, with the image being created and stored automatically in that same directory.
![Image](https://github.com/user-attachments/assets/cdb109b4-4009-4081-bc11-8818e3d01fda)

# Project 5: Currency Converter
I created a program that facilitates currency conversion.  The program allows the user to input a monetary value and choose the source and target currencies.

I chose 3 currencies for my program, which are the CFA(Communauté Financière Africaine) currency of my bilingual country Cameroon, the USD currency of the United States and the CAD currency of Canada.

Using predefined exchange rates, the program will then calculate and display the converted amount.
![Image](https://github.com/user-attachments/assets/999f82bd-c7b3-4add-a748-6c7b8760fad6)

# Project 6: Quiz Game
I develop here a program that constructs a multiple-choice quiz.  The program allows the user to respond to the questions presented.  After the user has completed the quiz, the program should calculate and display the user's score.
![Image](https://github.com/user-attachments/assets/ed2fbe06-bbd4-4d5b-b835-0fd83a692a10)

# Project 7: Tic Tac Toe Game
We'll craft here now a Tic-Tac-Toe game program.  Two players will alternate placing their marks—X's and O's—on a 3x3 grid.  The goal is to get three of your marks in a row (horizontally, vertically, or diagonally).

After each turn, the game board will be displayed, using distinct colors for X's and O's to make it easy to follow.  The program will check for a winner after every move.  The game concludes when one player achieves a winning pattern, or when all the spaces on the board are filled, resulting in a draw/tie.

![Image](https://github.com/user-attachments/assets/5f3541af-96f6-45db-ad6d-1403ac61b383)
![Image](https://github.com/user-attachments/assets/20deb4ae-cec2-4f4c-a71d-a56ed3d89263)

# Project 8: To-Do-List
I developed a basic To-Do List application that enables users to input tasks, display the existing task list, and delete tasks upon completion.

![Image](https://github.com/user-attachments/assets/28a1ae4c-6c00-435a-939d-3300c96c38ef)
![Image](https://github.com/user-attachments/assets/d29e42c7-24dc-4805-afa6-fb0d30402d1a)

# Project 9: Simple Text Editor
Developed a basic text editor application. This application enables users to either load an existing text file or generate a new one. Users can then modify the text content.  To persist these changes, users __must__ input the command "SAVE".

![Image](https://github.com/user-attachments/assets/d848ea58-efb9-4a66-85cb-c3238b9bd87d)

# Project 10: 
Pig Dice is a two-player game focused on strategy and a bit of luck.  The goal is to be the first player to reach 100 points.  Each player takes turns rolling a single die.  Each roll adds the die's value to the player's current turn score.  However, rolling a 1 ends the player's turn, and they lose all points accumulated during that turn.  The player must then pass the die to their opponent.  A key element of the game is deciding when to "hold" – banking the current turn score and ending the turn – versus continuing to roll and risk losing it all.

![Image](https://github.com/user-attachments/assets/240dfeda-e21f-405e-bfdd-4cb5f442c7bd)
![Image](https://github.com/user-attachments/assets/ac3160e0-c558-4d40-a0cc-529495fe5d07)
![Image](https://github.com/user-attachments/assets/4db7679d-d28e-4ccd-a393-c35a278f4a6a)
![Image](https://github.com/user-attachments/assets/0921ab02-c662-40bf-8857-4e3b6dfa821b)

# Project 11: Cow and Bulls Game
This project involves creating a number-guessing game called "Cows and Bulls."  The computer will generate a secret 4-digit number, and the player must deduce it.  Feedback will be given after each guess in the form of "cows" and "bulls."  A "bull" indicates a correctly guessed digit in the correct position, while a "cow" signifies a correct digit in the wrong position.  This game challenges the player's logical reasoning and problem-solving abilities, to persevere towards guessing the correct number.
Below was how I ended up guessing mine

![Image](https://github.com/user-attachments/assets/b6d4947b-3a34-4016-bf12-f5632f9b23d3)

# Project 12: Password Strength Checker
I simply wrote a program here to evaluate the strength of a password based on criteria like length, the inclusion of uppercase letters, numbers, and special characters. The program will then categorize the password as Very Weak, Weak, Medium, Strong, or Very Strong.
Check what the program said about mine below

![Image](https://github.com/user-attachments/assets/02491133-960a-4061-866b-a446a1e5a97d)

# Project 13: Password Generator
I developed a program that creates random passwords.  The user can customize the password generation by specifying parameters like the desired length and whether it should contain uppercase letters, numbers, and special symbols.

![Image](https://github.com/user-attachments/assets/7e311223-e747-47ae-b391-2f0237330ddf)

# Project 14: Word Guessing Game
In this Word Guessing Game project, players are trying to figure out a hidden word the computer randomly chooses. The computer chooses this word from a list stored in a text file. Players have six tries to guess the word, and each wrong guess reduces their remaining attempts.  Correctly guessed letters are shown in their places within the word, while incorrect guesses mean the player has to try again.
I personally failed after exhausting my six attempts.

![Image](https://github.com/user-attachments/assets/28226099-de45-43b5-b569-b4916f2eb9e1)

# Project 15: Slot Machine Game
This project simulates a slot machine game, offering a simple and engaging experience.  Players begin with a set balance and can place bets before each spin. The reels then spin, revealing a set of symbols.  Winning combinations result in payouts based on the player's wager.  Specifically, three matching symbols pay out 10 times the bet, while two matching symbols pay out 2 times the bet.  If no symbols match, the player loses their bet. The game continues until the player's balance reaches zero or they choose to stop playing and keep their winnings.
Below is how the game looks like

![Image](https://github.com/user-attachments/assets/e1b60490-ec33-43b6-aac2-9bf589ae0c6a)

# Project 16: ATM(Automated Teller Machine)
This ATM simulation project I did provided a hands-on learning experience in developing a simplified automated teller machine system. I built a program that enables users to perform common ATM functions such as checking account balances, depositing funds, and withdrawing cash.  This project served me on a platter an introduction to fundamental Object-Oriented Programming (OOP) principles, demonstrating how to organize program logic within a class structure and manage user input(UI logic) through a separate controller class.

![Image](https://github.com/user-attachments/assets/03b411cb-80da-4d53-b496-58f7c5ccccc8)



## 🚀 About Me
I'm an aspring Data Analyst and Data Scientist, with the obsession of making Python one of my biggest strengths.
After completing the AWS AI & ML Scholarship program 2023, my primary goal was to get started with some cool python projects, which will help me dive deep into the process of __thinking like a programmer__.


