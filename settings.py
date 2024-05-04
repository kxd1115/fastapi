
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
            }
        }
    },
    'apps': {
        "models": {
          "models": ["database.student", "aerich.models"],
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
                'schema': 'crm'
            }
        }
    },
    'apps': {
        "models": {
          "models": ["database.crm", "aerich.models"],
          "default_connection": "pg_conn"
          }
        }
}
