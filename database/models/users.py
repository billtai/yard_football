from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.mysql import BIGINT
from database import db
from database.models.accuracy import AccuracyModel


class UsersModel(AccuracyModel):
    __tablename__ = 'users'
    id              = Column('id', BIGINT(unsigned=True),primary_key=True, autoincrement=True)
    username        = Column('username', String(length=50), nullable=True)
    name            = Column('name', String(length=50), default=None, nullable=True)
    password        = Column('password', String(length=250))
    email           = Column('email', String(length=50), nullable=True)
    phone           = Column('phone', String(length=50), nullable=True)
    address         = Column('address', String(length=250), nullable=True)

    status          = Column('status', Boolean, default=False)
    account_type    = Column('account_type', Integer, default=0, nullable=True)
    avatar          = Column("avatar", String(length=255), nullable=True)
    role_id         = Column('role_id', BIGINT, nullable=True)

    created_at              = Column('created_at', DateTime, nullable=True)
    updated_at              = Column('updated_at', DateTime,nullable=True, onupdate=db.func.now())
    deleted_at              = Column('deleted_at', DateTime, nullable=True)

    # Constructor

    def __init__(self, data):
        for key in data:
            value = data[key]
            setattr(self, key, value)
        pass
