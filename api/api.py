#!/usr/bin/env python
from fastapi import FastAPI
from models import users
import pydantic
import uvicorn

app = FastAPI()


@app.post("/login")
async def login(params: users.LoginParams):
    user: users.User = users.fetch_user(params)
    if not user:
        return {"error": "Invalid username or password"}
    else:
        return {"jwt": users.get_jwt(user)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081, log_level="info")