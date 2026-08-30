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




class RegisterReq(BaseModel):
    name:str
    email:str
    password:str


class RegisterRes(BaseModel):
    id:int
    name:str
    email:str
    

class LoginSchema(BaseModel):
    email:str
    password:str


class LoginOutSchema(BaseModel):
    access_token:str
    refresh_token:str




class ProfileSchema(BaseModel):
    id:int
    name:str
    email:str



class CourseSchema(BaseModel):
    id:int
    name:str