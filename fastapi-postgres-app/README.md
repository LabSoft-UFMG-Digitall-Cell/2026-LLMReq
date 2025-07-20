# FastAPI with PostgreSQL

This project is a FastAPI application that connects to a PostgreSQL database. It demonstrates how to set up a simple API with data validation and serialization using Pydantic, and how to manage the database schema with SQLAlchemy.

## Project Structure

```
fastapi-postgres-app
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── models.py        # SQLAlchemy models for the database schema
│   ├── schemas.py       # Pydantic schemas for data validation
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile             # Dockerfile for building the FastAPI application image
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-postgres-app
   ```

2. **Build and run the application using Docker Compose:**
   ```
   docker-compose up --build
   ```

3. **Access the FastAPI application:**
   Open your browser and go to `http://localhost:8000`. You can also access the interactive API documentation at `http://localhost:8000/docs`.

## Usage Examples

- To create a new item, send a POST request to `/items/` with the required data.
- To retrieve all items, send a GET request to `/items/`.

## Dependencies

- FastAPI
- SQLAlchemy
- psycopg2
- uvicorn

Make sure to check the `requirements.txt` file for the complete list of dependencies.

## License

This project is licensed under the MIT License.