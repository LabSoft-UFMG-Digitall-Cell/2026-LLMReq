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

@router.get("/init")
async def init_db(db: AsyncSession = Depends(get_db)):
    statements = [
        "DROP TABLE IF EXISTS participants;",
        "DROP TABLE IF EXISTS tasks;",
        """
        CREATE TABLE participants (
            code TEXT, institution TEXT, course TEXT, prog_oo TEXT, soft_arch TEXT, web_tech TEXT,
            db_systems TEXT, sw_project_mgmt TEXT, requirements TEXT, agile_methods TEXT,
            llm_usage TEXT, experience TEXT, positive_llm TEXT, negative_llm TEXT,
            positive_nollm TEXT, negative_nollm TEXT, example_positive TEXT,
            example_negative TEXT, llm_influence TEXT, general TEXT, link TEXT
        );
        """,
        """
        CREATE TABLE tasks (
            code TEXT, "group" TEXT, task_id TEXT, llm TEXT, description TEXT,
            main_flow TEXT, alt_flow TEXT, time INT, grad_phd_01 INT, note01 TEXT,
            grad_phd_02 INT, note02 TEXT, grad_mean FLOAT, grad_llm FLOAT, note_llm TEXT
        );
        """
    ]

    for stmt in statements:
        await db.execute(text(stmt))

    await db.commit()
    return {"message": "Database tables initialized successfully."}

@router.get("/populate")
async def populate_db(db: AsyncSession = Depends(get_db)):
    statements = [
        f"COPY participants FROM '{os.path.join(DATA_DIR, 'participants.csv')}' WITH (FORMAT csv, DELIMITER ',', HEADER true);",
        f"COPY tasks FROM '{os.path.join(DATA_DIR, 'tasks.csv')}' WITH (FORMAT csv, DELIMITER ',', HEADER true);"
    ]

    for stmt in statements:
        await db.execute(text(stmt))

    await db.commit()
    return {"message": "Database populated with initial data."}

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

@router.get("/results")
async def get_results(db: AsyncSession = Depends(get_db)):
    query = text("""
        SELECT p.code, p.prog_oo, p.soft_arch, p.web_tech, p.db_systems, p.sw_project_mgmt, p.requirements, p.agile_methods, p.llm_usage, t.time
        FROM participants p
        JOIN tasks t ON p.code = t.code
    """)
    result = await db.execute(query)
    rows = result.mappings().all()
    return {"Results": [dict(row) for row in rows]}

@router.get("/llm_grades")
async def get_results(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT llm, grad_llm FROM tasks"))
    rows = result.mappings().all()
    return {"Grades" : [dict(row) for row in rows]}