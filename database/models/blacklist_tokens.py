from database import base, db
from sqlalchemy import Column, Integer, String, DateTime



class BlacklistTokenModel(base):
    __tablename__ = 'blacklist_tokens'

    id          = Column('id', Integer, primary_key=True, autoincrement=True)
    jti         = Column('jti', String(length=300))
    created_at  = Column('created_at', DateTime,nullable=True)
    updated_at  = Column('updated_at', DateTime,nullable=True, onupdate=db.func.now())
    deleted_at  = Column('deleted_at', DateTime, nullable=True)
    
     # Constructor
    def __init__(self, data):
        for key in data:
            value = data[key]
            setattr(self, key, value)
        pass
