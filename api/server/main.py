# main.py
from fastapi import FastAPI
from routers.database import engine, Base
from routers import database  # Import your router

app = FastAPI()

# Create tables at startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Register the router
app.include_router(database.router)

@app.get("/")
def home():
    return {"message": "Student Performance Analysis!"}
