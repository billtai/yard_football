from utils.messageHelper import MessageHelper
from marshmallow import fields
from marshmallow.exceptions import ValidationError
import re

PATTERN_EMAIL_FIRST = re.compile(r'^[a-zA-Z0-9]\S+$')
PATTERN_STATUS = re.compile(r'^[01]{1}$')
PATTERN_UNSIGNED_INTERGER = re.compile(r'^[0-9]+$')
PATTERN_CODE = re.compile(r'^[a-zA-Z0-9-_]+$')
PATTERN_USER_NAME = re.compile(r'^[a-zA-Z0-9_\.]+$')
PATTERN_NAME = re.compile(
    r'^[a-z0-9A-Z_\sÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệếỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹý]+$')
PATTERN_EMAIL = re.compile(
    r'^[^\W][a-zA-Z0-9-_\\.]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
# PATTERN_EMAIL_STRONG = re.compile(
#     r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
PATTERN_EMAIL_STRONG = re.compile(
    r'^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})'
)

PATTERN_STR_INTERGER_NOT_SPECIAL = re.compile(r'^[a-zA-Z0-9]+$')


PATTERN_PHONE = re.compile(r'(0[3|5|7|8|9])+([0-9]{8})\b')
PATTERN_PHONE_NO_CHECK_REFIX = re.compile(r'(0[0-9])+([0-9]{8})\b')
PATTERN_PHONE_INTERNATIONAL_AREA_CODE = re.compile(r'^([0-9]{11})$')

PATTERN_PASSWORD = re.compile(r'([0-9]{1,8})\b')
PATTERN_PASSWORD_STRONG = re.compile((
    r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$')
)

PATTERN_MONEY = re.compile(r'^[0-9]\d*(\.\d{1,2})?$')

PATTERN_MONEY_LIMIT = re.compile(r'^[0-9]+$|^$|^\s$')


class IsPhoneHelper(fields.Str):
    def _validate(self, value):
        # if value.startswith("84"):
        #     if not re.fullmatch(PATTERN_PHONE_INTERNATIONAL_AREA_CODE, value):
        #         raise ValidationError(MessageHelper.INVALID_VIET_NAME)
        #     return super()._validate(value)
        if not re.fullmatch(PATTERN_PHONE, value):
            raise ValidationError(MessageHelper.INVALID_PHONE_FORMAT)
        return super()._validate(value)


class IsEmailHelper(fields.Str):
    def _validate(self, value):

        # if not re.fullmatch(PATTERN_EMAIL_FIRST, value):
        #     raise ValidationError(MessageHelper.INVALID_EMAIL_FORMAT)

        # if not re.fullmatch(PATTERN_EMAIL, value):
        #     raise ValidationError(MessageHelper.INVALID_EMAIL_FORMAT)

        if not re.fullmatch(PATTERN_EMAIL_STRONG, value):
            raise ValidationError(MessageHelper.INVALID_EMAIL_FORMAT)

        return super()._validate(value)


class IsStatusHelper(fields.Int):
    def _validate(self, value):
        if not re.fullmatch(PATTERN_STATUS, str(value)):
            raise ValidationError(MessageHelper.STATUS_ACCEPT)
        return super()._validate(value)


class IsPasswordHelper(fields.Str):
    def _validate(self, value):
        if not re.fullmatch(PATTERN_PASSWORD_STRONG, value):
            raise ValidationError(MessageHelper.INVALID_PASSWORD)
        return super()._validate(value)


class IsUserNameHelper(fields.Str):
    @classmethod
    def check_char_duplicate(self, value, char_dup='.'):
        list_dup = value.split(char_dup)
        return list_dup.count('') > 0

    def _validate(self, value):
        if not re.fullmatch(PATTERN_USER_NAME, value):
            raise ValidationError(MessageHelper.INVALID_USER_NAME_FORMAT)
        if self.check_char_duplicate(value, '.'):
            raise ValidationError(MessageHelper.INVALID_USER_NAME_FORMAT_DOT)
        return super()._validate(value)


class IsCodeHelper(fields.Str):
    def _validate(self, value):
        if not re.fullmatch(PATTERN_CODE,  value):
            raise ValidationError(MessageHelper.INVALID_CODE_FORMAT)
        return super()._validate(value)


class IsNameHelper(fields.Str):
    def _validate(self, value):
        if not re.fullmatch(PATTERN_NAME, str(value).lower()):
            raise ValidationError(MessageHelper.INVALID_NAME_FORMAT)
        return super()._validate(value)


class IsStatusHelper(fields.Int):
    def _validate(self, value):
        if not re.fullmatch(PATTERN_STATUS, str(value)):
            raise ValidationError(MessageHelper.STATUS_ACCEPT)
        return super()._validate(value)


class IsUnsignedIntHelper(fields.Int):
    def _validate(self, value):
        if not re.fullmatch(PATTERN_UNSIGNED_INTERGER, str(value)):
            raise ValidationError(MessageHelper.INVALID_FOREIGN_FORMAT)
        return super()._validate(value)
