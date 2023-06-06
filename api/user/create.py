from flask_restx import Resource
from api.user.__namespace__ import api
from flask_jwt_extended import jwt_required


@api.doc(security='bearer')
class Create(Resource):
    @jwt_required()
    @api.doc()
    def post(self):
        """
        Create user
        """
        pass
        