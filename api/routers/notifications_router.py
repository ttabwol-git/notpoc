from fastapi import APIRouter


class NotificationsRouter:

    def __init__(self, engine, prefix):
        self.router = APIRouter()
        self.engine = engine
        self.prefix = prefix

        @self.router.get(f'{self.prefix}/')
        async def get_notifications(user_id: str = None) -> list[dict]:
            return self.engine.get_notifications(user_id)

        @self.router.put(f'{self.prefix}/')
        async def get_notifications(notification_id: str = None) -> dict:
            return self.engine.read_notification(notification_id)
