from utils.timeHelpers import TimeHelper
from database import base
from settings.useJWT import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import current_app


class AccuracyModel(base):
    __abstract__ = True

    # Constructor
    def __init__(self, data):
        for key in data:
            value = data[key]
            if key == 'mat_khau':
                value = bcrypt.generate_password_hash(data[key])
            setattr(self, key, value)
        pass

    @classmethod
    def get_not_attr_password(self, field={}):
        return self.get_session().query(*[c for c in self.__table__.c if c.name != 'mat_khau']).filter_by(**field).first()

    @classmethod
    def refresh(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        token_expired = TimeHelper.getSeconds(
            current_app.config['TOKEN_EXPIRED'])
        return ({"access_token": access_token, "token_expired": token_expired}, 200)

    @classmethod
    def logout(self, jti):
        token_block = dict()
        # token_block = BlacklistTokenModel({"jti": jti})
        token_block.create_to_db()

    @classmethod
    def register(self, data):
        user = self(data)
        user.create_to_db()
        return user
