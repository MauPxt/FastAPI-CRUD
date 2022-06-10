from fastapi import APIRouter

from config.db import conn
from models.index import students
from schemas.index import Student

student = APIRouter()


@student.get("/")
async def read_data():
    return conn.execute(students.select()).fetchall()


@student.get("/{id}")
async def read_data(id: int):
    return conn.execute(
        students.select().where(students.c.id == id)).fetchall()


@student.post("/")
async def write_data(student: Student):
    conn.execute(students.insert().values(
        nome=student.nome,
        curso=student.curso,
        idade=student.idade,
        nacionalidade=student.nacionalidade
    ))
    return conn.execute(students.select()).fetchall()


@student.put("/{id}")
async def update_data(id: int, student: Student):
    conn.execute(students.update().values(
        nome=student.nome,
        curso=student.curso,
        idade=student.idade,
        nacionalidade=student.nacionalidade
    ).where(students.c.id == id))
    return conn.execute(students.select()).fetchall()


@student.delete("/{id}")
async def delete_data(id:int):
    conn.execute(students.delete().where(students.c.id == id))
    return conn.execute(students.select()).fetchall()
