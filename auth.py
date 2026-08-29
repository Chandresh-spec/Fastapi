from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends
from .database import Base,engine,get_db
from fastapi import FastAPI,Query,status
from pydantic import BaseModel
from enum import Enum
from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import User

from jose import jwt,JWTError
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
from datetime import datetime, timedelta, timezone

SECRET_KEY ="my-super-secret-key-123456789"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=50
REFRESH_TOKEN_EXPIRE_DAY=7

def hash_password(password:str):
     return pwd_context.hash(password)

def verify_password(password:str,hashed_password):
     return pwd_context.verify(password,hashed_password)

    
def get_user(db:Session,email:str):
     return db.query(User).filter(User.email==email).first()

 
            
       


def authenticate_user(email:str,password:str,db=Session)->bool:
     user=get_user(db,email)
     print(user)
     
     
     if user is None:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail="user does not exists"
          )

     

     passowrd_verify=verify_password(password,user.hashed_password)

     if not passowrd_verify:
                    raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail="password is incorrect"
          )

     return user



def create_access_token(data:dict):
      to_encode=data.copy()
      exp= datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
      to_encode.update({
             "exp":exp,
             "type":"access"
      }
      )

      return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

       

     
def create_refresh_token(data:dict):
      to_encode=data.copy()
      exp= datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAY)
      to_encode.update({
             "exp":exp,
             "type":"access"
      }
      )

      return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


