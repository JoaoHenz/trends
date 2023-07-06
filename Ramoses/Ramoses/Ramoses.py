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


#def compare_two_words_to_discover_limt(word1, word2):
#    1+1

if __name__ == "__main__":
    # Connect to Google
    pytrend = TrendReq()
    
    complete_word_list = get_word_list()

    # Set search term and time frame
    keywords = ["Python programming", 
                "Data science", 
                "Data science2", 
                "Web development"]

    interest_over_time_df = run_google_trends(pytrend, keywords);

    print(interest_over_time_df)

    # TODO
    # 1 discover what is the upper limit and the bottom limit from the word list

    # TODO
    # discover the value of every word comparing to the upper limit and the bottom limit

    # TODO
    # build a graph with ALL the word using what we just gathered