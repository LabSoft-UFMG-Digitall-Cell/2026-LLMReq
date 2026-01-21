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

    df = pd.DataFrame(data)
    knowledge_areas = df[['Object-Oriented Programming', 'Software Architecture', 'Web Tecnologies',
                        'Database Systems', 'Project Management', 'Requirements Engineering',
                        'Agile Methods', 'Use of LLMs']]

    knowledge_levels = sorted(df[knowledge_areas.columns].stack().unique())

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
            edgecolor='black'
        )
        left = [l + c for l, c in zip(left, counts)]

    english_labels = ['OOP', 'Software Arch.', 'Web Tech.', 'Database Sys.',
                    'Project Mgmt.', 'Req. Eng.', 'Agile Methods', 'Use of LLMs']
    ax.set_ylabel('Knowledge Areas', fontsize=18)
    ax.set_xlabel('Number of Participants', fontsize=18)
    ax.tick_params(axis='x', labelsize=14)
    ax.set_title('Number of Participants by Knowledge Level per Area', fontsize=20)
    ax.set_yticks(index)
    ax.set_yticklabels(english_labels, fontsize=16)

    ax.legend(
        title='Knowledge Level',
        fontsize=16,         
        title_fontsize=18,
        bbox_to_anchor=(1.02, 1),
        loc='upper left',
        borderaxespad=0.
    )

    plt.tight_layout()
    plt.savefig("./figs/participants_knowledge.png")

def experience():
    url = "http://localhost:8000/participants"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    participants = response.json()["Participants"]

    # Extract experience values
    experience = [entry['experience'] for entry in participants]

    label_map = {
        'Até 1 ano de experiência': 'Up to 1 year',
        '1 a 3 anos de experiência': '1 to 3 years',
        'Mais de 3 anos de experiência': 'More than 3 years',
        'Não, nunca trabalhei em uma empresa de desenvolvimento de software': 'No experience'
    }
    experience = [label_map.get(exp, exp) for exp in experience]

    # Count occurrences
    counts = Counter(experience)

    # Explicit y-axis order (semantic order)
    desired_order = [
        "No experience",
        "Up to 1 year",
        "1 to 3 years",
        "More than 3 years"
    ]

    labels = [label for label in desired_order if label in counts]
    values = [counts[label] for label in labels]

    # Plot
    plt.figure(figsize=(9, 5))
    bars = plt.barh(labels, values, color="0.7", edgecolor="black")

    # Value labels
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + 0.1,
            bar.get_y() + bar.get_height() / 2,
            str(width),
            va="center",
            fontsize=16
        )

    plt.title("Participants by Experience Level", fontsize=22)
    plt.xlabel("Number of Participants", fontsize=20)
    plt.ylabel("Experience Level", fontsize=20)

    # Increase tick label font size
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.grid(axis="x", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig("./figs/experience.png", dpi=300)
    plt.close()


def specific_knowledge_by_time(topic = 'requirements'):
    # Step 1: Request data from the API with topic as a query param
    url = "http://localhost:8000/results"
    headers = {"accept": "application/json"}
    params = {"topic": topic}
    response = requests.get(url, headers=headers, params=params)

    # Step 2: Extract and convert to DataFrame
    data = response.json()
    results = data.get("Results", data)  # Handle wrapped or direct response
    df = pd.DataFrame(results)

    # Step 3: Rename the column of interest to a common name 'A' if needed
    # You may skip this if column is already 'A'
    # Step 1: Rename the column
    df = df.rename(columns={topic: 'A'})

    # Step 2: Map numeric values to categorical strings
    mapping = {
        '1': 'Low',
        '2': 'Low',
        '3': 'Medium',
        '4': 'High',
        '5': 'High'
    }
    df['A'] = df['A'].astype(str).replace(mapping)

    # ✅ Step 3: Define the categorical order
    category_order = ['Low', 'Medium', 'High']
    df['A'] = pd.Categorical(df['A'], categories=category_order, ordered=True)

    # Step 4: Plot the boxplot
    plt.figure(figsize=(8, 6))
    df.boxplot('time', by='A', grid=False)
    plt.title('Knowledge Level Impact on Response Time')
    plt.suptitle('')  # Remove default automatic title
    plt.xlabel(f'Knowledge Level on {topic}')
    plt.ylabel('Time (minutes)')
    plt.tight_layout()
    plt.savefig(f"./figs/{topic}_knowledge_time.png")
