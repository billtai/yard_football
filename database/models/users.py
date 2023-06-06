from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from sqlalchemy.dialects.mysql import BIGINT
from database import db
from database.models.xac_thuc import AccuracyModel


class Users(AccuracyModel):
    __tablename__ = 'users'
    id              = Column('id', BIGINT(unsigned=True),primary_key=True, autoincrement=True)
    name            = Column('name', String(length=50), default=None, nullable=True)
    username        = Column('username', String(length=50), nullable=True)
    email           = Column('email', String(length=50), nullable=True)
    phone           = Column('phone', String(length=50), nullable=True)
    password        = Column('password', String(length=250))
    status          = Column('status', Boolean, default=False)
    account_type    = Column('account_type', Integer, default=0, nullable=True)
    avatar          = Column("avatar", String(length=255), nullable=True)

    created_at              = Column('created_at', DateTime, nullable=True)
    updated_at              = Column('updated_at', DateTime,nullable=True, onupdate=db.func.now())
    deleted_at              = Column('deleted_at', DateTime, nullable=True)


    def __init__(self, data):
        super().__init__(data)
        pass
