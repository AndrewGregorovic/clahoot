import os
import random
import time
import question_dictionaries as qd


# takes the question dictionary for the selected topic and randomly picks 10 questions and 4 choices for each
# returns a list of lists containing the questions, choices and the answer key
def randomizer(question_dict):
    number_of_questions = 10

    # creates individual empty lists that will be used to hold the corresponding random selections
    question_list = []
    choice_a_list = []
    choice_b_list = []
    choice_c_list = []
    choice_d_list = []
    answer_key = []

    # picks 10 random questions from the dictionary passed to the function
    random_questions = (random.sample(list(question_dict), k=number_of_questions))

    for question in random_questions:
        # picks 4 of the 5 question choices for each question that has been randomly picked
        random_choices = random.sample(list(question_dict[question]["choices"]), k=4)

        # adds the appropriate values to the lists that will hold the current quiz data
        question_list.append(question_dict[question]["question"])
        choice_a_list.append(question_dict[question]["choices"][random_choices[0]])
        choice_b_list.append(question_dict[question]["choices"][random_choices[1]])
        choice_c_list.append(question_dict[question]["choices"][random_choices[2]])

        # ensures that the answer will always be one of the choices, if it wasn't picked randomly it's assigned to the "d" choice for the question
        if "answer" not in random_choices:
            choice_d_list.append(question_dict[question]["choices"]["answer"])
        else:
            choice_d_list.append(question_dict[question]["choices"][random_choices[3]])

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
# to avoid using global, the function also needs to be passed all the variables that it needs to return updated values for
def scoring(answer, user_answer, time_taken, current_points, total_score, total_correct, total_time, answer_streak):

    # if user answered correctly, update all values
    if answer == user_answer:
        total_correct += 1
        answer_streak += 1
        total_time += time_taken

        # 30 seconds is the cut off for additional points for speed
        # 100 pts for correct answer, up to another 100 pts determined by speed, all multiplied by 1.x where x is answer streak - 1
        if time_taken < 30:
            current_points = int(((100 + 100 * ((30 - time_taken) / 30))) * (1 + ((answer_streak - 1) / 10)))
        else:
            current_points = int(100 * (1 + ((answer_streak - 1) / 10)))
        total_score += current_points

        # returns a list of the updated values
        return [current_points, total_score, total_correct, total_time, answer_streak]

    # if user answered incorrectly, need to reset the answer streak to 0 and return 0 pts for the question
    # return an additional value for the previous answer streak so that it can be displayed in a print statement
    else:
        previous_answer_streak = answer_streak
        answer_streak = 0
        current_points = 0
        return [current_points, total_score, total_correct, total_time, answer_streak, previous_answer_streak]


# reads and saves the leaderboard information to a separate text file and displays the leaderboard at the end of the quiz
# updates the leaderboard if user makes it into the top 10
def leaderboard():
    # read leaderboard file and convert to a list of tuples
    # add user's current score if it higher than the 10th highest score
    # remove the lowest score and sort by score
    # save to file if leaderboard was updated
    # display leaderboard
    pass

# countdown function to be used before each question is displayed
def countdown():
    countdown_length = 5
    while countdown_length > 0:
        print(f"00:0{countdown_length}", end="\r")
        countdown_length -= 1
        time.sleep(1)

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
print("{:^155}".format("Press enter to continue\n"))
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
Before each question is displayed there will be a short countdown. Once it ends, a hidden timer will start to track how quickly you answer the question.
After each question you will be given time to review the question and answer before moving on. This screen will also display your current score and speed.
You will be awarded points for each correct answer. You will receive additional points for faster answers and maintaining an answer streak.

