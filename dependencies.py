# @Coding: utf-8
# @Time: 2024/4/27 11:11
# @User: Administrator

# 依赖注入相关

####
# IP白名单
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://192.168.1.16:3000",
    "http://192.168.1.1"
]

####
# 生成的secret_key，应该妥善保存，并不要暴露在文件中，要加密存储；它应该是保密的，并且仅由后端服务器知道。在实际应用中，您应该使用一个足够复杂的随机字符串作为密钥。
SECRET_KEY = "AAAAB3NzaC1yc2EAAAADAQABAAABgQDORkJWz+OwcggCKjP+JdgBNofGh7SguNgmqrEEreKNywyXsWCtk2l498hyyN3UfLPrHC1qDxEfiVxeNr7M7/vsVY+x1sL34T9mclKafy3JYhQpi39vnQ8mUbuyes96uvOOpZe/HC/YN55udFiZQkicSLfrL4NhkjN42pufws3JJDuZLYzEr1zoGK2m61wZsPGiM7k/cwjZONbzKhGsEPx42m+3JqTLHAWFCPegB28u4z0hcKvUxwsuuhfYBmPrKuXD1m5TDy35wbWCkrhhy8ualpPr1qnQqN2jnWxloAOvbpMcn6aLVdEGaIjqkh4+VVanJIdtZVtJyuQpAJrEhySdV3/K8HcLRvwQSyse2HUBH+cM28gI1DhsuBjnBaRozQXwaHyzREHpdhYMq/x6kUT2/li0nYV6tlQe30GUYw6DEluP8/fwPHzpEODwR22ZHNeJJ2xiF20r/vrVibjGxe2bqNlhJtwdgQncM5LEVGrXF55PCbESxA3jCTzLmuP0xP8"
# 指定用于签名JWT的算法，这是一种常用的对称加密算法，意味着使用同一个密钥（即SECRET_KEY）既用于生成签名，也用于验证签名。
ALGORITHM = "HS256"
# 定义了生成的访问令牌（access token）的有效期，以分钟为单位
ACCESS_TOKEN_EXPIRE_MINUTES = 480

