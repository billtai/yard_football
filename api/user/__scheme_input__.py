from flask_restx import fields
from api.user.__namespace__ import api

#########################################################################
# MODELS for expect
#########################################################################


input_them = api.model('Add user', {
    'name'           : fields.String(example="Super amdin"),
    'username'          : fields.String(example="admin"),
})
