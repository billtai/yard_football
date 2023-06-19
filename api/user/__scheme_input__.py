from flask_restx import fields
from api.user.__namespace__ import api

#########################################################################
# MODELS for expect
#########################################################################


user_input = api.model('Users', {
    'name'      : fields.String(example="Super amdin"),
    'username'  : fields.String(example="admin"),
    'password'  : fields.String(example="Abc@12345"),
    'email'     : fields.String(example="abca@gmail.com"),
    'phone'     : fields.String(example="0385444312"),
    'address'   : fields.String(example="359 Phạm Văn Chiêu"),
    'status'    : fields.Integer(example=1),
    'avatar'    : fields.String(example="avatar.png"),
    'role_id'   : fields.Integer(example=1),
})
login_input = api.model('Login', {
    'username': fields.String(example='nv1'),
    'password': fields.String(example='@Abc123')
})
