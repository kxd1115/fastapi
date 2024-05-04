# @Coding: utf-8
# @Time: 2024/5/1 10:56
# @User: Administrator
from fastapi import Query
from pydantic import BaseModel
from enum import Enum

class STATUS(Enum):
    # 部门状态
    ACTIVE = 'active'
    INACTIVE = 'inactive'

class ChangeStatus(Enum):
    # 客户归属转移状态
    NORMAL = "正常"
    APPLY  = "待转移"

class GetAllMemStatus(BaseModel):
    # 获取mem列表时的参数
    page: int = Query(default=1, ge=1, description="page number")
    page_size: int = Query(default=100, description="page size")