At the end of the quiz, your final score will be displayed along with how many questions you answered correctly.
You will also have the option to view the current leaderboard for the topic you selected.
\n\n\n\n""")
print("{:^155}".format("Press enter to continue to topic selection"))
input("{:^77}".format(""))

# clear screen and ask user to select topic
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\n\n")
print("""There are 3 topics available for you to choose between,\n
    1) Capitol Cities
    2) World Geography
    3) World Languages""")
print("\n")

# repeat until user makes a valid selection
while True:

    # try/except block to prevent the app from crashing when the user enters an invalid input
    try:
        # ask user for their selection
        selected_topic = int(input("What topic would you like to be quizzed on? (Please enter the topic number)\n"))
        if selected_topic == 1:
            current_quiz = randomizer(qd.test_dict)
            break
        elif selected_topic == 2:
            current_quiz = randomizer(qd.test_dict)
            break
        elif selected_topic == 3:
            current_quiz = randomizer(qd.test_dict)
            break
        else:
            print("\nSorry, that isn't a valid selection.\n")
    except Exception:
        print("\nSorry, that isn't a valid selection.\n")

print("\n\n")

# ask user to enter name, repeat until they enter a valid name that only contains letters of the alphabet
while True:
    user_name = input("Please enter your name (only use letters, special characters and numbers are not allowed):\n")

    # checks that user_name only contains letters of the alphabet
    if user_name.isalpha() == False:
        print("Sorry that is not a valid name.")
    else:
        break

print("\n\n\n")
print("{:^155}".format("Press enter when you are ready to begin the quiz"))
input("{:^77}".format(""))

# initialise variables that will be used during the quiz
answer_streak = 0
current_points = 0
total_score = 0
total_correct = 0
total_time = 0
choices = ("a", "b", "c", "d")

# loop through all the questions
for i in range(0, len(current_quiz[0])):
    os.system('cls' if os.name == 'nt' else 'clear')

    # prints the current question number and a countdown to it being displayed, also starts a timer when the countdown ends
    print("\n\n\n")
    print(f"Question {i + 1}/{len(current_quiz[0])}")
    print("\n")
    countdown()
    os.system('cls' if os.name == 'nt' else 'clear')
    start_time = time.time()

    # print the current question
    print("\n\n\n")
    print(f"Question {i + 1}/{len(current_quiz[0])}\n\n")
    print(f"{current_quiz[0][i]}\n")

    # iterates over the choices tuple to print each one out
    for x in range(0, len(choices)):
        print(f"    {choices[x]}) {current_quiz[x + 1][i]}")

    print("\n\n")

    # ask for the user's answer and applies necessary string methods to check if it's a valid answer, repeat until a valid answer is given
    while True:
        user_answer = input("Enter your answer: ")
        user_answer = user_answer.strip().lower()
        if user_answer in choices:
            break
        else:
            print("Sorry that is not one of the 4 choices, please try again.")

    # stop the timer when user enters a valid answer and find the difference to get time taken
    end_time = time.time()
    time_taken = end_time - start_time
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n")

    # reprints the question for review, showing what the correct answer was and what answer the user gave
    print(f"Question {i + 1}/{len(current_quiz[0])}\n\n")
    print(f"{current_quiz[0][i]}\n")
    for x in range(0, len(choices)):
        print(f"    {choices[x]}) {current_quiz[x + 1][i]}", end=" ")

        if current_quiz[5][i] == choices[x]:
            print("- Correct answer")
        elif user_answer == choices[x] and current_quiz[5][i] != choices[x]:
            print("- Your answer")
        else:
            print("")

    print("\n\n")

    # compares user_answer to the answer key and prints whether they answered correctly or not
    if user_answer == current_quiz[5][i]:
        print("Well done, you answered the question", end=" ")
        print("correctly", end=" ")
        print(f"in {time_taken:.1f} seconds.")
    else:
        print("Good try, unfortunately you answered the question", end=" ")
        print("incorrectly", end=" ")
        print(f"in {time_taken:.1f} seconds.")

    # calls the scoring function and updates variables with the values returned
    score = scoring(current_quiz[5][i], user_answer, time_taken, current_points, total_score, total_correct, total_time, answer_streak)
    current_points = score[0]
    total_score = score[1]
    total_correct = score[2]
    total_time = score[3]
    answer_streak = score[4]

    print("\n\n")
    print(f"You received {current_points} points for this question.\n")
    print(f"Your current score is: {total_score}\n")

    # prints out a message informing the user of the current state of their answer streak
    if answer_streak == 1:
        print("You have started an answer streak by answering this question correctly.")
    elif answer_streak > 1:
        print(f"You are on a roll with an answer streak of {answer_streak}!")
    elif answer_streak == 0 and score[5] == 0:
        print("")
    else:
        print(f"You have dropped your answer streak of {score[5]}.")

    # print a different continue message depending on if it's the last question or not
    print("\n\n")
    if i + 1 != len(current_quiz[0]):
        input("Press enter to continue to the next question")
    else:
        input("Press enter to continue to your results")

# calculate avg time for correct answers as a fun fact to display with the results
avg_time = total_time / total_correct

# clear screen and display results
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\n\n")
print("{:^155}".format("Congratulations on completing the quiz!\n\n"))
print("{:^155}".format(f"You answered {total_correct} out of {len(current_quiz[0])} questions correctly!\n"))
print("{:^155}".format(f"Your final score is {total_score}\n\n\n"))
print("{:^155}".format(f"Fun fact: You had an average answer speed of {avg_time:.1f} seconds for the questions that you answered correctly.\n\n\n\n"))
print("{:^155}".format("To view the leaderboard enter 'l', otherwise would you like to take another quiz? (y/n): "))
end_of_quiz_input = input("{:^77}".format(""))
