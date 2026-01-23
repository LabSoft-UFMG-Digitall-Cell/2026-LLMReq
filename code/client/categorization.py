import pandas as pd
import matplotlib.pyplot as plt

def open_coding_categorization():
    df = pd.read_csv("../data/User_Model_Interaction.csv")

    actor_freq = df.groupby(["actor", "code"]).size().reset_index(name="count")
    pivot = actor_freq.pivot(index="code", columns="actor", values="count").fillna(0)

    # 🔹 Remove "User " and "Model " from y-axis labels
    pivot.index = (
        pivot.index
        .str.replace("User ", "", regex=False)
        .str.replace("Model ", "", regex=False)
    )

    ax = pivot.plot(kind="barh")
    plt.xlabel("Frequency")
    plt.ylabel("Code")
    plt.title("Interactions Behaviour by Actor")
    ax.legend(title="Actor")
    plt.tight_layout()
    plt.savefig("./figs/open_coding.png")
