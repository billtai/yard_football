from flask_restx import Resource
from api.user.__namespace__ import api
from flask_jwt_extended import jwt_required

#########################################################################
# ENDPOINTS
#########################################################################


@api.doc(security='bearer')
class List(Resource):

    @jwt_required()
    @api.doc()
    def get(self):
        """
        List user
        """
        pass