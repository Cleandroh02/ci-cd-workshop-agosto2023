import uvicorn

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Book


app = FastAPI()

books_db = []

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    year = Column(Integer)
    pages = Column(Integer)
    isbn = Column(String)


Base.metadata.create_all(bind=engine)


@app.get("/", include_in_schema=False)
async def home():
    return {"message": "Hello Friends!!!!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)