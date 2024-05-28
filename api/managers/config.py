import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI
from loguru import logger

# import routers
from users_router import UsersRouter
from notifications_router import NotificationsRouter

# import engines
from users_engine import UsersEngine
from notifications_engine import NotificationsEngine


class APIConfig:

    def __init__(self) -> None:
        load_dotenv(os.path.join(os.environ['CONFIG_PATH'], 'local.env'))
        self.app = FastAPI()
        self.logger = logger
        self.mongo = MongoClient(os.getenv('DBURI', None), tlsCAFile=certifi.where())
        self.database = self.mongo[os.environ['DBNAME']]
        RegisterRouters(self.app, self.database)


class RegisterRouters:

    def __init__(self, app, database) -> None:
        self.app = app
        self.prefix = '/api'

        self.services = [
            (UsersRouter, UsersEngine(database), '/users'),
            (NotificationsRouter, NotificationsEngine(database), '/notifications')
        ]

        for service in self.services:
            initialized_service = service[0](service[1], service[2])
            self.app.include_router(initialized_service.router, prefix=self.prefix)
