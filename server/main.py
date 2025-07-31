# main.py
from fastapi import FastAPI
from routers.database import engine, Base
from routers import database  # Import your router

app = FastAPI()

# Register the router
app.include_router(database.router)

@app.get("/")
def home():
    return {"message": "Student Performance Analysis!"}
