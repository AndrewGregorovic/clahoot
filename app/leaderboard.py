import pickle
import sys
import os
import time

def clear():
    if os.name == "nt":
        command = "cls"
    else:
        command = "clear"

    os.system(command)

def welcome():
    print("\n\n")
    print("                  CCCCCCCCCCCCC lllllll                    hhhhhhh                                                           tttt            !!!           ")
    print("               CCC::::::::::::C l:::::l                    h:::::h                                                        ttt:::t           !!:!!          ")
    print("             CC:::::::::::::::C l:::::l                    h:::::h                                                        t:::::t           !:::!          ")
    print("            C:::::CCCCCCCC::::C l:::::l                    h:::::h                                                        t:::::t           !:::!          ")
    print("           C:::::C       CCCCCC  l::::l    aaaaaaaaaaaaa    h::::h hhhhh           ooooooooooo       ooooooooooo    ttttttt:::::ttttttt     !:::!          ")
    print("          C:::::C                l::::l    a::::::::::::a   h::::hh:::::hhh      oo:::::::::::oo   oo:::::::::::oo  t:::::::::::::::::t     !:::!          ")
    print("          C:::::C                l::::l    aaaaaaaaa:::::a  h::::::::::::::hh   o:::::::::::::::o o:::::::::::::::o t:::::::::::::::::t     !:::!          ")
    print("          C:::::C                l::::l             a::::a  h:::::::hhh::::::h  o:::::ooooo:::::o o:::::ooooo:::::o tttttt:::::::tttttt     !:::!          ")
    print("          C:::::C                l::::l      aaaaaaa:::::a  h::::::h   h::::::h o::::o     o::::o o::::o     o::::o       t:::::t           !:::!          ")
    print("          C:::::C                l::::l    aa::::::::::::a  h:::::h     h:::::h o::::o     o::::o o::::o     o::::o       t:::::t           !:::!          ")
    print("          C:::::C                l::::l   a::::aaaa::::::a  h:::::h     h:::::h o::::o     o::::o o::::o     o::::o       t:::::t           !!:!!          ")
    print("           C:::::C       CCCCCC  l::::l  a::::a    a:::::a  h:::::h     h:::::h o::::o     o::::o o::::o     o::::o       t:::::t    tttttt  !!!           ")
    print("            C:::::CCCCCCCC::::C l::::::l a::::a    a:::::a  h:::::h     h:::::h o:::::ooooo:::::o o:::::ooooo:::::o       t::::::tttt:::::t                ")
    print("             CC:::::::::::::::C l::::::l a:::::aaaa::::::a  h:::::h     h:::::h o:::::::::::::::o o:::::::::::::::o       tt::::::::::::::t  !!!           ")
    print("               CCC::::::::::::C l::::::l  a::::::::::aa:::a h:::::h     h:::::h  oo:::::::::::oo   oo:::::::::::oo          tt:::::::::::tt !!:!!          ")
    print("                  CCCCCCCCCCCCC llllllll   aaaaaaaaaa  aaaa hhhhhhh     hhhhhhh    ooooooooooo       ooooooooooo              ttttttttttt    !!!           ")
    print("\n")
    print("{:^163}".format("\u001b[1mby Andrew Gregorovic\u001b[0m"))

# reads and saves the leaderboard information to a separate text file and displays the leaderboard at the end of the quiz
# updates the leaderboard if user makes it into the top 10
def leaderboard(quiz_topic, quiz_data, user_name, score):

    # get the directory of main.py
    path = sys.path[0]

    # load the pickled leaderboard data, if no file found load the fallback data in preset_leaderboard.py
    try:
        with open(path + "/leaderboard.pickle", "rb") as f:
            full_leaderboard = pickle.load(f)
    except:
        full_leaderboard = plb.preset_leaderboard

    # find the set of high scores for the quiz topic and length of the quiz just completed
    current_leaderboard = full_leaderboard[quiz_topic][len(quiz_data[0])]

    # add user's current score, sort the leaderboard by the 2nd tuple element (score), and delete anything outside of the top 10
    current_leaderboard.append((user_name, score))
    current_leaderboard.sort(key = lambda x: x[1], reverse = True)
    del current_leaderboard[10:]

    # replace the old leaderboard list with the new one in case anything changed and pickle the data to a file in the same directory as main.py
    full_leaderboard[quiz_topic][len(quiz_data[0])] = current_leaderboard
    with open(path + "/leaderboard.pickle", "wb") as f:
        pickle.dump(full_leaderboard, f, pickle.HIGHEST_PROTOCOL)

    return current_leaderboard

# print the leaderboard of high score for the current quiz topic and number of questions
def print_leaderboard(topic, quiz_data, current_leaderboard):
    print("\n\n\n")
    print("{:^187}".format(f"\u001b[1mHigh Scores for the \u001b[4m{topic}\u001b[0m\u001b[1m topic with \u001b[4m{len(quiz_data[0])}\u001b[0m\u001b[1m questions\u001b[0m"))
    print("\n")
    print(" " * 62 + "{:^16}|{:^11}".format("Name", "Score"))
    print(" " * 62 + "----------------------------")
    for name, score in current_leaderboard:
        print (" " * 62 + "   {:<13}|{:^11}".format(name, score))

# get user input, since we're at the leaderboard the print message needs to be different to the results screen
def leaderboard_input():
    while True:
        print("\n")
        print("{:^155}".format("Would you like to take another quiz? (y/n): "))

        # the user isn't allowed to input 'l' again and the only other inputs allowed are 'y' and 'n' which we haven't checked yet
        # so we can save the input to the same variable as before
        end_of_quiz_input = input("{:^77}".format("")).strip().lower()
        if end_of_quiz_input == "quit":
            clear()
            print("\n")
            print("{:^155}".format("Thanks for playing,"))
            welcome()
            time.sleep(5)
            clear()
            exit()
        elif end_of_quiz_input != "l" and end_of_quiz_input != "y" and end_of_quiz_input != "n":
            print("")
            print("{:^155}".format("Sorry that isn't a valid option, please try again.\n"))

        # need to print another message if the user tries to input 'l' again
        elif end_of_quiz_input == "l":
            print("")
            print("{:^155}".format("You are already viewing the leaderboard.\n"))
        else:
            break

    return end_of_quiz_input
