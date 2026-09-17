from sqlalchemy import String,Integer
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import ForeignKey

from .database import Base





class User(Base):
    __tablename__ = "users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    email:Mapped[str]=mapped_column(String(50))
    hashed_password:Mapped[str]=mapped_column(String(100))
    profile:Mapped["Profile"]=relationship(
        back_populates='user'
    ) 
    course:Mapped[list["Course"]]=relationship(
        back_populates='user'
    )
    course_purchase:Mapped[list['Course_purchase']]=relationship(
            back_populates='purchase_user'
        )



    



class Profile(Base):
    __tablename__ = 'profiles'
    id:Mapped[int]=mapped_column(primary_key=True)
    bio:Mapped[int]=mapped_column(String(100),nullable=True,default="helo everyone")
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id",ondelete="CASCADE"),unique=True)
    user:Mapped['User']=relationship(
        back_populates='profile'
    )


class Course(Base):
     __tablename__ ="courses"
     id:Mapped[int]=mapped_column(primary_key=True)
     name:Mapped[str]=mapped_column(String(100))
     price:Mapped[int]=mapped_column(Integer)
     user_id:Mapped[int]=mapped_column(ForeignKey("users.id",ondelete="CASCADE"))

     user:Mapped["User"]=relationship(
         back_populates='course'
     )




class Student(Base):
    __tablename__ ="students"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    

    


class Course_purchase(Base):
    __tablename__ ="course_purchase"
    id:Mapped[int]=mapped_column(primary_key=True)
    st_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    course_id:Mapped[int]=mapped_column(ForeignKey("courses.id"))
    purchase_user: Mapped["User"] = relationship(back_populates="course_purchase")
    course: Mapped["Course"] = relationship()
    












