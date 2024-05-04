# @Coding: utf-8
# @Time: 2024/4/25 21:55
# @User: Administrator

from fastapi import APIRouter
from pydantic import BaseModel

userAPI = APIRouter()

class UserIn(BaseModel):
    username: str
    pwd: str
    name_cn: str
    title: str
    status: str
    department_id: int

@userAPI.post('/')
async def add_user():
    return { "测试" }
