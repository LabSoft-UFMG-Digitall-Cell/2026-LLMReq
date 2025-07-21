from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import SessionLocal, engine, Base
from .models import Participant, Task
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with SessionLocal() as session:
        yield session

# Pydantic schemas
class ParticipantCreate(BaseModel):
    code: str
    institution: Optional[str] = None
    course: Optional[str] = None
    prog_oo: Optional[str] = None
    soft_arch: Optional[str] = None
    web_tech: Optional[str] = None
    db_systems: Optional[str] = None
    sw_project_mgmt: Optional[str] = None
    requirements: Optional[str] = None
    agile_methods: Optional[str] = None
    experience: Optional[str] = None
    positive_llm: Optional[str] = None
    negative_llm: Optional[str] = None
    positive_nollm: Optional[str] = None
    negative_nollm: Optional[str] = None
    example_positive: Optional[str] = None
    example_negative: Optional[str] = None
    llm_influence: Optional[str] = None
    general: Optional[str] = None
    link: Optional[str] = None

class TaskCreate(BaseModel):
    code: str
    task_id: str
    llm: str
    description: Optional[str]
    main_flow: Optional[str]
    alt_flow: Optional[str]
    time: Optional[int]
    grad_phd: Optional[int]
    note01: Optional[str]
    note02: Optional[str]

@app.post("/participants/")
async def create_participant(part: ParticipantCreate, db: AsyncSession = Depends(get_db)):
    participant = Participant(**part.dict())
    db.add(participant)
    await db.commit()
    return {"status": "participant added"}

@app.post("/tasks/")
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    task_obj = Task(**task.dict())
    db.add(task_obj)
    await db.commit()
    return {"status": "task added"}
