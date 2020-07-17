import pickle
import os
import random
import sys
import time
import preset_leaderboard as plb
import question_dictionaries as qd

# takes the question dictionary for the selected topic and randomly picks 10 questions and 4 choices for each
# returns a list of lists containing the questions, choices and the answer key
def randomizer(question_dict):
    number_of_questions = random.randint(10, 20)

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

    # display leaderboard
    print("\n\n\n")
    print("{:^155}".format(f"High Scores for the {quiz_topic} topic with {len(quiz_data[0])} questions"))
    print("\n")
    print(" " * 62 + "{:^16}|{:^11}".format("Name", "Score"))
    print(" " * 62 + "----------------------------")
    for name, score in current_leaderboard:
        print (" " * 62 + "   {:<13}|{:^11}".format(name, score))


current_quiz = randomizer(qd.test_dict)
quiz_topic = "Capitol Cities"

leaderboard(quiz_topic, current_quiz, "test", 1000)
