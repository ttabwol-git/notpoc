from bson import ObjectId
import datetime


class NotificationsEngine:

    def __init__(self, database):
        self.database = database

    async def get_notifications(self, user_id: str) -> list[dict]:
        # TODO: Validate user_id is a valid ObjectId
        notifications = list(self.database['notifications'].find(
            {'target': ObjectId(user_id)},
            {'target': False}
        ))
        for notification in notifications:
            notification['_id'] = str(notification['_id'])
        return notifications

    async def read_notification(self, notification_id: str) -> dict:
        # TODO: Validate user_id is a valid ObjectId
        result = self.database['notifications'].update_one(
            {'_id': ObjectId(notification_id)},
            {'$set': {'opened_at': datetime.datetime.now(datetime.UTC)}}
        )
        return {'result': result.acknowledged}
