import pandas as pd
from scipy.stats import shapiro, kruskal
import seaborn as sns
import matplotlib.pyplot as plt

def knowledgeHeatMap():
    # Carregar os dados do CSV
    df = pd.read_csv('./docs/participantes_knowledge.csv')
    df = df.set_index('Code')
    # Criar o heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=True, cmap='gray_r', vmin=0, vmax=4)  # Alterado para escala de cinza e invertida (gray_r)
    plt.title('Participants Knowledge')
    plt.show()

def knowledgeSpecificByTime(topic):
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

    # print("Shapiro-Wilk Normality Test:")
    for group in df['A'].unique():
        group_data = df[df['A'] == group]['Time']
        shapiro(group_data)
        # print(f"- {group}: p = {p:.4f} ({'Not normal' if p < 0.05 else 'Normal'})")
    
    # Kruskal-Wallis test
    groups = [g['Time'].values for _, g in df.groupby('A')]
    stat, p = kruskal(*groups)
    print(f"\nKruskal-Wallis Test: H = {stat:.4f}, p = {p:.4f}")

    message = ""

    if ( p > 0.05):
        message = 'The level of knowledge in the topic does not appear to have a statistically significant impact on the response time.'
    else:
        message = 'The level of knowledge in the topic have a statistically significant impact on the response time.'

    return df, message

def knowledgeBoxplot(topic):
    """
    This function generates a boxplot of response times for different knowledge levels
    on the topic.
    
    Parameters:
    topic (str): The topic for which to generate the boxplot.
    
    Returns:
    None: Displays the boxplot.
    """
    df, message = knowledgeTest(topic)
    print(df)

    # Boxplot
    plt.figure(figsize=(8, 6))
    df.boxplot('Time', by='A')
    plt.title(f'Response Time by Knowledge Level: {topic}')
    plt.xlabel('Knowledge Level')
    plt.ylabel('Time')
    plt.tight_layout()
    plt.show()
 

