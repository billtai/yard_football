from flask_cors import CORS
import werkzeug
import flask.scaffold
from flask_restx import Api
from flask import Blueprint

werkzeug.cached_property = werkzeug.utils.cached_property
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func


blueprint = Blueprint('api', __name__)
authorizations = {
    'bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api_extension = Api(
    blueprint,
    title='YARD FOOTBALL MANAGER',
    version='1.0',
    description='YARD FOOTBALL MANAGER',
    doc = '/v1/documentation',
    prefix = '/v1',
    ordered=True,
    authorizations = authorizations
)

CORS(blueprint, origins=['http://localhost:3000'])

#########################################################################
# Hãng bay bamboo
#########################################################################
# import namespace của module

from api.user import api as user_ns


# thêm namespace vào api


api_extension.add_namespace(user_ns)