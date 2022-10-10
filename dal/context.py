from webbrowser import get
from config.env_config import get_env
from dal.model import init_db

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger('discord.custom')

class DBContext:
    def __init__(self):
        self.__engine = create_engine(f"mysql://{get_env('db_user')}:{get_env('db_password')}@{get_env('db_server')}/{get_env('db_name')}")
        self.__session = sessionmaker(bind=self.__engine)()
        if not inspect(self.__engine).get_table_names():
            logger.info("DB Empty - Creating from model")
            init_db(self.__engine)
    