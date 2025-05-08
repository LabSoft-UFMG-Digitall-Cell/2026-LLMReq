import pandas as pd
import sqlite3
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def positiveWordCloud():
    conn = sqlite3.connect("./database/participants.db")
    participants_df = pd.read_sql_query("SELECT * FROM Participants;", conn)

    textos_positivos = participants_df['PositivoComLLM'].dropna().str.cat(sep=' ')

    pt_manual = {
        'e', 'de', 'da', 'do', 'que', 'o', 'em', 'a', 'as', 'os', 
        'para', 'com', 'um', 'uma', 'no', 'na', 'se', 'por',
        'ao', 'à', 'dos', 'das', 'mais', 'como', 'suas'
    }
    stopwords = STOPWORDS.union(pt_manual)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=100,
        stopwords=stopwords
    ).generate(textos_positivos)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud - Positive Aspects of LLM Use", fontsize=16)
    plt.show()

def negativeWordCloud():
    # Conectar ao banco
    conn = sqlite3.connect("./database/participants.db")
    participants_df = pd.read_sql_query("SELECT * FROM Participants;", conn)

    # Texto único com pontos positivos
    textos_negativos = participants_df['NegativosComLLM'].dropna().str.cat(sep=' ')

    # Definir stop-words: as padrões + algumas em português
    '''
    pt_manual = {
        'e', 'de', 'da', 'do', 'que', 'o', 'em', 'a', 'as', 'os', 
        'para', 'com', 'um', 'uma', 'no', 'na', 'se', 'por', 'uso', 'pode',
        'ao', 'à', 'dos', 'das', 'mais', 'como', 'suas'
    }
    stopwords = STOPWORDS.union(pt_manual) 
    '''

    # Gerar nuvem de palavras ignorando as stop-words
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=100,
        #stopwords=stopwords
    ).generate(textos_negativos)

    # Exibir
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud – Negative Aspects of LLM Use", fontsize=16)
    plt.show()