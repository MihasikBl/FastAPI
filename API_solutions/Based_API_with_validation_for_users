import uvicorn
from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI

app = FastAPI()
user_list = []

user = {
    "nickname": "Lord12345",
    "email": "cartofel@mail.org",
    "age": 14,
    "gender": "men",
    "job": "schoolboy",
}

user_list.append(user)


class UserSchema(BaseModel):
    nickname: str = Field(max_length=30)        # Validation nickname.
    email: EmailStr = Field(max_length=45)      # Validation email.
    age: int = Field(ge=14, le=150)             # Validation age. At least 14 y.o. and no more than 150 y.o.
    gender: str = Field(max_length=5)           # Validation gender.
    job: str = Field(max_length=45)             # Validation job.


@app.get("/users", tags=["users"], summary="Output all users")
def get_all_users():
    return user_list


class NewUser(BaseModel):
    nickname: str
    email: EmailStr
    age: int
    gender: str
    job: str


@app.post("/users", tags=["users"], summary="Create users")
def create_user(n_user: NewUser):
    user_list.append({
        "nickname": n_user.nickname,
        "email": n_user.email,
        "age": n_user.age,
        "gender": n_user.gender,
        "job": n_user.job,
    })
    return {"Status": "OK", "Message": "User successfully added in list"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
