from fastapi import FastAPI
import query
import database

app = FastAPI()
app.include_router(database.router)
app.include_router(query.router)

@app.get("/")
def home():
    return {"message": "Student Performance Analysis!"}
