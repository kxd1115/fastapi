# @Coding: utf-8
# @Time: 2024/4/27 11:10
# @User: Administrator

from fastapi import Depends, HTTPException, status
import jwt
from fastapi.security import OAuth2PasswordBearer
from dependencies import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from database.crm import CrmUser

# 拿到当前登录用户的路由地址中拿到token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data):
    # token的过期时间
    access_token_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode(
        # 存入对应的用户信息
        {
            "sub": data,
            "exp": access_token_expires
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return access_token

# 解码token的方式（解码当前登录用户的token，验证数据是否正确，处理报错）
def decode_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = {"username": username}
    except:
        raise credentials_exception
    return token_data

async def get_current_user(token_data: dict = Depends(decode_token)):
    username = token_data.get("username")
    # 从数据库中获取当前登录用户的用户信息
    user = await CrmUser.get(username=username).values('id', 'username', 'name_cn', 'title', 'department__name')
    return user