# @Coding: utf-8
# @Time: 2024/4/25 21:46
# @User: Administrator

#
from fastapi import APIRouter, Depends, HTTPException, status
#
from status.login_models import LoginRequest
from utils.user_token import create_access_token, get_current_user
# 导入数据库模型
from database.crm import *

loginAPI = APIRouter()


# 登录接口
@loginAPI.post('/')
async def login(request: LoginRequest):
    # 获取前端的账号和密码
    user = await CrmUser.get(username=request.username).values('username')
    pwd = await CrmUser.get(username=request.username).values('pwd') # .get('pwd')
    # 注意，直接通过ORM从数据库获取的数据是QuerySet格式
    username = user['username']
    password = pwd['pwd']
    # 账密验证
    if request.username == username and request.password == password:
        # token的过期时间
        access_token = create_access_token(request.username)
        # print(access_token)
        # 提供给前端的token格式
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# 获取当前登录用户信息的接口
@loginAPI.get("/profile")
async def user_msg(current_user: dict = Depends(get_current_user)):
    return {
        "user_msg": current_user
    }



