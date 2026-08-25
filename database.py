from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
DATABASE_URL = "postgresql+psycopg2://postgres:Moger%40123@localhost:5432/sir"
from sqlalchemy.orm import DeclarativeBase

engine=create_engine(DATABASE_URL)


Session_local=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine

)



class Base(DeclarativeBase): 
     pass





def get_db():
    db=Session_local()

    try:
        yield db 
    finally:
        db.close()



