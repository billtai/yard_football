from flask_restx import Resource
from api.user.__namespace__ import api
from flask_jwt_extended import jwt_required
from api.user.__scheme_input__ import input_them
from database.models.users import UsersModel
from utils.formatHelper import FormatHelper


@api.doc(security='bearer')
class Create(Resource):
    # @jwt_required()
    @api.doc(body=input_them)
    def post(self):
        """
        Create user
        """
        add_user = FormatHelper.trim_payload(api.payload).copy()
        user = UsersModel(add_user)
        user.create_to_db()
        return add_user
