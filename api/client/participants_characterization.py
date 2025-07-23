import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def knowledge_distribuition():
    url = "http://localhost:8000/participants"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    participants = response.json()["Participants"]
    data = {
        'Code': [entry['code'] for entry in participants],
        'Object-Oriented Programming': [entry['prog_oo'] for entry in participants],
        'Software Architecture': [entry['soft_arch'] for entry in participants],
        'Web Tecnologies': [entry['web_tech'] for entry in participants],
        'Database Systems': [entry['db_systems'] for entry in participants],
        'Project Management': [entry['sw_project_mgmt'] for entry in participants],
        'Requirements Engineering': [entry['requirements'] for entry in participants],
        'Agile Methods': [entry['agile_methods'] for entry in participants],
        'Use of LLMs': [entry['llm_usage'] for entry in participants]
    }

    # Cria o DataFrame
    df = pd.DataFrame(data)

    # Seleciona as colunas de conhecimento
    knowledge_areas = df[['Object-Oriented Programming', 'Software Architecture', 'Web Tecnologies',
                        'Database Systems', 'Project Management', 'Requirements Engineering',
                        'Agile Methods', 'Use of LLMs']]

    # Define os níveis de conhecimento
    knowledge_levels = sorted(df[knowledge_areas.columns].stack().unique())

    # Prepara os dados para o gráfico de barras horizontais acumuladas
    bar_height = 0.6
    index = range(len(knowledge_areas.columns))
    colors = ["#ffffff", "#dadada", "#8d8d8d", "#494949", "#030303"]  # Cores para cada nível

    fig, ax = plt.subplots(figsize=(10, 6))

    left = [0] * len(knowledge_areas.columns)

    for i, level in enumerate(knowledge_levels):
        counts = knowledge_areas.apply(lambda col: (col == level).sum(), axis=0)
        ax.barh(
            index,
            counts,
            height=bar_height,
            left=left,
            label=f'Level {level}',
            color=colors[i],
            edgecolor='black'  # Adiciona borda preta às barras
        )
        left = [l + c for l, c in zip(left, counts)]

    # Define os rótulos do eixo y
    english_labels = ['OOP', 'Software Arch.', 'Web Tech.', 'Database Sys.',
                    'Project Mgmt.', 'Req. Eng.', 'Agile Methods', 'Use of LLMs']
    ax.set_ylabel('Knowledge Areas')
    ax.set_xlabel('Number of Participants')
    ax.set_title('Number of Participants by Knowledge Level per Area')
    ax.set_yticks(index)
    ax.set_yticklabels(english_labels)

    # Posiciona a legenda fora do gráfico, à direita
    ax.legend(title='Knowledge Level', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)

    plt.tight_layout()
    plt.savefig("./figs/KnowledgParticipants.png")

def experience():
    url = "http://localhost:8000/participants"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    participants = response.json()["Participants"]

    # Step 2: Extract and map experience values
    experience = [entry['experience'] for entry in participants]

    label_map = {
        'Até 1 ano de experiência': 'Up to 1 year',
        '1 a 3 anos de experiência': '1 to 3 years',
        'Mais de 3 anos de experiência': 'More than 3 years',
        'Não, nunca trabalhei em uma empresa de desenvolvimento de software': 'No experience'
    }
    experience = [label_map.get(exp, exp) for exp in experience]

    # Step 3: Count and sort
    counts = Counter(experience)
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    labels, values = zip(*sorted_items)

    # Step 4: Grayscale colors
    gray_colors = ['#f2f2f2', '#c0c0c0', '#8c8c8c', '#404040']  # Adjust to number of categories
    colors = gray_colors[:len(labels)]

    # Step 5: Plot the bar chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=colors, edgecolor="black")

    # Add values on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, str(height), ha='center', va='bottom')

    plt.title("Participants by Experience Level")
    plt.xlabel("Experience")
    plt.ylabel("Number of Participants")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("./figs/experience.png")

