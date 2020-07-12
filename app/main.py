import random
import time

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

# dictionary used to store the possible questions and their choices
test_dict = {
            "question1": {
                "question": "this is question 1",
                "choices": {
                    "answer": "this is question 1 answer",
                    "wrong1": "this is question 1 wrong choice 1",
                    "wrong2": "this is question 1 wrong choice 2",
                    "wrong3": "this is question 1 wrong choice 3",
                    "wrong4": "this is question 1 wrong choice 4"
                }
            },
            "question2": {
                "question": "this is question 2",
                "choices": {
                    "answer": "this is question 2 answer",
                    "wrong1": "this is question 2 wrong choice 1",
                    "wrong2": "this is question 2 wrong choice 2",
                    "wrong3": "this is question 2 wrong choice 3",
                    "wrong4": "this is question 2 wrong choice 4"
                }
            },
            "question3": {
                "question": "this is question 3",
                "choices": {
                    "answer": "this is question 3 answer",
                    "wrong1": "this is question 3 wrong choice 1",
                    "wrong2": "this is question 3 wrong choice 2",
                    "wrong3": "this is question 3 wrong choice 3",
                    "wrong4": "this is question 3 wrong choice 4"
                }
            },
            "question4": {
                "question": "this is question 4",
                "choices": {
                    "answer": "this is question 4 answer",
                    "wrong1": "this is question 4 wrong choice 1",
                    "wrong2": "this is question 4 wrong choice 2",
                    "wrong3": "this is question 4 wrong choice 3",
                    "wrong4": "this is question 4 wrong choice 4"
                }
            },
            "question5": {
                "question": "this is question 5",
                "choices": {
                    "answer": "this is question 5 answer",
                    "wrong1": "this is question 5 wrong choice 1",
                    "wrong2": "this is question 5 wrong choice 2",
                    "wrong3": "this is question 5 wrong choice 3",
                    "wrong4": "this is question 5 wrong choice 4"
                }
            },
            "question6": {
                "question": "this is question 6",
                "choices": {
                    "answer": "this is question 6 answer",
                    "wrong1": "this is question 6 wrong choice 1",
                    "wrong2": "this is question 6 wrong choice 2",
                    "wrong3": "this is question 6 wrong choice 3",
                    "wrong4": "this is question 6 wrong choice 4"
                }
            },
            "question7": {
                "question": "this is question 7",
                "choices": {
                    "answer": "this is question 7 answer",
                    "wrong1": "this is question 7 wrong choice 1",
                    "wrong2": "this is question 7 wrong choice 2",
                    "wrong3": "this is question 7 wrong choice 3",
                    "wrong4": "this is question 7 wrong choice 4"
                }
            },
            "question8": {
                "question": "this is question 8",
                "choices": {
                    "answer": "this is question 8 answer",
                    "wrong1": "this is question 8 wrong choice 1",
                    "wrong2": "this is question 8 wrong choice 2",
                    "wrong3": "this is question 8 wrong choice 3",
                    "wrong4": "this is question 8 wrong choice 4"
                }
            },
            "question9": {
                "question": "this is question 9",
                "choices": {
                    "answer": "this is question 9 answer",
                    "wrong1": "this is question 9 wrong choice 1",
                    "wrong2": "this is question 9 wrong choice 2",
                    "wrong3": "this is question 9 wrong choice 3",
                    "wrong4": "this is question 9 wrong choice 4"
                }
            },
            "question10": {
                "question": "this is question 10",
                "choices": {
                    "answer": "this is question 10 answer",
                    "wrong1": "this is question 10 wrong choice 1",
                    "wrong2": "this is question 10 wrong choice 2",
                    "wrong3": "this is question 10 wrong choice 3",
                    "wrong4": "this is question 10 wrong choice 4"
                }
            },
            "question11": {
                "question": "this is question 11",
                "choices": {
                    "answer": "this is question 11 answer",
                    "wrong1": "this is question 11 wrong choice 1",
                    "wrong2": "this is question 11 wrong choice 2",
                    "wrong3": "this is question 11 wrong choice 3",
                    "wrong4": "this is question 11 wrong choice 4"
                }
            },
            "question12": {
                "question": "this is question 12",
                "choices": {
                    "answer": "this is question 12 answer",
                    "wrong1": "this is question 12 wrong choice 1",
                    "wrong2": "this is question 12 wrong choice 2",
                    "wrong3": "this is question 12 wrong choice 3",
                    "wrong4": "this is question 12 wrong choice 4"
                }
            },
            "question13": {
                "question": "this is question 13",
                "choices": {
                    "answer": "this is question 13 answer",
                    "wrong1": "this is question 13 wrong choice 1",
                    "wrong2": "this is question 13 wrong choice 2",
                    "wrong3": "this is question 13 wrong choice 3",
                    "wrong4": "this is question 13 wrong choice 4"
                }
            },
            "question14": {
                "question": "this is question 14",
                "choices": {
                    "answer": "this is question 14 answer",
                    "wrong1": "this is question 14 wrong choice 1",
                    "wrong2": "this is question 14 wrong choice 2",
                    "wrong3": "this is question 14 wrong choice 3",
                    "wrong4": "this is question 14 wrong choice 4"
                }
            },
            "question15": {
                "question": "this is question 15",
                "choices": {
                    "answer": "this is question 15 answer",
                    "wrong1": "this is question 15 wrong choice 1",
                    "wrong2": "this is question 15 wrong choice 2",
                    "wrong3": "this is question 15 wrong choice 3",
                    "wrong4": "this is question 15 wrong choice 4"
                }
            },
            "question16": {
                "question": "this is question 16",
                "choices": {
                    "answer": "this is question 16 answer",
                    "wrong1": "this is question 16 wrong choice 1",
                    "wrong2": "this is question 16 wrong choice 2",
                    "wrong3": "this is question 16 wrong choice 3",
                    "wrong4": "this is question 16 wrong choice 4"
                }
            },
            "question17": {
                "question": "this is question 17",
                "choices": {
                    "answer": "this is question 17 answer",
                    "wrong1": "this is question 17 wrong choice 1",
                    "wrong2": "this is question 17 wrong choice 2",
                    "wrong3": "this is question 17 wrong choice 3",
                    "wrong4": "this is question 17 wrong choice 4"
                }
            },
            "question18": {
                "question": "this is question 18",
                "choices": {
                    "answer": "this is question 18 answer",
                    "wrong1": "this is question 18 wrong choice 1",
                    "wrong2": "this is question 18 wrong choice 2",
                    "wrong3": "this is question 18 wrong choice 3",
                    "wrong4": "this is question 18 wrong choice 4"
                }
            },
            "question19": {
                "question": "this is question 19",
                "choices": {
                    "answer": "this is question 19 answer",
                    "wrong1": "this is question 19 wrong choice 1",
                    "wrong2": "this is question 19 wrong choice 2",
                    "wrong3": "this is question 19 wrong choice 3",
                    "wrong4": "this is question 19 wrong choice 4"
                }
            },
            "question20": {
                "question": "this is question 20",
                "choices": {
                    "answer": "this is question 20 answer",
                    "wrong1": "this is question 20 wrong choice 1",
                    "wrong2": "this is question 20 wrong choice 2",
                    "wrong3": "this is question 20 wrong choice 3",
                    "wrong4": "this is question 20 wrong choice 4"
                }
            }
}

# welcome/menu screen
print("CLahoot!")
# ask user to select topic
print("""There are 3 topics available for you to choose between,
1) Topic 1
2) Topic 2
3) Topic 3\n""")
selected_topic = input("What topic would you like to be quizzed on? (Please enter the topic number)\n")
# ask user to enter name
# display rules by entering "r" during topic selection or name input
# call randomizer() to get data for current quiz
if selected_topic == "1":
    current_quiz = randomizer(test_dict)
elif selected_topic == "2":
    current_quiz = randomizer(test_dict)
else:
    current_quiz = randomizer(test_dict)

print(current_quiz)
# display question 1
# ask user for answer
# display whether user is correct or not, display correct answer and how long it took
# call scoring for question 1
# display updated user score and correct answer streak
# repeat for all 10 questions
# display leaderboard and user's final score
# ask to play again
