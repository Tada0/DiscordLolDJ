from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    voice_channel_id = Column(String(50))
    username = Column(String(50))
    summoner_name = Column(String(50)) 


def init_db(engine):
    Base.metadata.create_all(engine)