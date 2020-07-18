# using the time taken to answer the question and if the user is correct,
# calculates the user's points for the current question and returns the value

# the score data from the previous question is passed into the function as a list
# the list is full of 0 values when the function is run for the first question
def scoring(answer, user_answer, time_taken, score_data):

    # if user answered correctly, update all values
    if answer == user_answer:
        
        # update the answer streak, needs to be done first since it is used for the calculations below
        score_data[4] += 1
        
        # calculations for the pts given for current question, 30 seconds is the cut off for additional points for speed
        # 100 pts for correct answer, up to another 100 pts determined by speed, all multiplied by 1.x where x is answer streak - 1
        if time_taken < 30:
            score_data[0] = int(((100 + 100 * ((30 - time_taken) / 30))) * (1 + ((score_data[4] - 1) / 10)))
        else:
            score_data[0] = int(100 * (1 + ((score_data[4] - 1) / 10)))
        
        # increment the total score by the pts awarded for the current question
        score_data[1] += score_data[0]

        score_data[2] += 1                  # total correct answers
        score_data[3] += time_taken         # total time on correct questions

        # tracking highest answer streak [5] by comparing to current answer streak [4]
        if score_data[5] <= score_data[4]:
            score_data[5] = score_data[4]

    # if user answered incorrectly, need to reset the answer streak to 0 and return 0 pts for the question
    # return an additional value for the previous answer streak so that it can be displayed in a print statement
    else:
        score_data[6] = score_data[4]       # set the previous answer streak to the answer streak value passed in
        score_data[4] = 0                   # now reset the answer streak
        score_data[0] = 0                   # set the pts for the current question to 0 for a wrong answer

    return score_data

# prints out some of the information being tracked and maintained by the scoring function
def print_current_score(score_data):
    print("\n--------------------------------------------------------------------------------------------------------\n")
    print(f"You received {score_data[0]} points for this question.\n")
    print(f"Your current score is: {score_data[1]}\n")

    # prints out a message informing the user of the current state of their answer streak
    if score_data[4] == 1:
        print("You have started an answer streak by answering this question correctly.")
    elif score_data[4] > 1:
        print(f"You are on a roll with an answer streak of {score_data[4]}!")
    elif score_data[4] == 0 and score_data[6] == 0:
        print("")
    else:
        print(f"You have dropped your answer streak of {score_data[6]}.")

# after all questions have been answered calculate avg time for correct answers as a fun fact to display with the results
# uses a try/except block in the case that no questions were answered correctly as it would be trying to divide by 0
def get_avg_time(time, correct):
    try:
        return (time / correct)
    except Exception:
        return 0
