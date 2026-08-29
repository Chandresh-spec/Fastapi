from fastapi import FastAPI,Query,status
from pydantic import BaseModel
from enum import Enum
from fastapi import HTTPException
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from .database import Base,engine,get_db
from .models import User
from .schemas import UserProfile,RequestProfile,RegisterReq,RegisterRes,LoginOutSchema,LoginSchema
from .auth import hash_password,authenticate_user,create_access_token,create_refresh_token

print(Base.metadata.tables)
Base.metadata.create_all(bind=engine)

app=FastAPI()





class Role(str,Enum):
    ADMIN="Admin"
    TEACHER="teacher"
    STUDENT="Student"

    



@app.get("/users/{role}")
def profile(role:Role):
    return{
        "name":role
    }



# http://127.0.0.1:8000/user/m








# @app.get("/user/{id}")
# def user_data(
#     id:int,
#     is_active:Role,
#     name:str|None=None,
   
#     ):
#     return {
#         "id":id,
#         "is_active":is_active,
#         "name":name
#     }
    

# arr=[1,2,3,4]

# for ele in range(len(arr)):
#    print(arr[ele])



class Userdata(BaseModel):
    name:str
    rollno:int
    course:str



@app.get("/req_exmple")
def req_example(user:Userdata):
      #db opertions
      return {
           "message":"user saved sucessfully"
      }




class ResponseData(BaseModel):
     name:str
     roll:int
     course:str


hashmap={
     "name":"chandresh",
     "roll":3604,
     "course":"bca"
}

@app.post("/userdata/{id}")
def res_example(id:int):
    return {
         
    }




class Reqprofile(BaseModel):
    id:int|None=0
    name:str
    age:int|None=0
    bio:str|None="helo user"


class responseProfile(BaseModel):
    bio:str|None="helo user"
    name:str|None="user"
    age:int|None=0
    



@app.post("user/profile/{id:int}",response_model=responseProfile)
def get_user_profile(user:Reqprofile):
    return user



arr=Annotated[str,Query(min_length=2,max_length=10)]
@app.get("/user/helo")
def get_helo(
    name:Annotated[list[arr]|None,Query()]=None
):
    return {
        "name":name
    }




@app.post("/user",response_model=UserProfile)
def save_user_profile(user_data:RequestProfile,db:Session=Depends(get_db)):
    
    user=User(
        name=user_data.name,
        grade=user_data.grade,
        info=user_data.info
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/user/{id}",response_model=UserProfile)
def get_user_name(id:int,db:Session=Depends(get_db)):
    user=db.query(User).where(User.id==id).scalar()
    return user


@app.put("/user/profile",response_model=UserProfile)
def update_user(user:RequestProfile,db:Session=Depends(get_db)):
    db_user=db.query(User).where(User.id==user.id).first()
    print(db_user)

    if db_user.name==user.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="name already same"
            
        )
    db_user.name=user.name
    db_user.info=user.info
    db_user.grade=user.grade
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@app.delete("/user/{id}")
def delete_user(id:int,db:Session=Depends(get_db)):
    user=db.query(User).where(User.id==id)

    user.delete()
    db.commit()
    return {
        "message":"user deleted sucessfull"
    }



@app.post("/user/register",response_model=RegisterRes)
def register(user:RegisterReq,db:Session=Depends(get_db)):

    existinng=db.execute(select(User).where(User.email==user.email)).scalar_one_or_none()
    if existinng:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email already exists"
        )

    db_user=User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password)

    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@app.post("/login")
def login(user:LoginSchema,db:Session=Depends(get_db)):
    print("hello")

    db_user=authenticate_user(user.email,user.password,db)
    print("hello2")
   
    

    if db_user is None:
         raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="user not found"
                )

    
    access_token=create_access_token({"sub":db_user.id})
    refresh_token=create_refresh_token({"sub":db_user.id})

    return {
        "access_token":access_token,
        "refresh_token":refresh_token
    }










    





