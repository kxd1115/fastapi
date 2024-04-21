import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# IP白名单
origins = [
    "http://localhost"
]

# TORTOISE_ORM设置
ORM_STUDENT = {
    "connections": {
        "pg_conn": {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': '127.0.0.1',
                'port': '5432',
                'user': 'postgres',
                'password': '1217kxd.',
                'database': 'fastapi',
                "ssl": ctx
            }
        }
    },
    'apps': {
        "models": {
          "models": ["models.student", "aerich.models"],
          "default_connection": "pg_conn"
          }
        }
}

ORM_CRM = {
    "connections": {
        "pg_conn": {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': '127.0.0.1',
                'port': '5432',
                'user': 'postgres',
                'password': '1217kxd.',
                'database': 'fastapi',
                "ssl": ctx
            }
        }
    },
    'apps': {
        "models": {
          "models": ["models.user", "aerich.models"],
          "default_connection": "pg_conn"
          }
        }
}