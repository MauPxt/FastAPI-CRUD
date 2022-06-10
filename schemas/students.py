from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    curso: str
    idade: int
    nacionalidade: str
