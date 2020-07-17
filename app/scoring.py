# using the time taken to answer the question and if the user is correct,
# calculates the user's points for the current question and returns the value
# to avoid using globals, the function also needs to be passed all the variables that it needs to return updated values for
def scoring(answer, user_answer, time_taken, current_points, total_score, total_correct, total_time, answer_streak, highest_streak):

    # if user answered correctly, update all values
    if answer == user_answer:
        total_correct += 1
        answer_streak += 1
        total_time += time_taken

        if highest_streak <= answer_streak:
            highest_streak = answer_streak

        # 30 seconds is the cut off for additional points for speed
        # 100 pts for correct answer, up to another 100 pts determined by speed, all multiplied by 1.x where x is answer streak - 1
        if time_taken < 30:
            current_points = int(((100 + 100 * ((30 - time_taken) / 30))) * (1 + ((answer_streak - 1) / 10)))
        else:
            current_points = int(100 * (1 + ((answer_streak - 1) / 10)))
        total_score += current_points

        # returns a list of the updated values
        return [current_points, total_score, total_correct, total_time, answer_streak, highest_streak]

    # if user answered incorrectly, need to reset the answer streak to 0 and return 0 pts for the question
    # return an additional value for the previous answer streak so that it can be displayed in a print statement
    else:
        previous_answer_streak = answer_streak
        answer_streak = 0
        current_points = 0
        return [current_points, total_score, total_correct, total_time, answer_streak, highest_streak, previous_answer_streak]
