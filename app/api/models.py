
from sqlalchemy import Binary, Column, Integer, String
from app import db, login_manager

from json import JSONEncoder, JSONDecoder



class Input(db.Model):
    """
    Input Class
    """
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)
    desc = Column(String)
    data = Column(String)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)
    
    def __str__(self):
        return ','.join([self.id, self.text, self.desc, self.data])




class Output(db.Model):
    """
    Output Class
    """
    __tablename__ = 'outputs'

    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)
    desc = Column(String)
    data = Column(String)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)




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




#region Encoder

class InputEncoder(JSONEncoder):
    def default(self, o: Input):
        return {"id": o.id, "text": o.text, "desc": o.desc, "data": o.data}


class OutputEncoder(JSONEncoder):
    def default(self, o: Output):
        return {"id": o.id, "text": o.text, "desc": o.desc, "data": o.data}


class DataEncoder(JSONEncoder):
    def default(self, o: Data):
        return {"id": o.id, "text": o.text, "desc": o.desc, "data": o.data}

 