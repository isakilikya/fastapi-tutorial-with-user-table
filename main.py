from fastapi import FastAPI, HTTPException
from uuid import UUID

from models import User, UserUpdateRequest
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


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in sample_db:
        if user.id == user_id:
            sample_db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists."
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in sample_db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
