from database.schemas import PGBaseSchema
from database.models.users import UsersModel

user = ("id", "username", "name", "email", "phone", "address", "avatar")


class UserSchema(PGBaseSchema):

    class Meta:
        model   = UsersModel
        fields  = user
