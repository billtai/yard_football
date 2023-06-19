from datetime import datetime, timezone
from pandas.core.frame import DataFrame
from sqlalchemy.ext.declarative import declared_attr
from database import db
import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm.query import Query
import pytz
from utils.timeHelpers import TimeHelper


class BaseModel(db.Model):
    __abstract__    = True
    __table_args__  = {'extend_existing': True}

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    def find_by_fields(cls, fields={}):
        """
        Select 1 example where {"id":id}
        """
        if hasattr(cls, 'deleted_at'):
            return cls.query.filter_by(deleted_at=None).filter_by(**fields).first()
        return cls.query.filter_by(**fields).first()

    @classmethod
    def find_fields(cls, fields_condition=None):
        """
        Select nhiều example where {"id":id}
        """
        if hasattr(cls, 'deleted_at'):
            return cls.query.filter_by(deleted_at=None).filter(fields_condition).first()
        return cls.query.filter(fields_condition).first()
    
    @classmethod
    def find_field_all(cls, fields_condition=None):
        """
        Select nhiều example where {"id":id}
        """
        if hasattr(cls, 'deleted_at'):
            return cls.query.filter_by(deleted_at=None).filter(fields_condition).all()
        return cls.query.filter(fields_condition).all()

    @classmethod
    def find_by_id(cls, _id):
        """
        Select 1 example where {"id":id}
        """
        if hasattr(cls, 'deleted_at'):
            return cls.query.filter_by(deleted_at=None).filter_by(id=_id).first()
        return cls.query.filter_by(id=_id).first()
    @classmethod
    def find_all(cls, fields={}):
        """
        Select 1 example where {"id":id}
        """
        if hasattr(cls, 'deleted_at'):
            return cls.query.filter_by(deleted_at=None).filter_by(**fields).all()
        return cls.query.filter_by(**fields).all()

    @classmethod
    def reset_db():
        """
        Drops and Creates fresh database
        """
        db.drop_all()
        db.create_all()

        return "initialize default database"

    def delete_row(self, condition={}):
        """
        xóa 1 records theo điều kiện
        """
        self.query.filter_by(condition).limit(1).first()
        self.delete_from_db()

    def save_to_db(self) -> None:
        """
        Cập nhật 1 records
        """
        self.updated_at = TimeHelper.get_date_now()
        db.session.add(self)
        db.session.commit()

    def create_to_db(self) -> None:
        """
        Thêm 1 records
        """
        self.created_at = datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh")).strftime(TimeHelper.FORMAT_TIME_Y_M_D__h_m_s)
        db.session.add(self)
        db.session.commit()

    def create_to_db_all(models) -> None:
        """
        Thêm nhiều records truyền vào array [model]
        """
        db.session.add_all(models)
        db.session.commit()

    def set_create_at(self) -> None:
        """
        Khi thêm nhiều thì nên gọi thằng này để thêm thời gian cho created_at
        """
        self.created_at = TimeHelper.get_date_now()
    def delete_from_db(self) -> None:
        """
        Xóa luôn không nên dùng
        """
        db.session.delete(self)
        db.session.commit()

    def soft_delete(self) -> None:
        """
        soft delete nên dùng
        """
        self.deleted_at = TimeHelper.get_date_now()
        db.session.commit()

    def get_session():
        """
        Lấy session hiện tại
        """
        return db.session

    def rollback_session():
        """
        Nếu như khi add data vào trong model mà chưa commit thì muốn bỏ ra thì call thằng này nó sẽ hủy session đó.
        """
        return db.session.rollback()

    @classmethod
    def update(self, _id, data={}):
        """

        """
        try:
            result = 0
            data.update({'updated_at': datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh")).strftime(TimeHelper.FORMAT_TIME_Y_M_D__h_m_s)})
            result = db.session.query(self).filter_by(id=_id).update(data)
            db.session.commit()
        except Exception as e:
            pass
        return result

    @classmethod
    def update_multiple(self, _where, data={}):
        result = 0
        try:
            result = db.session.query(self).filter_by(**_where).update(data)
            db.session.commit()
        except Exception as e:
            pass
        return result

    @classmethod
    def soft_delete_multiple(self, fields={}) -> None:
        db.session.query(self).filter_by(**fields).update({'deleted_at': TimeHelper.get_date_now()})
        db.session.commit()

    @classmethod
    def save(self):
        db.session.commit()

    @classmethod
    def read_to_df(self, stm) -> DataFrame:
        if not hasattr(self, '__bind_key__'):
            return pd.read_sql(stm.statement, stm.session.bind)
        return pd.read_sql(stm.statement, db.get_engine(None, self.__bind_key__))

    @classmethod
    def count_all(cls):
        if hasattr(cls, 'deleted_at'):
            return db.session.query(func.count(cls.id)).filter(cls.deleted_at == None).scalar()
        return db.session.query(func.count(cls.id)).scalar()
    
    @classmethod
    def count_fields(cls,fields_condition=None):
        if hasattr(cls, 'deleted_at'):
            return db.session.query(func.count(cls.id)).filter(cls.deleted_at == None).filter(fields_condition).scalar()
        return db.session.query(func.count(cls.id)).filter(fields_condition).scalar()
