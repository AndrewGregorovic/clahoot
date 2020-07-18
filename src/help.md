# Clahoot!

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
6. Now you can run Clahoot! by simply using the command "./path/to/location/main.py".

Note: If main.py is in the current working directory you still need to indicate that in the terminal by using "./main.py".

### Additional Options
Clahoot! can be run with the following options (if viewing this in the terminal ignore the ` characters):
--help: displays the contents of this readme file instead of running the actual app.
--anon: runs Clahoot!, will ask you for a topic selection but does not ask you to enter a name, name will be set to "anonymous". This persists for the current session.
--random: runs Clahoot!, will ask you for a name but not for your topic selection, a topic will be selected at random. This persists for the current session.
--start: combination of --anon and --random, runs Clahoot! but will not ask for a name or topic selection and will skip the quiz instructions. After the welcome screen you will be taken straight to the start of a quiz.
