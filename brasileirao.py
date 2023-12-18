import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

def tabela():
    url = 'https://www.espn.com.br/futebol/classificacao/_/liga/bra.1'

    df = pd.read_html(url)
    times_nomes = df[0].rename(columns={'2023':'Time'})
    pontuacoes = df[1]

    new_df = pd.concat([times_nomes, pontuacoes], join='inner', axis=1)

    pos_list = []
    nome_list = []
    for i in range(20):
        time = new_df['Time'].loc[i]
        if i < 9:
            pos = time[0]
            sig = time[1:4]
            nome = time[4:]
        else:
            pos = time[0:2]
            sig = time[2:5]
            nome = time[5:]

        pos_list.append(pos)
        nome_list.append(nome)

    new_df = new_df.drop(columns=['Time'])
    new_df.insert(loc=0, column='Time', value=nome_list)
    new_df.insert(loc=0, column='POS', value=pos_list)
    
    return new_df