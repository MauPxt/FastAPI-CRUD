from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('nome', String(255)),
    Column('curso', String(255)),
    Column('idade', Integer),
    Column('nacionalidade', String(255))
)
