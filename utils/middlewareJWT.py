from utils.responseHelper import ResponseHelper
from utils.messageHelper import MessageHelper
from settings.useJWT import jwt_token
from database.models.blacklist_tokens import BlacklistTokenModel

# Check a JWT exists in the database blocklist


@jwt_token.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    """
        Return True // Block False unblock
    """
    jti = jwt_payload["jti"]
    check_token_exist=None
    # Trường hợp đại lý
    if not jwt_payload.get('is_quan_ly'):
        # Trường hợp 1: user bị khóa -> có user trong bảng khóa token
        kt_user_id = BlacklistTokenModel.find_by_fields(fields={'user_id': jwt_payload['user_id'],'is_quan_ly':False})
        if bool(kt_user_id):
            return True

        # Trường hợp 2: token bị khóa là có token trong bảng khóa token
        kt_jti = BlacklistTokenModel.find_by_fields(fields={'jti': jti})
        if bool(kt_jti):
            return True
        # Trường hợp 3: user bị mở khóa -> có user trong bảng khóa token và deleted_at != NULL
        return False
    # Trường hợp quản lý
    kt_user_id = BlacklistTokenModel.find_by_fields(fields={'user_id': jwt_payload['user_id'],'is_quan_ly':True})
    if bool(kt_user_id):
        return True
    
    # check_token_exist = BlacklistTokenModel.find_by_fields(fields={'jti': jti})
    # Rãnh chuyển sang xử lý bằng redis
    # token_in_redis = jwt_redis_blocklist.get(jti)
    check_token_exist = BlacklistTokenModel.find_by_fields(fields={'jti': jti})

    return check_token_exist is not None

# Expired token handler


@jwt_token.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return ResponseHelper.on_error(message=MessageHelper.TOKEN_EXPIRES,code=401)

# Invalid token handler


@jwt_token.invalid_token_loader
def my_invalid_token_callback(invalid_token):
    if "Only refresh tokens are allowed" in invalid_token:
        return ResponseHelper.on_error(message=MessageHelper.ONLY_REFRESH, code=401)
    if "Signature verification failed" in invalid_token:
        return ResponseHelper.on_error(message=MessageHelper.message_get_expired('Token'), code=401)
    return ResponseHelper.on_error(message=invalid_token, code=401)


# Revoked token handler
@jwt_token.revoked_token_loader
def my_revoked_token_callback(jwt_header, jwt_payload):
    return ResponseHelper.on_error(message=MessageHelper.TOKEN_LOGOUT,code=401)
    



@jwt_token.unauthorized_loader
def my_unauthorized_token_callback(jwt_payload):
    return ResponseHelper.on_error(message=MessageHelper.message_custom('Hết phiên đăng nhập','header'),code=401) 