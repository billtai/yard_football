from datetime import datetime
import re
from utils.parserHelper import ParserHelper
from utils.timeHelpers import TimeHelper
from marshmallow.exceptions import ValidationError
from utils.schemeHelper import PATTERN_CODE, PATTERN_EMAIL, PATTERN_EMAIL_FIRST,\
    PATTERN_EMAIL_STRONG, PATTERN_NAME, PATTERN_PASSWORD_STRONG, PATTERN_PHONE,\
    PATTERN_STATUS, PATTERN_STR_INTERGER_NOT_SPECIAL, PATTERN_UNSIGNED_INTERGER, PATTERN_USER_NAME, PATTERN_MONEY_LIMIT
from utils.messageHelper import MessageHelper


class ValidateHelper:
    @classmethod
    def paging(self, payload, is_parser=False, init_limit=25):
        try:
            trang = 1
            so_luong = init_limit
            if 'trang' in payload:
                trang = payload['trang'][0] if is_parser else payload['trang']
                if not trang.isdigit():
                    raise ValueError(MessageHelper.PAGE)
            if 'so_luong' in payload:
                so_luong = payload['so_luong'][0] if is_parser else payload['so_luong']
                if not so_luong.isdigit():
                    raise ValueError(MessageHelper.ITEM_PER_PAGE)
            return {"success": True, "message": '', "data": {"trang": trang, "so_luong": so_luong}}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    @classmethod
    def status(self, value):
        try:
            if len(str(value).strip()) == 0:
                raise ValueError(MessageHelper.STATUS_EMTPY)
            if not re.fullmatch(PATTERN_STATUS, str(value)):
                raise ValueError(MessageHelper.STATUS_ACCEPT)
            return {"success": True, "message": ''}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    @classmethod
    def getValue(self, payload, field='', custom_field=None):
        value = ''
        try:
            value = payload[field]
        except KeyError as e:
            raise ValidationError(custom_field + MessageHelper.INVALID_KEY)
        return ParserHelper.getValue(value)

    @classmethod
    def paging_order(self, value):
        try:
            if not re.fullmatch(PATTERN_STATUS, str(value)):
                raise ValueError(MessageHelper.ORDER_A_Z_STATUS)
            return {"success": True, "message": ''}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    @classmethod
    def str_length(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        len_value = len(str(value).strip())
        fld = custom_field if custom_field is not None else field
        if len_value == 0:
            raise ValidationError(custom_field + MessageHelper.LENGTH_EMTPY)

        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}

        if not len_value >= min:
            raise ValidationError(
                MessageHelper.message_join(fld, 'LENGTH_MIN', min))

        if not len_value <= max:
            raise ValidationError(
                MessageHelper.message_join(fld, 'LENGTH_MAX', max))
        return {"success": True, "message": ''}
    
    @classmethod
    def choose_str_empty(self, payload, field='', custom_field=None,  is_empty=False):
        value = self.getValue(payload, field, custom_field)
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}

    @classmethod
    def min_max(self, value, custom_field=None, min=0, max=255):
        len_value = len(str(value).strip())
        if min > 0:
            if not len_value >= min:
                raise ValidationError(
                    MessageHelper.message_join(custom_field, 'LENGTH_MIN', min))

        if not len_value <= max:
            raise ValidationError(
                MessageHelper.message_join(custom_field, 'LENGTH_MAX', max))
        return {"success": True, "message": ''}

    @classmethod
    def str_length_min_max(self, value, custom_field=None, min=0, max=255, is_empty=False):
        len_value = len(str(value).strip())
        if is_empty:
            self.min_max(value, custom_field=custom_field, min=min, max=max)
            return {"success": True, "message": ''}
        if len_value == 0:
            raise ValidationError(custom_field + MessageHelper.LENGTH_EMTPY)
        self.min_max(value, custom_field=custom_field, min=min, max=max)
        return {"success": True, "message": ''}

    @classmethod
    def str_status(self, payload, field='', custom_field=None):
        value = self.getValue(payload, field, custom_field)

        len_value = len(str(value).strip())
        fld = custom_field if custom_field is not None else field
        if len_value == 0:
            raise ValidationError(custom_field + MessageHelper.LENGTH_EMTPY)

        if len(str(value).strip()) == 0:
            raise ValidationError(fld + MessageHelper.BOOLEAN_EMTPY)
        if not re.fullmatch(PATTERN_STATUS, str(value)):
            raise ValidationError(fld + MessageHelper.BOOLEAN_ACCEPT)

        return {"success": True, "message": ''}
    #vn-code validate
    @classmethod
    def validate_field(self, payload, field='', custom_field=None, is_empty=False):

        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        #check_value = len(str(value).strip())
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}
        #if not check_value:
        #    raise ValidationError(custom_field + MessageHelper.LENGTH_EMTPY)
        if not re.fullmatch(PATTERN_STR_INTERGER_NOT_SPECIAL, str(value)):
            raise ValidationError(fld + MessageHelper.CHECK_VN_CODE)

    @classmethod
    def str_empty(self, payload, field='', custom_field=None):
        value = self.getValue(payload, field, custom_field)
        len_value = len(str(value).strip())
        fld = custom_field if custom_field is not None else field
        if len_value == 0 or len  == "":
            raise ValidationError(custom_field + MessageHelper.LENGTH_EMTPY)
        return {"success": True, "message": ''}
    @classmethod
    def str_unsigned_int(self, payload, field='', custom_field=None, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        len_value = len(str(value).strip())
        fld = custom_field if custom_field is not None else field
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}
        if len_value == 0 or len  == "":
            raise ValidationError(custom_field + MessageHelper.LENGTH_EMTPY)

        if not re.fullmatch(PATTERN_UNSIGNED_INTERGER, str(value)):
            raise ValidationError(
                fld + MessageHelper.INVALID_FOREIGN_FORMAT_VALIDATE)

        return {"success": True, "message": ''}

    @classmethod
    def name(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        self.str_length_min_max(value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}
        if not re.fullmatch(PATTERN_NAME, str(value).lower()):
            raise ValidationError(MessageHelper.message_invalid_format(fld))
        return {"success": True, "message": ''}

    @classmethod
    def password(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        self.str_length_min_max(
            value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        if not re.fullmatch(PATTERN_PASSWORD_STRONG, value):
            raise ValidationError(MessageHelper.message_custom(
                fld, 'tối thiểu sáu ký tự, ít nhất một chữ hoa, một chữ thường, một số và một ký tự đặc biệt'))

        return {"success": True, "message": ''}

    @classmethod
    def check_char_duplicate(self, value, char_dup='.'):
        list_dup = value.split(char_dup)
        return list_dup.count('') > 0

    @classmethod
    def username(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        self.str_length_min_max(
            value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        if not re.fullmatch(PATTERN_USER_NAME, value):
            raise ValidationError(
                MessageHelper.message_invalid_format(fld))
        if self.check_char_duplicate(value, '.'):
            raise ValidationError(MessageHelper.message_custom(
                fld, 'không chứa dấu chấm kề nhau hoặc ở đầu và cuối'))

        return {"success": True, "message": ''}

    @classmethod
    def code(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        self.str_length_min_max(
            value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        if not re.fullmatch(PATTERN_CODE, value):
            raise ValidationError(
                MessageHelper.message_invalid_format(fld))
        if self.check_char_duplicate(value, '.'):
            raise ValidationError(MessageHelper.message_custom(
                fld, 'không chứa dấu chấm kề nhau hoặc ở đầu và cuối'))

        return {"success": True, "message": ''}

    @classmethod
    def phone(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}
        self.str_length_min_max(
            value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        # if value.startswith("84"):
        #     if not re.fullmatch(PATTERN_PHONE_INTERNATIONAL_AREA_CODE, value):
        #         raise ValidationError(MessageHelper.message_custom(
        #             fld, 'không đúng định dạng đầu số việt nam'))
        #     return {"success": True, "message": ''}
        # if not re.fullmatch(PATTERN_PHONE_NO_CHECK_REFIX, value):
        #     raise ValidationError(MessageHelper.message_invalid_format(fld))
        if not re.fullmatch(PATTERN_PHONE, value):
            raise ValidationError(MessageHelper.message_invalid_format(fld))

        return {"success": True, "message": ''}

    @classmethod
    def email(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        #check_value = len(str(value).strip())
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}
        fld = custom_field if custom_field is not None else field
        self.str_length_min_max(
            value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        if not re.fullmatch(PATTERN_EMAIL_FIRST, value):
            raise ValidationError(MessageHelper.message_invalid_format(fld))

        if not re.fullmatch(PATTERN_EMAIL, value):
            raise ValidationError(MessageHelper.message_invalid_format(fld))

        if not re.fullmatch(PATTERN_EMAIL_STRONG, value):
            raise ValidationError(MessageHelper.message_invalid_format(fld))
        return {"success": True, "message": ''}
    
    @classmethod
    def address(self, payload, field='', custom_field=None, min=0, max=255, is_empty=False):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        self.str_length_min_max(
            value=value, custom_field=fld, min=min, max=max, is_empty=is_empty)
        return {"success": True, "message": ''}

    @classmethod
    def date_start(self, payload, field='', custom_field=None, format=TimeHelper.FORMAT_TIME_D_M_Y__h_m_s):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        date_time_ngay_di = None
        try:
            date_time_ngay_di = datetime.strptime(
                value, format)
        except Exception as e:
            raise ValidationError(MessageHelper.message_invalid_format(fld))
        if date_time_ngay_di < TimeHelper.get_date_now():
            raise ValidationError(MessageHelper.message_custom(
                fld, 'phải lớn hơn thời gian hiện tại'))
        return {"success": True, "message": ''}

    @classmethod
    def birthday(self, payload, field='', custom_field=None):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        ngay_sinh = None
        # value = 
        if value == "":
            raise ValidationError(MessageHelper.message_custom(fld, 'Không được trống'))
        try:
            ngay_sinh = datetime.strptime(value, TimeHelper.FORMAT_TIME_D_M_Y)
        except Exception as e:
            raise ValidationError(MessageHelper.message_invalid_format(fld))
        if ngay_sinh > TimeHelper.get_date_now():
            raise ValidationError(MessageHelper.message_custom(
                fld, 'phải nhỏ hơn thời gian hiện tại'))
        return {"success": True, "message": '', 'ngay_sinh': ngay_sinh}

    @classmethod
    def birthdayYMD(self, payload, field='', custom_field=None):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        ngay_sinh = None
        # value =
        if value == "":
            raise ValidationError(
                MessageHelper.message_custom(fld, 'Không được trống'))
        try:
            ngay_sinh = datetime.strptime(value, TimeHelper.FORMAT_TIME_Y_M_D)
        except Exception as e:
            raise ValidationError(MessageHelper.message_invalid_format(fld))
        if ngay_sinh > TimeHelper.get_date_now():
            raise ValidationError(MessageHelper.message_custom(
                fld, 'phải nhỏ hơn thời gian hiện tại'))
        return {"success": True, "message": '', 'ngay_sinh': ngay_sinh}

    @classmethod
    def birthdayHHMMYY(self, payload, field='', custom_field=None, message_field=None):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        ngay_sinh = None
        try:
            ngay_sinh = datetime.strptime(
                value, TimeHelper.FORMAT_TIME_D_M_Y)
        except Exception as e:
            raise ValidationError(MessageHelper.message_invalid_format(
                message_field if message_field is not None else fld))
        if ngay_sinh > TimeHelper.get_date_now():
            raise ValidationError(MessageHelper.message_custom(
                fld, 'phải nhỏ hơn thời gian hiện tại'))
        return {"success": True, "message": '', 'ngay_sinh': ngay_sinh}

    @classmethod
    def min_max_number(self, payload, field, custom_field=None, min=0, max=255):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        try:
            value = int(value)
        except (ValidationError, ValueError) as e:
            raise ValidationError(MessageHelper.message_invalid_format(fld))
        if min > 0:
            if not value >= min:
                raise ValidationError(
                    MessageHelper.message_join(custom_field, 'LENGTH_MIN', min, after=''))

        if not value <= max:
            raise ValidationError(
                MessageHelper.message_join(custom_field, 'LENGTH_MAX', max, after=''))
        return {"success": True, "message": ''}

    @classmethod
    def date_end(self, payload, date_start, field='', custom_field=None, custom_field_start=None, format=TimeHelper.FORMAT_TIME_D_M_Y__h_m_s):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        date_time_ngay_ve = None
        date_time_ngay_di = None
        try:
            date_time_ngay_ve = datetime.strptime(value, format)
        except Exception as e:
            raise ValidationError(MessageHelper.message_invalid_format(fld))

        try:
            date_time_ngay_di = datetime.strptime(date_start, format)
        except Exception as e:
            raise ValidationError(
                MessageHelper.message_invalid_format(custom_field_start))

        if date_time_ngay_ve < date_time_ngay_di:
            raise ValidationError(MessageHelper.message_custom(
                fld, 'phải lớn hơn ' + custom_field_start.lower()))
        return {"success": True, "message": ''}

    @classmethod
    def money(self, payload, field='', custom_field=None):
        value = self.getValue(payload, field, custom_field)
        fld = custom_field if custom_field is not None else field
        try:
            if not re.fullmatch(PATTERN_MONEY_LIMIT, value):
                raise ValidationError(
                    MessageHelper.message_invalid_format(fld))

        except Exception as e:
            raise ValidationError(MessageHelper.message_invalid_format(fld))

        return {"success": True, "message": ''}
    
    @classmethod
    def kiem_tra_ten(self, payload, field = "", custom_field = "", is_empty=False):
        value = self.getValue(payload, field, custom_field)
        if len(str(value)) == 0 and is_empty:
            return {"success": True, "message": ''}
