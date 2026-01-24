# Client Module – Execution Tutorial

This README provides a **step‑by‑step tutorial** on how to execute and use `main.py`, which is the interactive entry point for generating all graphs and visual analyses used in the study. The client module is responsible for **loading processed data and producing figures** (boxplots, Sankey diagrams, and categorizations) used in the analysis of LLM usage in requirements engineering.

---

## 📁 Folder Structure (Relevant Part)

```
2026-LLMReq/
├── README.md
├── docs/
└── code/
    ├── client/
    │   ├── main.py              # Entry point (interactive)
    │   ├── participants.py      # Participant background analysis
    │   ├── results.py           # Boxplots and statistical results
    │   ├── categorization.py    # Open coding analysis
    │   ├── interactions.py      # Interaction flow Sankey
    │   ├── perception.py        # Positive/Negative perception Sankey
    │   ├── data/                # CSV and processed datasets
    │   ├── figs/                # Generated figures (output)
    │   ├── requirements.txt     # Python dependencies
    │   └── env/                 # (Optional) local virtual environment
```

---

## ⚙️ Environment Setup
> **Note:** The scripts assume a local server api running.

### 1. Create and activate a virtual environment (recommended)
```bash
cd code/client
python3 -m venv env
source env/bin/activate
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Once the environment is ready, execute:

```bash
python main.py
```

You should see the following message:

```
This is the main entry point for the client API.
```

And an **interactive menu** will appear.

---

## 🧭 Interactive Menu Overview

The program runs in a loop and asks which graph you want to generate:

```
Do you want to generate any graph?
1  - Knowledge Distribution
2  - Experience Distribution
3  - Boxplot LLM usage by time
4  - Boxplot LLM usage by grade
5  - Specific Knowledge by Topic
6  - Positive LLM usage diagram
7  - Negative LLM usage diagram
8  - Open Coding Categorization
9  - Sankey Diagram
0  - Exit
```

Type the number and press **Enter**.

---

## 📂 Output

- Figures are saved in:
  ```
  code/client/figs/
  ```
- Some Sankey diagrams may also open directly in the browser (Plotly)
---