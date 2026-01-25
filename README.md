# Replication Package

This repository contains the replication package for the study.

## Participants and Tasks Documentation (docs)

The `2026-LLMREQ/code/docs/` directory contains all documentation artifacts related to participants and experimental tasks used in the study.

### Directory structure

```text
docs/
├── participants/
│   ├── interactions_thematic_analysis/
│   │   ├── CodeBook.md
│   │   ├── Open_Coding.md
│   │   ├── User_Model_Interaction.csv
│   │   └── shared_link/
│   │       ├── P002.md
│   │       ├── P003.md
│   │       ├── ...
│   │       └── P028.md
│   ├── knowledge_experience.csv
│   ├── perceptions_thematic_analysis/
│   └── usage_llm_feedbacks.csv
│
└── tasks/
    └── tasks_results.csv
```

### Raw Interaction Data (Shared Links)
This folder contains one Markdown file per participant (e.g., `P002.md`, `P003.md`). Each file corresponds to a shared interaction link provided by the participant and contains raw interaction logs between the participant and the LLM.

👉 **[2026-LLMREQ/code/docs/participants/interactions_thematic_analysis/shared_link/](docs/participants/interactions_thematic_analysis/shared_link/P002.md)**

### Codebook

The codebook defines all codes used in the thematic analysis, including definitions, ensuring replicability.

👉 **[2026-LLMREQ/code/docs/participants/interactions_thematic_analysis/CodeBook.md](docs/participants/interactions_thematic_analysis/CodeBook.md)**

### Open Coding

This document provides the open coding applied to the interaction data and supports traceability from codes back to participant interactions.

👉 **[2026-LLMREQ/code/docs/participants/interactions_thematic_analysis/Open_Coding.md](docs/participants/interactions_thematic_analysis/Open_Coding.md)**

### Consolidated Interaction Dataset

This file aggregates information extracted from the shared interaction links into a structured dataset. It is used by the client scripts to generate the visualizations.

👉 **[2026-LLMREQ/code/docs/participants/interactions_thematic_analysis/User_Model_Interaction.csv](docs/participants/interactions_thematic_analysis/User_Model_Interaction.csv)**


### Background Knowledge and Experience

This dataset contains participants’ self-reported background knowledge and experience levels.

👉 **[2026-LLMREQ/code/docs/participants/knowledge_experience.csv](docs/participants/knowledge_experience.csv)**


### Perceptions Thematic Analysis

This directory contains materials related to the thematic analysis of participant perceptions derived from feedback regarding llm usage.

- Challenges: 👉 **[2026-LLMREQ/code/docs/participants/perceptions_thematic_analysis/Negative_Perception_Open_Coding](docs/participants/perceptions_thematic_analysis/Negative_Perception_Open_Coding.csv)**

- Benefits: 👉 **[2026-LLMREQ/code/docs/participants/perceptions_thematic_analysis/Positive_Perception_Open_Coding](docs/participants/perceptions_thematic_analysis/Positive_Perception_Open_Coding.csv)**
  
- Compilation: 👉 **[2026-LLMREQ/code/docs/participants/usage_llm_feedbacks.csv](docs/participants/usage_llm_feedbacks.csv)**


## Aplication to Analysis (code)
All executable artifacts are in `code/`:
- `data/`: datasets and database initialization script  
- `server/`: Dockerized FastAPI backend (must be running)  
- `client/`: analysis scripts that generate the figures  

### Reproducing Results
1. Run the server via Docker (`code/server/README`).
2. Run the client application (`code/client/README`).
3. Figures are generated in:
```
code/client/figs/
```

## 📊 Graph Options Explained

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

### 1️⃣ Knowledge Distribution
```text
Option: 1
Produces a distribution of participants' prior knowledge
```

![Knowledge Distribution](code/client/figs/participants_knowledge.png)

---

### 2️⃣ Experience Distribution
```text
Option: 2
Shows participants' experience levels
```

![Knowledge Distribution](code/client/figs/experience.png)

---

### 3️⃣ Boxplot – LLM Usage by Time
```text
Option: 3
Compares LLM usage considering time-related measures
```

![Knowledge Distribution](code/client/figs/boxplot_time_llm.png)

---

### 4️⃣ Boxplot – LLM Usage by Grade
```text
Option: 4
Relates LLM usage to participants' academic grades
```

![Knowledge Distribution](code/client/figs/boxplot_time_llm.png)

---

### 5️⃣ Specific Knowledge by Topic
```text
Option: 5
Currently fixed topic: `requirements`
Can be extended for other topics
```

![Knowledge Distribution](code/client/figs/requirements_knowledge_time.png)
---

### 6️⃣ Positive LLM Usage Sankey
```text
Option: 6
Visualizes positive perceptions of LLM usage
```

![Knowledge Distribution](code/client/figs/sankey_positive.png)

---

### 7️⃣ Negative LLM Usage Sankey
```text
Option: 7
Visualizes negative perceptions (e.g., overdependence, reduced learning)
```

![Knowledge Distribution](code/client/figs/sankey_negative.png)

---
### 8️⃣ Open Coding Categorization
```text
Option: 8
- Generates categorical analysis from open-ended responses
```

![Knowledge Distribution](code/client/figs/open_coding.png)

---
### 9️⃣ Interaction Flow Sankey
```text
Option: 9
Shows user–LLM interaction flows as a Sankey diagram
```

![Knowledge Distribution](code/client/figs/sankey_interactions_flows.png)

---
### 0️⃣ Exit
```text
Option: 0
```
- Terminates the program

---


