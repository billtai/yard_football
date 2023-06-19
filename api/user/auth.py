from flask_restx import Resource
from api.user.__namespace__ import api
from database.models.blacklist_tokens import BlacklistTokenModel
from database.models.users import UsersModel
from utils.UserGeneralHelper import UserGeneralHelper
from utils.validateHelper import ValidateHelper, ValidationError
from utils.responseHelper import ResponseHelper
from utils.messageHelper import MessageHelper
from settings.useJWT import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, jwt_required
from utils.timeHelpers import TimeHelper
from flask import current_app
from datetime import timedelta
from settings.useJWT import jwt_token as jwt
from api.user.__scheme_input__ import login_input


@api.doc(security='bearer')
class Authentication(Resource):

    @api.doc(security=[])
    @api.doc(body=login_input)
    def post(self):
        """
        User Login
        """
        try:
            ValidateHelper.str_length(payload=api.payload, field="username", custom_field='Tên đăng nhập', max=20)
            ValidateHelper.str_length(payload=api.payload, field="password", custom_field='Mật khẩu', max=50)
        except ValidationError as err:
            return ResponseHelper.on_error(err.messages)
        payload = api.payload
        check_account = UsersModel.find_by_fields(fields={'username': payload['username']})

        if not check_account:
            return ResponseHelper.on_error(MessageHelper.message_not_exists('Tài khoản'))


        if not bcrypt.check_password_hash(check_account.password, payload['password']):
            return ResponseHelper.on_error(MessageHelper.PASS_WORD_INVALID)

        create_info_token = {"id": check_account.id, }
        additional_claims = {'user_id': check_account.id, "username": check_account.username, "role_id": check_account.role_id}

        expires = timedelta(days=current_app.config['TOKEN_EXPIRED'])

        access_token = create_access_token(identity=create_info_token, expires_delta=expires, additional_claims=additional_claims)
        token_expired = TimeHelper.getSeconds(current_app.config['TOKEN_EXPIRED'])

        return ResponseHelper.on_success(message=MessageHelper.LOGIN_SUCCESS,
                                         data={"access_token": access_token,"token_expired": token_expired,})

    # -----------------------------------------------------------------
    # Đăng xuất
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload["jti"]
        token = BlacklistTokenModel.count_fields(BlacklistTokenModel.jti == jti)
        if token == 1:
            return token is not None

    @jwt_required()
    def delete(self):
        """
        Đăng xuất.
        """
        jti = ''
        try:
            jti = get_jwt()["jti"]
        except Exception as e:
            return ResponseHelper.on_error(message=MessageHelper.NO_GET_TOKEN, code=400)
        UsersModel.logout(jti)
        return ResponseHelper.on_success(message=MessageHelper.LOGOUT_SUCCESS, code=200)
