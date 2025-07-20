from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    code: int

class User(UserBase):
    code: int

    class Config:
        orm_mode = True