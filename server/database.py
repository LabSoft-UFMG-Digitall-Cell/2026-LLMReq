# routers/database.py
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL").replace("postgresql://", "postgresql+asyncpg://")
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

router = APIRouter()

# Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/health")
async def check_tables(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_name IN ('participants', 'tasks')
    """))
    tables = [row[0] for row in result.fetchall()]
    return {"existing_tables": tables}

@router.get("/participants")
async def get_participants(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("""
        SELECT DISTINCT ON (code) *
        FROM participants
        ORDER BY code
    """))
    participants = result.mappings().all()
    return {"Participants": [dict(row) for row in participants]}

@router.get("/tasks")
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM tasks"))
    tasks = result.mappings().all()  # <- Use mappings()
    return {"Tasks": [dict(row) for row in tasks]}