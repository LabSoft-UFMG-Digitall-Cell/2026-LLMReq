# Replication Package

This repository contains the replication package for the study.

## Participants and Tasks Documentation (docs)

The `docs/` directory contains all documentation artifacts related to participants and experimental tasks used in the study. It includes raw qualitative data, thematic analyses, and supporting quantitative datasets, ensuring transparency, traceability, and reproducibility of the reported results.

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


This folder contains one Markdown file per participant (e.g., `P002.md`, `P003.md`). Each file corresponds to a shared interaction link provided by the participant and contains raw interaction logs between the participant and the LLM. These files represent the primary qualitative data source.

👉 **[Access shared links](docs/participants/interactions_thematic_analysis/shared_link/)**

### Consolidated Interaction Dataset

```
docs/participants/interactions_thematic_analysis/User_Model_Interaction.csv
```

This file aggregates information extracted from the shared interaction links into a structured dataset. It is used by the client scripts to generate the visualizations.

### Open Coding Documentation

```
docs/participants/interactions_thematic_analysis/Open_Coding.md
```

This document provides the open coding applied to the interaction data and supports traceability from codes back to participant interactions.

### Codebook

```
docs/participants/interactions_thematic_analysis/CodeBook.md
```

The codebook defines all codes used in the thematic analysis, including definitions, ensuring replicability.

### Background Knowledge and Experience

```
docs/participants/knowledge_experience.csv
```

This dataset contains participants’ self-reported background knowledge and experience levels and supports knowledge and experience distribution analyses.

### LLM Usage and Feedback

```
docs/participants/usage_llm_feedbacks.csv
```

This file includes participants’ feedback on LLM usage regarding the challenge and benefits percieved.

### Perceptions Thematic Analysis

```
docs/participants/perceptions_thematic_analysis/
```

This directory contains materials related to the thematic analysis of participant perceptions derived from feedback regarding llm usage.


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
