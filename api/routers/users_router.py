from fastapi import APIRouter


class UsersRouter:

    def __init__(self, engine, prefix):
        self.router = APIRouter()
        self.engine = engine
        self.prefix = prefix

        @self.router.get(f'{self.prefix}/')
        async def get_users():
            return self.engine.get_users()
