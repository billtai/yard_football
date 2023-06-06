from utils.hashCodeHelper import hash_code
from utils.messageHelper import TranslateMessageHelper
from flask.json import dumps, loads
import logging as logging
import traceback
from utils.telegram import send
from flask import request

def get_first_order_dict(message):
    try:
        for _, value in message.items():
            return value[0]
    except KeyError as e:
        return ''


class ResponseHelper:
    @classmethod
    def on_error(self, message, status='error', code=400, data=None):
        """
            Nếu muốn raise hoặc dừng request thì nên dùng hàm này để format response error
        """
       

        if type(message) is list:
            message = message[0] if len(message) == 1 else ''

        if type(message) is dict:
            message = get_first_order_dict(message)

        res = ({"message": message,"data": data, "status": status, "code": code}, 200)
        logging.error(res)
        message = traceback.format_exc()
        logging.error(message)
        # send(f"🆘 <b>{request.url}</b>\nLỗi {code}\n{message}")
        return res


    @classmethod
    def on_success(self, message='', data=None, status='success', code=200):
        res =  ({"message": message, "data": data, "status": status, "code": code}, 200)  
        logging.info(res)
        return res


def createResPaging(data, paging):
    return {
        "content": data,
        "has_next": paging.has_next,
        "has_prev": paging.has_prev,
        "page": paging.page,
        "total_pages": paging.pages,
        "total_records": paging.total
    }



def create_custom_error_lib(response_data, response, delete_props, status):
    del response_data[delete_props]
    response_data['code'] = status
    response_data['data'] = None
    response.set_data(dumps(response_data))
    response.headers.add('Content-Type', 'application/json')
    return response


def check_message_token(response):
    response_data = dict()
    try:
        response_data = loads(response.get_data())
    except:
        return response
    if 'msg' in response_data:
        res = ''
        if 'Missing Authorization Header':
            res = 'Hết phiên đăng nhập'
            response_data['message'] = res
            response = create_custom_error_lib(response_data, response, 'msg', 401)
    return response


def check_message_validate_field(response):
    response_data = dict()
    try:
        response_data = loads(response.get_data())
    except:
        return response
    if 'errors' in response_data:
        res = ""
        for k, v in response_data['errors'].items():
            res = TranslateMessageHelper.message_to_vi(k, v)
            break
        response_data['message'] = res
        response = create_custom_error_lib(response_data, response, 'errors', 400)
    return response
