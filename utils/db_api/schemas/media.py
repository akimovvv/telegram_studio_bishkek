from sqlalchemy import Column, BigInteger, String, Integer, sql

from utils.db_api.db_gino import TimedBaseModel


class Media(TimedBaseModel):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    media_id = Column(String(255))
    media = Column(String(255))

    query: sql.Select