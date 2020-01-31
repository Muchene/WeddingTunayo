from pydantic import BaseModel
import jwt
import bcrypt


class LoginParams(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    user_id: str
    hashed_pwd: str


def fetch_user(params: LoginParams):
    user = User(username="admin",
                hashed_pwd=b"$2b$14$oUK4hkkLBVM9sw6Tusi5yuuRZ1Rn2m2mG7xqRpEEoTDmIREgDkF0u",
                user_id="4450e9c7-d974-49bc-87f4-0e6aee7f7340")
    if bcrypt.checkpw(params.password.encode(), user.hashed_pwd.encode()):
        return user
    return None


def get_jwt(user: User):
    secret = "change_secret"
    algorithm = "HS256"
    return jwt.encode({"user_id": user.user_id}, secret, algorithm=algorithm)
