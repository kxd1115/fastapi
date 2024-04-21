from fastapi import APIRouter

userAPI = APIRouter()

@userAPI.get('/user')
async def get_user():
    return "测试"