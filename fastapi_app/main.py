from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int
    email: str

class UserUpdate(BaseModel):
    name: str |None = None
    age: int |None = None
    email: str |None = None

def get_user_by_email(email):
    for user in users:
        if user["email"] == email:
            return user

    return None

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user

    return None

users = []
user_id_counter = 1

@app.get("/")
def root():
    return {"message": "用户管理系统启动成功"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="用户不存在"
        )

    return user


@app.post("/users",status_code=201)
def create_user(user_data: UserCreate):
    global user_id_counter

    existing_user = get_user_by_email(user_data.email)

    if existing_user is not None:
        raise HTTPException(
            status_code=409,
            detail="该邮箱已被注册"
        )

    user = {
        "id": user_id_counter,
        "name": user_data.name,
        "age": user_data.age,
        "email": user_data.email
    }

    users.append(user)
    user_id_counter += 1

    return user

@app.patch("/users/{user_id}")
def update_user(user_id: int, user_data: UserUpdate):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="用户不存在"
        )

    if user_data.name is not None:
        user["name"] = user_data.name

    if user_data.age is not None:
        user["age"] = user_data.age

    if user_data.email is not None:
        existing_user = get_user_by_email(user_data.email)
        if existing_user is not None and existing_user["id"] != user_id:
            raise HTTPException(
                status_code=409,
                detail="该邮箱已被注册"
            )
        user["email"] = user_data.email

    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="用户不存在"
        )

    users.remove(user)

    return {
        "message": "用户删除成功"
    }