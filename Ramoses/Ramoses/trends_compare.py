from operator import le
from re import L
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_word_list():
    word_list = []

    # Read from file
    with open("WordList.txt", "r") as file:
        # Read each line and append it to the list
        for line in file:
            word_list.append(line.strip())

    return word_list

def compare_word(a,b, timeframe):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list = [a,b], timeframe = timeframe)
    df_interest = pytrend.interest_over_time()
    df_interest=df_interest.reset_index().drop('isPartial',axis=1)
    df_interest['year_month'] = df_interest['date'].apply(lambda x : (x.year,x.month))
    df_interest = df_interest.drop('date',axis=1)
    df_interest = df_interest.groupby('year_month').mean().reset_index()
    return df_interest

all_words = get_word_list()
timeframe = 'today 12-m'
scores = dict()
for i,w1 in enumerate(all_words):
    print("word number {}".format(i))
    compared = dict()
    for w2 in all_words:
        if w1 != w2:
            compared[w2] = compare_word(w1,w2,timeframe)
    scores[w1] = compared

found_dates = list(scores[all_words[0]][all_words[1]]['year_month'])
df_compare = pd.DataFrame(columns = all_words)
list_ranking = []
for d in found_dates:
    cols =  ['word'] + all_words
    df_compare = pd.DataFrame(columns = cols)

    for w1 in all_words:
        row = [0 for i in range(len(cols))]
        row[0] = w1
        for i,w2 in enumerate(all_words):
            if w1 != w2:
                df = scores[w1][w2]
                df = df[df['year_month'] == d]
                if df[w2].iloc[0] < df[w1].iloc[0]:
                    row[i+1] = 1
        df_temp = pd.DataFrame([row], columns = cols)
        df_compare = pd.concat([df_compare, df_temp])

    df_compare['sum'] = df_compare.apply(lambda x: x[1:].sum(), axis=1)
    df_compare = df_compare.sort_values(by = 'sum', ascending=False)
    ranking = [d] + list(df_compare['word'])
    list_ranking.append(ranking)

df_ranking = pd.DataFrame(list_ranking, columns = ['date'] + ['w{}'.format(i+1) for i in range(len(all_words))])

df_ranking.to_csv("results.csv", sep=';', index=False, encoding ='utf8')