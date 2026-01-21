# 2026-LLMReq

## Run
- docker compose up --build


## Usage
- On server execute init and populate routes, check tables in health and tables participants and tasks
- Create output folder figs and navigate to the client folder, run main.py, and choose a graph to display.


## Docker Commands
- sudo docker stop $(docker ps -a -q)
- sudo docker system prune -a --volumes
- sudo docker exec -it api-db-1 psql -U user -d mydatabase
- sudo docker compose down -v  # remove volumes to force re-initialization
- sudo docker compose up --build -d # run in detach mode
- sudo docker volume ls
- sudo docker volume rm sbqs-2025-llmreq_pgdata
