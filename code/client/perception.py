import os
import plotly.graph_objects as go

# -------------------------------------------------
# Ensure output directory exists
# -------------------------------------------------
OUTPUT_DIR = "./figs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------
# Data
# -------------------------------------------------
POSITIVE_SANKEY = {
    "nodes": [
        {"name": "Time"}, {"name": "Quality"}, {"name": "Speed"},
        {"name": "Agility"}, {"name": "Precision"}, {"name": "Ease of Use"},
        {"name": "Creativity & Ideas"}, {"name": "Clarity"},
        {"name": "Standardization"}, {"name": "Context"}
    ],
    "links": [
        {"source": "Time", "target": "Speed", "value": 17},
        {"source": "Time", "target": "Agility", "value": 8},
        {"source": "Time", "target": "Precision", "value": 7},
        {"source": "Quality", "target": "Ease of Use", "value": 6},
        {"source": "Quality", "target": "Creativity & Ideas", "value": 11},
        {"source": "Quality", "target": "Clarity", "value": 7},
        {"source": "Quality", "target": "Standardization", "value": 3},
        {"source": "Quality", "target": "Context", "value": 2},
    ]
}

NEGATIVE_SANKEY = {
    "nodes": [
        {"name": "Learning"}, {"name": "Reliability"}, {"name": "Overdependence"},
        {"name": "Reduced Learning"}, {"name": "Loss of Critical Thinking"},
        {"name": "Loss of Personal Authorship"}, {"name": "Generic Output"},
        {"name": "Inaccurate"}, {"name": "Misinterpretation"},
        {"name": "Misalignment"}
    ],
    "links": [
        {"source": "Learning", "target": "Overdependence", "value": 9},
        {"source": "Learning", "target": "Reduced Learning", "value": 7},
        {"source": "Learning", "target": "Loss of Critical Thinking", "value": 6},
        {"source": "Learning", "target": "Loss of Personal Authorship", "value": 4},
        {"source": "Reliability", "target": "Generic Output", "value": 8},
        {"source": "Reliability", "target": "Inaccurate", "value": 6},
        {"source": "Reliability", "target": "Misinterpretation", "value": 5},
        {"source": "Reliability", "target": "Misalignment", "value": 3},
    ]
}

# -------------------------------------------------
# Sankey builder (IMAGE ONLY)
# -------------------------------------------------
def build_sankey(data, title, left_nodes, output_name):
    labels = [n["name"] for n in data["nodes"]]
    index = {label: i for i, label in enumerate(labels)}

    LEFT_COLOR = "rgba(31,119,180,0.85)"
    RIGHT_COLOR = "rgba(44,160,44,0.85)"

    node_colors = [
        LEFT_COLOR if label in left_nodes else RIGHT_COLOR
        for label in labels
    ]

    fig = go.Figure(
        go.Sankey(
            arrangement="perpendicular",
            node=dict(
                label=labels,
                color=node_colors,
                pad=25,
                thickness=18,
                line=dict(color="black", width=0.4),
            ),
            link=dict(
                source=[index[l["source"]] for l in data["links"]],
                target=[index[l["target"]] for l in data["links"]],
                value=[l["value"] for l in data["links"]],
                color="rgba(160,160,160,0.4)",
            ),
        )
    )

    fig.update_layout(
        title=title,
        font_size=28,
        height=800,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=40, r=40, t=80, b=140),
    )

    # ----------------------------
    # Save static images only
    # ----------------------------
    fig.write_image(os.path.join(OUTPUT_DIR, f"{output_name}.png"), scale=2)

# -------------------------------------------------
# Run
# -------------------------------------------------
def build_sankey_positive():
    build_sankey(
        POSITIVE_SANKEY,
        "Positive Perceptions of LLM Usage",
        left_nodes=["Time", "Quality"],
        output_name="sankey_positive"
    )

def build_sankey_negative():
    build_sankey(
        NEGATIVE_SANKEY,
        "Negative Perceptions of LLM Usage",
        left_nodes=["Learning", "Reliability"],
        output_name="sankey_negative"
    )

if __name__ == "__main__":
    print("Generating Positive LLM usage diagram...")
    build_sankey_positive()