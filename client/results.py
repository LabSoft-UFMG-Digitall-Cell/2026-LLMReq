import requests
import pandas as pd
import matplotlib.pyplot as plt

def boxplotLLM(column):
    # Get tasks data from FastAPI
    url = "http://localhost:8000/tasks"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    tasks = response.json()["Tasks"]

    # Convert to DataFrame
    df = pd.DataFrame(tasks)

    # Rename and standardize LLM labels
    df['llm'] = df['llm'].replace({
        'Com o uso de LLM': 'With LLM',
        'Sem o uso de LLM': 'Without LLM'
    })

    # Drop rows where selected column is null
    df = df.dropna(subset=[column, 'llm'])

    # Plot boxplot
    plt.figure(figsize=(8, 6))
    ax = df.boxplot(column=column, by='llm', grid=False)

    # Plot mean markers
    xticks = ax.get_xticks()
    labels = [tick.get_text() for tick in ax.get_xticklabels()]
    for x, label in zip(xticks, labels):
        group_data = df[df['llm'] == label][column]
        mean_val = group_data.mean()
        plt.plot(x, mean_val, marker='D', color='black', label='Mean' if x == xticks[0] else "")

    # Final touches
    plt.title("")
    plt.suptitle(f"")
    plt.xlabel("LLM Usage")
    if column == 'time':
        plt.ylabel("Time (minutes)")
        plt.legend()
        plt.tight_layout()
        plt.savefig("./figs/boxplot_time_llm.png")
    elif column == 'grad_phd':
        plt.ylabel("Grade")
        plt.legend()
        plt.tight_layout()
        plt.savefig("./figs/boxplot_grade_llm.png")
