from fastapi import FastAPI
from models import users
import pydantic

app = FastAPI()


@app.post("/login")
async def login(params: users.LoginParams):
    user: users.User = users.fetch_user(params)
    if not user:
        return {"error": "Invalid username or password"}
    else:
        return {"jwt": users.get_jwt(user)}
