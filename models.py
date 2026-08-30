from sqlalchemy import String,Integer
from sqlalchemy.orm import mapped_column,Mapped

from .database import Base





class User(Base):
    __tablename__ = "users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    email:Mapped[str]=mapped_column(String(50))
    hashed_password:Mapped[str]=mapped_column(String(100))




class Course(Base):
    __tablename__ ="courses"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    
    


