import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def boxplotLLM(column):
    # Conectar ao banco SQLite e carregar os dados
    conn = sqlite3.connect("./database/participants.db")
    df = pd.read_sql("SELECT `LLM?` AS llm, Time, GradeLLM FROM Does", conn)
    conn.close()

    #[FE] Criar boxplot usando matplotlib
    df['llm'] = df['llm'].replace({ 'Com o uso de LLM': 'YES', 'Sem o uso de LLM': 'NO' })
    plt.figure(figsize=(8, 6))
    df.boxplot(column, by='llm')
    plt.title("LLM Usage vs " + column)
    plt.suptitle("")  # Remove o título automático de "Boxplot grouped by"
    plt.xlabel("LLM Usage")
    plt.ylabel(column)
    plt.tight_layout()
    plt.show()