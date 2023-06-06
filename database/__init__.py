from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# khoi tao SQLAlchemy
db = SQLAlchemy()

from database.models import BaseModel
base = db.make_declarative_base(model=BaseModel)

# Initialize Marshmallow
ma = Marshmallow()


#connect redis
from flask_redis import FlaskRedis
redis_client = FlaskRedis()

# mongoDB
from flask_mongoengine import MongoEngine
mongodb = MongoEngine()