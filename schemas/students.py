from pydantic import BaseModel


class Student(BaseModel):
    nome: str
    curso: str
    idade: int
    nacionalidade: str
