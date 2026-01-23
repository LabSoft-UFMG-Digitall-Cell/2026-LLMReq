# Server Module – Execution Guide

This guide describes **how to run the server exclusively using Docker**. A local Python environment is **not required**. Docker and Docker Compose must be installed beforehand.

---

## 🐳 Prerequisites

- Docker
- Docker Compose (v2+)

Verify installation:
```bash
docker --version
docker compose version
```

---

## 📁 Structure

```
code/
├── docker-compose.yml
├── data/
│   ├── participants.csv
│   ├── tasks.csv
│   └── init.sql
└── server/
    ├── main.py
    ├── database.py
    ├── query.py
    ├── requirements.txt
    └── dockerfile
```

---

## 🐘 Database Initialization

The PostgreSQL container automatically initializes the database using the SQL script mounted at:

```
./data → /docker-entrypoint-initdb.d
```

### Tables created at startup

- `participants`
- `tasks`

### Initialization script (executed automatically)

- Drops existing tables (if any)
- Creates tables
- Loads CSV data using `COPY`

No manual database setup is required.

---

## ▶️ Starting the Server Stack

From the `code/` directory, run:

```bash
docker compose up --build
```

This command will:

1. Start a PostgreSQL 16 container
2. Build the FastAPI server image
3. Run the API using Uvicorn

---

## 🌐 Service Endpoints

Once running, the services are available at:

- **API root**: http://localhost:8000
- **Health check**: http://localhost:8000/health

Expected health response:
```json
{
  "existing_tables": ["participants", "tasks"]
}
```

---