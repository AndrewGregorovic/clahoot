# Clahoot!

## About
Clahoot! is a multiple choice quiz game created as a terminal application based on the online Kahoot! game.
It has been adapted to a single player experience with a leaderboard rather than an online multiplayer game and follows a similar scoring style to Kahoot!.

## Requirements
The only requirement to run Clahoot! on your local machine you will need to have Python 3.8 installed.

Note: This was created in a linux environment, so it may not run 100% correctly on another operating system.

## Instructions

### Running Clahoot! through Python:
1. Open the terminal on your system.
2. Find the file path to the location where you have saved the files for Clahoot!, namely main.py.
3. Enter the command "python path/to/location/main.py" into the terminal.

### Running Clahoot! as an executable script:
1. Open the terminal on your system.
2. Find the file path to the location where you have saved the files for Clahoot!, namely main.py.
3. Enter "which python" into the terminal, copy the path given by the command.
4. Open main.py in a text editor and replace the path on line 1 with the path you copied just before. Make sure you keep the #! on line 1!
5. Go back to the terminal and enter "chmod +x path/to/location/main.py".
6. Now you can run Clahoot! by simply using the command "path/to/location/main.py".

Note: If main.py is in the current working directory you still need to indicate that in the terminal by using "./main.py".

### Additional Options
Clahoot! can be run with the following options:
- --help: displays the contents of this readme file instead of running the actual app.
- --anon: runs Clahoot!, will ask you for a topic selection but does not ask you to enter a name, name will be set to "anonymous". This persists for the current session.
- --random: runs Clahoot!, will ask you for a name but not for your topic selection, a topic will be selected at random. This persists for the current session.
- --start: combination of --anon and --random, runs Clahoot! but will not ask for a name or topic selection. After the welcome screen you will be taken straight to the start of a quiz.

## How to play
- The app will randomly choose the length of the quiz (10-20 questions) and the questions that you will be asked.
- The questions will be from a pool of potential questions for the topic you select.
- To input your answer, type the letter corresponding to the choice you would like to select and press 'Enter'.
- Before each question is displayed there will be a short countdown. Once it ends, a hidden timer will start to track how quickly you answer the question.
- After each question you will be given time to review the question and answer before moving on. This screen will also display your current score and speed.
- You will be awarded points for each correct answer. You will receive additional points for faster answers and maintaining an answer streak.
- At the end of the quiz, your final score will be displayed along with how many questions you answered correctly and a fun fact about your performance.
- Your final score will be added to the leaderboard if it qualifies as one of the top 10 score for the current topic and question length.
- You will also have the option to view the current leaderboard for the topic you selected as well as options to play again or quit.
