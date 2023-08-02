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

#def find_correct_position(word_list, new_word):


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

    # Aqui, queridos amigos, o que estou fazendo, È: 
    # estou organizando a lista de palavras em ordem de peso
    # esse peso é medido comparando duas palavras no trends, vendo qual é maior
    # pois isso é só o que o algoritmo precisa, NÃO FARIA SENTIDO ALGUM USAR 5 PALAVRAS NESTE CONTEXTO > : CCCCC
    # aqui é a parte complexa de fato sipa
    for i in range(1, len(complete_word_list)):
        weighted_words.insert(find_correct_position(weighted_words, complete_word_list[i]), complete_word_list[i])

    # TODO
    # 1 discover what is the upper limit and the bottom limit from the word list
    # TENDO A LISTA JÁ ORGANIZADA, O TODO ACIMA É TRIVIAL, só pegar o bottom e o top da lista, ou last e first sla foda-se

    # TODO
    # discover the value of every word comparing to the upper limit and the bottom limit
    # por que, lmao? Acho que isso já ta incluso ali em cima também
    # Acho que talvez precise disso pra montar o gráfico só. É
    # tu vai precisar do valor "da linha" de cada palavra aqui pra montar o gráfico
    # antes tu só pegou um valor pra rankear, tu nao tem a info pra fazer o gráfico e tal
    # precisa medir todo contra o maior da lista pra que tu possa montar um grafico que faça sentido. Tu entendeu pq?
    # basicamente tu mede tudo contra o maior e menor e gelzinho
    #E SE TIVER ALGUM COM ZERO BUSCAS TU CORTA DA LISTA KKKKKKKKKKKKKKK

    # TODO
    # build a graph with ALL the word using what we just gathered
    # sipa isso aqui é o que tu implementou antes olha só que útil o código ramoseano

    print("")

    # conseguir emprego
    # que tu tenha skills
    # e vai estudar
    # tu paga alguém, assim funciona o mercado de trabalho
    
    # ALGORITMO: DE ACHAR TEMPO HÁBIL
    # o que tu faz no teu dia a dia:
    # atlantos (trabalho nao remunerado)
    # ele lê (...estudo....)
    # cursos (estudo)
    # tarefas domésticas
    # sexo com travestis (as vezes e LAZER)
