from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# khoi tao SQLAlchemy
db = SQLAlchemy()

from database.models import BaseModel
base = db._make_declarative_base(model=BaseModel)

# Initialize Marshmallow
ma = Marshmallow()


