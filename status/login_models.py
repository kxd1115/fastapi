# @Coding: utf-8
# @Time: 2024/4/27 11:08
# @User: Administrator

from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str