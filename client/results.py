import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

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
    elif column == 'grad_mean':
        plt.ylabel("Grade")
        plt.legend()
        plt.tight_layout()
        plt.savefig("./figs/boxplot_grade_llm.png")
    elif column == 'grad_llm':
        plt.ylabel("LLM Grade")
        plt.legend()
        plt.tight_layout()
        plt.savefig("./figs/boxplot_grade_by_llm.png")


def positive_usage_llm():
    data = [
        ("P001", ["Speed", "Standardization", "Ease"], "Time"),
        ("P002", ["Speed", "Ease", "Ideas"], "Time"),
        ("P003", ["Time", "Creativity", "Inspiration"], "Quality"),
        ("P004", ["Ease", "Time", "Agility"], "Time"),
        ("P005", ["Agility", "Clarity", "Organization"], "Quality"),
        ("P006", ["Speed", "Precision"], "Time"),
        ("P007", ["Speed", "Standardization"], "Time"),
        ("P008", ["Speed"], "Time"),
        ("P009", ["Ease", "Interpretation", "Examples"], "Quality"),
        ("P010", ["Speed", "Practicality"], "Time"),
        ("P011", ["Practicality", "Speed", "Assistance"], "Quality"),
        ("P012", ["Practicality", "Perspectives", "Clarity"], "Quality"),
        ("P013", ["Agility", "Practicality", "Discovery"], "Time"),
        ("P014", ["Speed", "Support", "Productivity"], "Time"),
        ("P015", ["Speed", "Dynamism"], "Time"),
        ("P016", ["Ease", "Clarity", "Speed"], "Time"),
        ("P017", ["Creativity", "Ideas", "Speed"], "Quality"),
        ("P018", ["Speed", "Clarity", "Standardization"], "Quality"),
        ("P019", ["Ease", "Time", "Efficiency"], "Time"),
        ("P020", ["Agility", "Clarity", "Creativity"], "Quality"),
        ("P021", ["Speed", "Precision", "Correction"], "Time"),
        ("P022", ["Speed"], "Time"),
        ("P023", ["Speed", "Novelty", "Discovery"], "Time"),
        ("P024", ["Speed", "Practicality"], "Time"),
        ("P025", ["Ideas", "Correction", "Context"], "Quality"),
        ("P026", ["Speed", "Insights", "Agility"], "Time"),
        ("P027", ["Speed"], "Time"),
        ("P028", ["Speed", "Quality"], "Quality"),
    ]

    rows = []
    for _, keywords, class2 in data:
        for keyword in keywords:
            rows.append({
                "Benefits": "Benefits of using LLMs",
                "class01": keyword,
                "class02": class2
            })

    df = pd.DataFrame(rows)
    df_counts = df.groupby(["Benefits", "class01", "class02"]).size().reset_index(name="count")

    fig = px.sunburst(
        df_counts,
        path=["Benefits", "class01", "class02"],
        values="count",
        title="Hierarchical Diagram: Benefits -> class01 -> class02",
        color="class02",
        color_discrete_map={"Time": "lightblue", "Quality": "lightgreen"}
    )

    fig.show()