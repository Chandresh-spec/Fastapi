from pydantic import BaseModel




class UserProfile(BaseModel):
    id:int
    name:str
    grade:str
    info:str


class RequestProfile(BaseModel):
    id:int
    name:str
    grade:str
    info:str




class requestlogin(BaseModel):
    name:str
    password:str

class Responsemodel(BaseModel):
    name:str



# alembic revision --autogenerate -m "create users table"