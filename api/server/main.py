# main.py
from fastapi import FastAPI
from database import engine, Base
from routers import route_database  # Import your router

app = FastAPI()

# Register the router
app.include_router(route_database.router)

# Create tables at startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def home():
    return {"message": "Student Performance Analysis!"}
