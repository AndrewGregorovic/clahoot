import random
import time

# takes the question dictionary for the selected topic and randomly picks 10 questions and 4 choices for each
# returns a list of lists containing the questions, choices and the letter corresponding to the correct answers
def randomizer(dict):
    # using random module, pick a random question and mark it as having been picked so it can't be picked again
    # using random module, pick 4 choices out of the 5 options in a random order
    # ensure that the correct answer is always selected as one of the 4 choices and mark which choice is the answer
    # repeat 10 times to get the full set of answers, their choices and the answers
    # create a list for the questions, choice a, choice b, choice c, choice d and the answer key
    # combine the lists into a single list and return
    pass

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
test_dict = {}

# welcome/menu screen
print("CLahoot!")
# ask user to select topic
# ask user to enter name
# display rules by entering "r" during topic selection or name input
# call randomizer() to get data for current quiz
# display question 1
# ask user for answer
# display whether user is correct or not, display correct answer and how long it took
# call scoring for question 1
# display updated user score and correct answer streak
# repeat for all 10 questions
# display leaderboard and user's final score
# ask to play again
