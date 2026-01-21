import pandas as pd
import plotly.graph_objects as go


def sankey_interaction_flows():
    # ----------------------------
    # Load data
    # ----------------------------
    df = pd.read_csv("../data/User_Model_Interaction.csv")

    LABEL_MAP = {
        "User Defines Template": "Defines Template",
        "User Provides Context": "Provides Context",
        "User Statement Prompt": "Statement Prompt",
        "User Contextualized Prompt": "Contextualized Prompt",
        "User Asks Improvements": "Asks Improvements",
        "User Repeat Ask": "Repeat Ask",

        "Model Confirm Instructions": "Confirm Instructions",
        "Model Adequate Solution": "Adequate Solution",
        "Model Inadequate Solution": "Inadequate Solution",
        "Model Offers Reinforcements": "Offers Reinforcements",
        "Model Explanation": "Explanation",
        "Model Asks Information": "Asks Information",
        "Model Out of Context": "Out of Context"
    }

    df["code"] = df["code"].map(lambda x: LABEL_MAP.get(x, x))
    df = df.sort_values(["participant", "turn"])

    # ----------------------------
    # Build transitions
    # ----------------------------
    transitions = []
    for _, group in df.groupby("participant"):
        codes = group["code"].tolist()
        for i in range(len(codes) - 1):
            transitions.append((codes[i], codes[i + 1]))

    trans_df = pd.DataFrame(transitions, columns=["source", "target"])
    flow = trans_df.value_counts().reset_index(name="value")

    # Filter dominant flows
    flow = flow[flow["value"] >= 3]

    labels = pd.unique(pd.concat([flow["source"], flow["target"]])).tolist()
    idx = {l: i for i, l in enumerate(labels)}

    # ----------------------------
    # Colors
    # ----------------------------
    USER_COLOR = "rgba(31,119,180,0.85)"
    MODEL_COLOR = "rgba(255,127,14,0.85)"

    USER_LABELS = {
        "Defines Template",
        "Provides Context",
        "Statement Prompt",
        "Contextualized Prompt",
        "Asks Improvements",
        "Repeat Ask"
    }

    node_colors = [
        USER_COLOR if label in USER_LABELS else MODEL_COLOR
        for label in labels
    ]

    # ----------------------------
    # Sankey
    # ----------------------------
    fig = go.Figure()

    fig.add_trace(
        go.Sankey(
            arrangement="perpendicular",
            node=dict(
                label=labels,
                color=node_colors,
                pad=25,
                thickness=18,
                line=dict(color="black", width=0.4)
            ),
            link=dict(
                source=[idx[s] for s in flow["source"]],
                target=[idx[t] for t in flow["target"]],
                value=flow["value"],
                color="rgba(160,160,160,0.4)"
            )
        )
    )

    # ----------------------------
    # Legend (dummy traces)
    # ----------------------------
    fig.add_trace(
        go.Scatter(
            x=[None], y=[None],
            mode="markers",
            marker=dict(size=14, color=USER_COLOR),
            name="User Interaction"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[None], y=[None],
            mode="markers",
            marker=dict(size=14, color=MODEL_COLOR),
            name="Model Response"
        )
    )

    # ----------------------------
    # Layout
    # ----------------------------
    fig.update_layout(
        title="Dominant User–LLM Interaction Flows (RQ4)",
        font_size=30,
        height=900,

        paper_bgcolor="white",
        plot_bgcolor="white",

        margin=dict(l=40, r=40, t=80, b=140),

        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5,
            font=dict(size=30),      # 🔹 increased legend font size
            itemwidth=80
        ),

        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )

    fig.show()
