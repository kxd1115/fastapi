from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 导入自带中间件
from fastapi.staticfiles import StaticFiles # 方便后续引用静态文件
from settings import origins # 导入允许访问的IP列表
from settings import ORM_STUDENT, ORM_CRM

from tortoise import Tortoise

##### 引入子路由
from routers.student import studentAPI
from routers.user import userAPI

app = FastAPI()

##### 设置允许访问的IP
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # * 代表所有IP
    allow_credentials=True,  # 是否正常认证
    allow_methods=["GET", "POST"],  # 允许的请求类型
    allow_headers=["*"]      # 自定义限制带的请求头参数
)

##### 连接ORM模型
# student模型，因为之前就已经创建，所以这里不需要进行设置初始化，数据库初始化，数据库更新上传等操作
async def init_db_student():
    # 连接之前已经创建好的表格
    await Tortoise.init(config=ORM_STUDENT)
@app.on_event("startup")
async def startup_event():
    # 启动服务
    await init_db_student()

### 连接新创建的模型，这里需要进设置初始化，数据库初始化等操作
# 设置初始化，在位于settings.py文件的文件夹中（只需要运行一次）
# aerich init -t settings.ORM_CRM
# 数据库初始化（一般只需要运行一次）
# aerich init-db

## 在每次模型有调整的时候都需要运行，要保持模型和数据库中的字段一致
# 更新模型
# aerich migrate
# 更新数据库
# aerich upgrade

# async def init_db_user():
#     # 连接新创建的模型
#     await Tortoise.init(config=ORM_CRM)
# @app.on_event("startup")
# async def startup_event():
#     # 启动服务
#     await init_db_user()

##### 引入静态文件
app.mount("/statics", StaticFiles(directory="statics"))

##### 使用子路由
app.include_router(studentAPI, tags=["学生路由-测试"])
app.include_router(userAPI, tags=["用户路由"])
