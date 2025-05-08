import pandas as pd
from scipy.stats import shapiro, kruskal
import seaborn as sns
import matplotlib.pyplot as plt

def knowledge(topic):
    # Object-Oriented Programming	
    # Software Architecture	Web Technologies	
    # Database Systems
    # Software Project Management	
    # Requirements Engineering or Software Analysis	
    # Agile Software Development Methods	
    # Use of LLMs in Software Development
    result = pd.read_csv('./docs/Result.csv')

    # Map input responses to levels
    mapping = {
        'Nunca ouvi falar': 'Low',
        'Já ouvi falar': 'Low',
        'Conheço o tópico': 'Medium',
        'Consigo ministrar': 'High',
        'Sou especialista': 'High'
    }

    # Select and transform relevant columns
    result[topic] = result[topic].replace(mapping)
    result = result.rename(columns={topic: 'A'})
    df = result[['Time', 'A']]

    # Shapiro-Wilk test for normality
    print("Shapiro-Wilk Normality Test:")
    for group in df['A'].unique():
        group_data = df[df['A'] == group]['Time']
        stat, p = shapiro(group_data)
        print(f"- {group}: p = {p:.4f} ({'Not normal' if p < 0.05 else 'Normal'})")

    # Kruskal-Wallis test
    groups = [g['Time'].values for _, g in df.groupby('A')]
    stat, p = kruskal(*groups)
    print(f"\nKruskal-Wallis Test: H = {stat:.4f}, p = {p:.4f}")

    # Boxplot
    df.boxplot('Time', by='A')
    plt.title(f'Response Time by Knowledge Level: {topic}')
    plt.xlabel('Knowledge Level')
    plt.ylabel('Time')
    plt.tight_layout()
    plt.show()

    if ( p > 0.05):
        print('The level of knowledge in the topic does not appear to have a statistically significant impact on the response time.')
    else:
        print('The level of knowledge in the topic have a statistically significant impact on the response time.')

    return df, groups, stat, p

