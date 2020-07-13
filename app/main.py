import os
import random
import time
import question_dictionaries as qd


# takes the question dictionary for the selected topic and randomly picks 10 questions and 4 choices for each
# returns a list of lists containing the questions, choices and the answer key
def randomizer(question_dict, number_of_questions=10):

    # creates individual empty lists that will be used to hold the corresponding random selections
    question_list = []
    choice_a_list = []
    choice_b_list = []
    choice_c_list = []
    choice_d_list = []
    answer_key = []

    # picks 10 random questions from the dictionary passed to the function
    random_questions = (random.sample(list(question_dict), k=number_of_questions))

    for i in random_questions:
        # picks 4 of the 5 question choices for each question that has been randomly picked
        random_choices = random.sample(list(question_dict[i]["choices"]), k=4)

        # adds the appropriate values to the lists that will hold the current quiz data
        question_list.append(question_dict[i]["question"])
        choice_a_list.append(question_dict[i]["choices"][random_choices[0]])
        choice_b_list.append(question_dict[i]["choices"][random_choices[1]])
        choice_c_list.append(question_dict[i]["choices"][random_choices[2]])

        # ensures that the answer will always be one of the choices, if it wasn't picked randomly it's assigned to the "d" choice for the question
        if "answer" not in random_choices:
            choice_d_list.append(question_dict[i]["choices"]["answer"])
        else:
            choice_d_list.append(question_dict[i]["choices"][random_choices[3]])

    # once the list of choices for each question is populated, iterate over the lists to determine which choice is the answer and create the answer key
    for i in range(0, len(random_questions)):
        if choice_a_list[i] == question_dict[random_questions[i]]["choices"]["answer"]:
             answer_key.append("a")
        elif choice_b_list[i] == question_dict[random_questions[i]]["choices"]["answer"]:
            answer_key.append("b")
        elif choice_c_list[i] == question_dict[random_questions[i]]["choices"]["answer"]:
            answer_key.append("c")
        elif choice_d_list[i] == question_dict[random_questions[i]]["choices"]["answer"]:
            answer_key.append("d")
        else:
            answer_key.append("answer not found")
    
    # returns a list of lists which contains all the required values for the current quiz
    return [question_list, choice_a_list, choice_b_list, choice_c_list, choice_d_list, answer_key]


# using the time taken to answer the question and if the user is correct,
# calculates the user's points for the current question and returns the value
def scoring():
    # 100 pts for correct answer, up to another 100 pts for answering quickly (0 additional pts at 30 secs)
    # keep track of correct answers in a row and use to multiply total pts for question by the number of
    # correct answers in a row
    # i.e. 3rd correct answer in a row, answered in 15 secs gives 100 + 100 * (15/30) * 1.3 (.3 from 3 in a row)
    # if user answered incorrectly reset the count of correct answers in a row and return 0
    pass


# reads and saves the leaderboard information to a separate text file and displays the leaderboard at the end of the quiz
# updates the leaderboard if user makes it into the top 10
def leaderboard():
    # read leaderboard file and convert to a list of tuples
    # add user's current score if it higher than the 10th highest score
    # remove the lowest score and sort by score
    # save to file if leaderboard was updated
    # display leaderboard
    pass


# welcome screen
print("\n\n\n")
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
print("{:^155}".format("by Andrew Gregorovic"))
print("\n\n\n\n")
print("{:^155}".format("Enter any key to continue\n"))
input("{:^77}".format(""))

# clear screen and display the instructions/rules
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\n\n")
print("{:^155}".format("Clahoot!\n\n"))
print("""Clahoot! is a multiple choice quiz game created as a terminal application based on the online Kahoot! game.
It has been adapted to a single player experience with a leaderboard rather than an online multiplayer game and follows a similar scoring style to Kahoot!.\n\n""")
print("{:^155}".format("Instructions\n\n"))
print("""The app will choose 10 random questions from a pool of potential questions for the topic you select.
To input your answer, type the letter corresponding to the choice you would like to select and press 'Enter'.
After each question you will be given time to review the question and answer before moving on. This screen will also display your current score.
You will be awarded points for each correct answer. You will receive additional points for faster answers and maintaining an answer streak.

At the end of the quiz, your final score will be displayed along with how many questions you answered correctly.
You will also have option to view the current leaderboard.
\n\n\n\n""")
print("{:^155}".format("Enter any key to continue to topic selection"))
input("{:^77}".format(""))

# clear screen and ask user to select topic
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\n\n")
print("""There are 3 topics available for you to choose between,\n
    1) Capitol Cities
    2) World Geography
    3) World Languages""")
print("\n")

selected_topic = 0
# repeat until user makes a valid selection
while selected_topic not in range(1,4):
    # try/except block to prevent the app from crashing when the user enters an invalid input
    try:
        selected_topic = int(input("What topic would you like to be quizzed on? (Please enter the topic number)\n"))
        if selected_topic == 1:
            current_quiz = randomizer(qd.test_dict)
        elif selected_topic == 2:
            current_quiz = randomizer(qd.test_dict)
        elif selected_topic == 3:
            current_quiz = randomizer(qd.test_dict)
        else:
            print("\nSorry, that isn't a valid selection.\n")
    except Exception:
        print("\nSorry, that isn't a valid selection.\n")

# ask user to enter name

# call randomizer() to get data for current quiz

print(current_quiz)
# display question 1
# ask user for answer
# display whether user is correct or not, display correct answer and how long it took
# call scoring for question 1
# display updated user score and correct answer streak
# repeat for all 10 questions
# display leaderboard and user's final score
# ask to play again
