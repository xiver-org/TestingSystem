from sqlalchemy import select, insert

from .database import engine, Role


__standart_roles = [
    {
        "id": 1,
        "name": "student",
        "permissions": None
    },
    {
        "id": 2,
        "name": "teacher",
        "permissions": None
    },
    {
        "id": 3,
        "name": "moderator",
        "permissions": None
    },
    {
        "id": 4,
        "name": "admin",
        "permissions": None
    },
    {
        "id": 5,
        "name": "creator",
        "permissions": None
    }
]

async def init_roles() -> None:
    async with engine.connect() as connection:
        for role_ in __standart_roles:
            result = await connection.execute(select(Role).where(Role.id == role_['id']))
            if not result.fetchone():
                await connection.execute(insert(Role).values(**role_))
        await connection.commit()
