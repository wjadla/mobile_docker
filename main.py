from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id =1, name ="jamel", age = 22),
    Person(id =3, name ="alex", age = 18),
    Person(id =3, name ="ali", age = 33),
    Person(id =4, name ="mathiew", age = 29)
]


@app.get("/")
async def root():
    return {"message": "Hello World 2023"}


@app.get("/api")
async def read_root():
    print("hello")
    return DB

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
