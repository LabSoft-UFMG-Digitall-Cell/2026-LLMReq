import pandas as pd
from scipy.stats import shapiro, kruskal
import seaborn as sns
import matplotlib.pyplot as plt

def experience():
    # Carregar os dados
    exp_participant = pd.read_csv('./docs/Data - csvToDB.Survey.csv', usecols=['Code', 'Experience'])

    # Agrupar e contar as ocorrências por experiência
    Pie = exp_participant.groupby('Experience').count()

    # Adicionar categoria ausente se necessário
    if 'Mais de 3 anos' not in Pie.index:
        Pie.loc['Mais de 3 anos'] = 0

    # Ordenar índices
    Pie = Pie.sort_index()

    # Criar gráfico de barras
    plt.figure(figsize=(8, 6))
    bars = plt.bar(range(len(Pie)), Pie['Code'], color='skyblue')

    # Substituir os nomes reais por letras
    plt.xticks(range(len(Pie)), ['1 a 3 anos', 'Até 1 ano', 'Mais de 3 anos', 'Não tem'])

    plt.xlabel('Experiência (codificada)')
    plt.ylabel('Número de Participantes')
    plt.title('Distribuição de Experiência dos Participantes')
    plt.tight_layout()
    plt.show()

def experienceByTime():
    # Load the dataset
    result = pd.read_csv('./docs/Result.csv')
    df = pd.DataFrame(result[['Time', 'Experience']])

    # Replace Portuguese labels with English equivalents
    label_map = {
        'Até 1 ano de experiência': 'Up to 1 year',
        '1 a 3 anos de experiência': '1 to 3 years',
        'Não, nunca trabalhei em uma empresa de desenvolvimento de software': 'No experience'
    }

    df['Experience'] = df['Experience'].replace(label_map)

    # Check normality with Shapiro-Wilk test
    print("Shapiro-Wilk Normality Test:")
    for group in df['Experience'].unique():
        group_data = df[df['Experience'] == group]['Time']
        stat, p = shapiro(group_data)
        status = "Not normal" if p < 0.05 else "Normal"
        print(f"- {group}: p = {p:.4f} ({status})")

    # Kruskal-Wallis Test (non-parametric)
    groups = [g['Time'].values for _, g in df.groupby('Experience')]
    stat, p = kruskal(*groups)
    print(f"\nKruskal-Wallis Test: H = {stat:.4f}, p = {p:.4f}")

    # Boxplot visualization
    sns.boxplot(data=df, x='Experience', y='Time')
    plt.title('Time Distribution by Experience')
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()