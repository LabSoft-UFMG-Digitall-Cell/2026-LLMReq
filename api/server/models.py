from sqlalchemy import Column, Integer, String, Text, ForeignKey
from .database import Base

class Participant(Base):
    __tablename__ = "participants"

    code = Column(String, primary_key=True, index=True)
    institution = Column(Text)
    course = Column(Text)
    prog_oo = Column(Text)
    soft_arch = Column(Text)
    web_tech = Column(Text)
    db_systems = Column(Text)
    sw_project_mgmt = Column(Text)
    requirements = Column(Text)
    agile_methods = Column(Text)
    experience = Column(Text)
    positive_llm = Column(Text)
    negative_llm = Column(Text)
    positive_nollm = Column(Text)
    negative_nollm = Column(Text)
    example_positive = Column(Text)
    example_negative = Column(Text)
    llm_influence = Column(Text)
    general = Column(Text)
    link = Column(Text)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, ForeignKey("participants.code"))
    task_id = Column(Text)
    llm = Column(Text)
    description = Column(Text)
    main_flow = Column(Text)
    alt_flow = Column(Text)
    time = Column(Integer)
    grad_phd = Column(Integer)
    note01 = Column(Text)
    note02 = Column(Text)
