from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import JWTError
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
from .database import get_db
from . import auth,models



def current_user(
        token:str=Depends(oauth2_scheme), #fetch the access token from the http reuqest
        db:Session=Depends(get_db)

):
    print(2)

    credential_exception=HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
       
    )
    try:
        payload=auth.decode_token(token)
        print(payload)

        if payload.get('type')!='access':
            raise credential_exception


        user_id:int=payload.get('sub')

        if user_id  is None:
            raise credential_exception

    except JWTError:
        raise credential_exception

    user=auth.get_user1(db,user_id)

    if user is None:
        raise credential_exception


    return user








    


    
    