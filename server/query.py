# routers/database.py
from fastapi import APIRouter, Depends
from database import get_db, AsyncSession, text

router = APIRouter()

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