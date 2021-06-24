from sqlalchemy import Column, BigInteger, String, Integer, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    language = Column(String(100))
    gender = Column(Integer)
    age = Column(Integer)
    agreement = Column(Integer)

    query: sql.Select