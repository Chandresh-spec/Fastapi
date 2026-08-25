from sqlalchemy import String,Integer
from sqlalchemy.orm import mapped_column,Mapped

from .database import Base





class User(Base):
    __tablename__ = "canara"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    grade:Mapped[str]=mapped_column(String(10))
    info:Mapped[str]=mapped_column(String(100))
   

