from database.models import BaseModel
from utils.messageHelper import MessageHelper
from marshmallow.exceptions import ValidationError


class DBHelper:
    @classmethod
    def get_list_payload_model(self, form=[], callback=None, model=None):
        list_payload = []
        for key_item, item in enumerate(form):
            payload_item = callback(item)
            list_payload.append(payload_item)
        if len(list_payload) > 0:
            model.create_to_db_all(list_payload)
        return list_payload

    @classmethod
    def check_exist(self, key, payload):
        if key in payload:
            return payload[key] is not None and len(payload[key]) > 0
        return False

    @classmethod
    def reset_session(self, model: BaseModel, message=""):
        model.rollback_session()
        raise ValidationError(
            MessageHelper.message_access_failed(message))

    @classmethod
    def set_create_at_db(self, _model: BaseModel, _payload: dict):
        model_db = _model(_payload)
        model_db.set_create_at()
        return model_db

    @classmethod
    def luu_db(self, _model: BaseModel, _payload: dict):
        model_db = self.set_create_at_db(_model, _payload)
        model_db.create_to_db()
        return model_db
