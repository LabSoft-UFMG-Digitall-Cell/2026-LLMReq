import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from scipy.stats import shapiro, wilcoxon

def boxplotLLM(column):
    # Connect to SQLite and load data
    conn = sqlite3.connect("./database/participants.db")
    df = pd.read_sql("SELECT `Code`, `LLM?` AS llm, Time, GradeLLM, GradePhd FROM Does", conn)
    conn.close()

    # Standardize labels
    df['llm'] = df['llm'].replace({
        'Com o uso de LLM': 'With LLM',
        'Sem o uso de LLM': 'Without LLM'
    })

    # Ensure paired data
    df_pivot = df.pivot(index='Code', columns='llm', values=column).dropna()

    # Boxplot
    plt.figure(figsize=(8, 6))
    ax = df.boxplot(column=column, by='llm', grid=False)

    # Get xtick labels to align means correctly
    xticks = ax.get_xticks()
    labels = [tick.get_text() for tick in ax.get_xticklabels()]

    # Plot mean markers at correct x positions
    for x, label in zip(xticks, labels):
        group_data = df[df['llm'] == label][column]
        mean_val = group_data.mean()
        plt.plot(x, mean_val, marker='D', color='black', label='Mean' if x == xticks[0] else "")

    # Labels and layout
    plt.title(f"")
    plt.suptitle("")
    plt.xlabel("LLM Usage")
    plt.ylabel("Score")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Shapiro-Wilk test
    diffs = df_pivot['With LLM'] - df_pivot['Without LLM']
    stat, p = shapiro(diffs)
    print("Shapiro-Wilk Test for normality of differences:")
    print(f"  W = {stat:.8f}, p = {p:.8f} -> {'Normal' if p > 0.05 else 'Not normal'}")

    # Wilcoxon test
    stat, p = wilcoxon(df_pivot['With LLM'], df_pivot['Without LLM'])
    print("\nWilcoxon Signed-Rank Test:")
    print(f"  W = {stat:.8f}, p = {p:.8f} -> {'Significant difference' if p < 0.05 else 'No significant difference'}")
