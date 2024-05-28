

class UsersEngine:

    def __init__(self, database) -> None:
        self.database = database

    async def get_users(self) -> list[dict]:
        users = list(self.database['users'].find({}))
        for user in users:
            user['_id'] = str(user['_id'])
        return users
