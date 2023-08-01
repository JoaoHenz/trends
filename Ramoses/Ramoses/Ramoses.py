from operator import le
from re import L
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


def get_word_list():
    word_list = []
    # Read from file
    try:
        with open("WordList.txt", "r") as file:
            # Read each line and append it to the list
            for line in file:
                word_list.append(line.strip())

    except FileNotFoundError:
        print("WordList.txt file not found.")
        return None

    return word_list

def run_google_trends(pytrend, word_list):
    pytrend.build_payload(kw_list=word_list, timeframe='today 5-y')
    return pytrend.interest_over_time()

def get_bigger(word1, word2):
    return word1 if word1 > word2 else word2

def get_bigger_with_request(word1, word2):
    trend_data = run_google_trends(pytrend, [word1, word2])
    return get_bigger(trend_data[word1].sum(), trend_data[word2].sum())

def find_correct_position(word_list, new_word):
    position = 0
    for word in word_list:
        if new_word > word:
            position += 1
        else:
            break
    return position

class WeightedWord:
    def __init__(self, weight, word):
        self.weight = weight
        self.word = word

if __name__ == "__main__":
    pytrend = TrendReq()
    
    complete_word_list = get_word_list()
    
    if complete_word_list is None:
        # Handle the error
        pass
    
    # Rest of the code
