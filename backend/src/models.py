import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/botdb')

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class UserStat(Base):
    __tablename__ = 'user_stats'
    id = Column(Integer, primary_key=True)
    discord_id = Column(String, unique=True)
    stat_name = Column(String)
    stat_value = Column(Integer)

def init_db():
    Base.metadata.create_all(engine)
