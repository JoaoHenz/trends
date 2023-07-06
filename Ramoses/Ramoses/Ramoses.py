from pytrends.request import TrendReq
import matplotlib.pyplot as plt


complete_word_list =[
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
        "aa",
    ]

#word_list =
#{
#    ""
#}

#def pytrends_response:


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

    # Set search term and time frame
    keywords = ["Python programming", 
                "Data science", 
                "Data science2", 
                "Data science2", 
                "Web development"]

    interest_over_time_df = run_google_trends(pytrend, keywords);

    print(interest_over_time_df)


    # Plotting the data
    for kw in keywords:
        plt.plot(interest_over_time_df.index, interest_over_time_df[kw], label=kw)

    plt.title("Interest Over Time")
    plt.xlabel("Year")
    plt.ylabel("Interest")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    # 1 discover what is the upper limit and the bottom limit from the word list

    # discover the value of every word comparing to the upper limit and the bottom limit
