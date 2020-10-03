
from sqlalchemy import Binary, Column, Integer, String
from app import db, login_manager

from json import JSONEncoder


class Data(db.Model):
    """
    Data Class
    """
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)
    desc = Column(String)
    data = Column(String)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)


class DataEncoder(JSONEncoder):
    def default(self, o: Data):
        return {"id": o.id, "text": o.text, "desc": o.desc, "data": o.data}

