from api.user.__namespace__ import api
from api.user.list import List
from api.user.create import Create
from api.user.delete import Delete
from api.user.update import Update
from api.user.auth import Authentication


#########################################################################
# CUSTOM ROUTES
#########################################################################
api.add_resource(List, '/list', methods=['GET'])
api.add_resource(Create, '/create', methods=['POST'])
api.add_resource(Delete, '/delete/<int:id>', methods=['DELETE'])
api.add_resource(Update, '/update/<int:id>', methods=['PUT'])
api.add_resource(Authentication, '/login', methods=['POST'])
api.add_resource(Authentication, '/logout', methods=['DELETE'])
