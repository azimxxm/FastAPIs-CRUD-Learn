from fastapi import FastAPI
from typing import  List
from uuid import  UUID,  uuid4
from models import User, Gender, Role, UserUpdateRequest
from fastapi import HTTPException


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Azimjon",
        last_name="Abdurasulov",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Azizbek",
        last_name="Ikromov",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Azimjon"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.midle_name is not None:
                user.midle_name = user_update.midle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists "
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exists"
    )
