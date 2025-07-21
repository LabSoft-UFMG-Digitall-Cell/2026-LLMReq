from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import SessionLocal, engine, Base

app = FastAPI()

# Dependency to get async DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

# Create tables at startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Health check route to verify if tables exist
@app.get("/health")
async def check_tables(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_name IN ('participants', 'tasks')
    """))
    tables = [row[0] for row in result.fetchall()]
    return {"existing_tables": tables}




