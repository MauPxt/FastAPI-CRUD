from fastapi import FastAPI
from routes.index import student

app = FastAPI()

app.include_router(student)