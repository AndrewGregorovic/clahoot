import pickle
import sys

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
