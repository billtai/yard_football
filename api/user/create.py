from flask_restx import Resource
from api.user.__namespace__ import api
from flask_jwt_extended import jwt_required
from api.user.__scheme_input__ import user_input
from database.models.users import UsersModel
from api.__schema__ import user_schema
from utils.messageHelper import MessageHelper
from utils.responseHelper import ResponseHelper
from utils.validateHelper import ValidateHelper
from marshmallow import ValidationError


@api.doc(security='bearer')
class Create(Resource):
    @jwt_required()
    @api.doc(body=user_input)
    def post(self):
        """
        Create user
        """
        try:
            ValidateHelper.name(payload=api.payload, field="name",custom_field='Họ tên', max=255)
            ValidateHelper.code(payload=api.payload, field="username",custom_field='Tên đăng nhập', max=20)
            ValidateHelper.password(payload=api.payload, field="password",custom_field='Mật khẩu', max=20)
            ValidateHelper.email(payload=api.payload, field="email",custom_field='Email', max=255)
            ValidateHelper.phone(payload=api.payload, field="phone",custom_field='Số điện thoại', max=20)
            ValidateHelper.str_unsigned_int(payload=api.payload, field="role_id",custom_field='Chức vụ ID')
        except ValidationError as err:
            return ResponseHelper.on_error(err.messages)
        check_username = UsersModel.find_by_fields(fields={'username': api.payload['username']})
        if check_username:
            return ResponseHelper.on_error(MessageHelper.USER_EXIST)
        user = UsersModel.register(api.payload)
        user_json = user_schema.dump(user)
        return ResponseHelper.on_success(message=MessageHelper.message_add_success('Người dùng'), data=user_json)

