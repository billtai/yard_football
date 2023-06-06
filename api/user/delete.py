from api.user.__namespace__ import api
from flask_jwt_extended import jwt_required
from flask_restx import Resource

#########################################################################
# ENDPOINTS
#########################################################################


@api.doc(security='bearer')
class Delete(Resource):

    @jwt_required()
    @api.doc()
    def delete(self, id):
        """
        Delete user
        """
        
