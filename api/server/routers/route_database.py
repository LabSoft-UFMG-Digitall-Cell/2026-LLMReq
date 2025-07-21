# routers/api.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import SessionLocal

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
    result = await db.execute(text("SELECT * FROM participants"))
    participants = result.mappings().all()  # <- Use mappings()
    return {"Participants": [dict(row) for row in participants]}

@router.get("/tasks")
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM tasks"))
    tasks = result.mappings().all()  # <- Use mappings()
    return {"Tasks": [dict(row) for row in tasks]}
