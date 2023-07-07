from operator import le
from re import L
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


def get_word_list():
    word_list = []

    # Read from file
    with open("WordList.txt", "r") as file:
        # Read each line and append it to the list
        for line in file:
            word_list.append(line.strip())

    return word_list

##max 5 words
def run_google_trends(pytrend, word_list):
    pytrend.build_payload(kw_list=keywords, timeframe='today 5-y')

    # Get interest over time
    return pytrend.interest_over_time()

def get_bigger(word1, word2):
    word1_counter = 0
    word2_counter = 0

def get_bigger_with_request(word1, word2):
    interest_over_time_df = run_google_trends(pytrend, keywords);

def find_correct_position(word_list, new_word):


class WeightedWord:
    def __init__(self, weight, word):
        self.weight = weight
        self.word = word

if __name__ == "__main__":
    # Connect to Google
    pytrend = TrendReq()
    
    complete_word_list = get_word_list()

    weighted_words = []

    weighted_words.append(WeightedWord(0, complete_word_list[0]))

    for i in range(1, len(complete_word_list)):
        weighted_words.insert(find_correct_position(weighted_words, complete_word_list[i]), 
                              complete_word_list[i])


    # TODO
    # 1 discover what is the upper limit and the bottom limit from the word list

    # TODO
    # discover the value of every word comparing to the upper limit and the bottom limit

    # TODO
    # build a graph with ALL the word using what we just gathered