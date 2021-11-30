from fastapi import FastAPI

from models import User
from sample_data import sample_db


app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return sample_db;


@app.post("/api/v1/users")
async def register_user(user: User):
    sample_db.append(user)
    return {"id": user.id}
