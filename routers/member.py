from fastapi import APIRouter, Depends

from database.crm import *
from utils.user_token import get_current_user
from tortoise import Tortoise
from status.orm_models import GetAllMemStatus

from database.sql.getAllMem import getMemCount, getMemList

memberAPI = APIRouter()

@memberAPI.get('/test')
async def read_items():
    return

# 查询单个member接口
@memberAPI.get('/')
async def get_member(member):
    mem = await CrmMember.filter(member=member)
    return mem


# 查询member列表接口
@memberAPI.get('/all')
async def list_items(
        current_page: GetAllMemStatus = Depends(),
        user: dict = Depends(get_current_user)
):
    connection = Tortoise.get_connection("pg_conn")
    # 获取前端传回来的页码和条数
    page = current_page.page
    page_size = current_page.page_size

    # 获取当前登录用户
    user = user
    user_id = user.get("id")
    user_name = user.get("username")

    # 参数page 当前页码数，page_size 每页的条目数 默认为100
    offset = (page - 1) * page_size
    limit = page_size


    # 查询总数
    sql_all = getMemCount % (user_id)
    # 查询mem列表
    sql = getMemList % (user_id, limit, offset)

    # items = await CrmMember.all().offset(offset).limit(limit).order_by("id")
    if user_name:
        items = await connection.execute_query_dict(sql)
        count = await connection.execute_query_dict(sql_all)
        total_count = count[0].get("mnum")
    return {
        # 当前页的内容
        "items": items,
        # 总页数
        "total_pages": (total_count // page_size) + (total_count % page_size > 0),
        # 当前页页码
        "current_page": page,
        "total_count": total_count,
        "username": user_name
    }






