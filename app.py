
from flask import Flask
from settings.useEvironment import ENVIRONMENT
from api import blueprint as documented_endpoint
from flask_migrate import Migrate
from database import db, ma
from settings.useJWT import jwt_token, bcrypt
from settings.useApscheduler import scheduler
import json
import pytz
from datetime import datetime
from flask.logging import default_handler
from utils.timeHelpers import TimeHelper
from utils.responseHelper import check_message_token


app = Flask(__name__, static_folder='assets')

if ENVIRONMENT == 'prod':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')


app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
))

app.config.update(dict(
    # mặc định là 5 khi pool_size vược quá số này sẽ gây ra tình trạng tràn.
    SQLALCHEMY_MAX_OVERFLOW=100,
    # 0 không giới hạn số lượng kết nối, Số kết nối giữ bên trong connect pool
    SQLALCHEMY_POOL_SIZE=0,
    # -1 không có thời gian chờ, tính bằng s. , mysql sẽ kill connect sau 8h nếu không có hoạt động.
    SQLALCHEMY_POOL_RECYCLE=3600,
    # thời gian timeout nếu vượt quá SQLALCHEMY_MAX_OVERFLOW set SQLALCHEMY_MAX_OVERFLOW bằng 0 để test, tính bằng s.
    SQLALCHEMY_POOL_TIMEOUT=10,
    SQLALCHEMY_ECHO=False,  # True debug sql
))

app.config.update(dict(
    PROPAGATE_EXCEPTIONS=True,  # không cho hiển thị lỗi ra ngoài swagger
))


# Config Apscheduler
app.config.update(
    SCHEDULER_API_ENABLED=True,
    SCHEDULER_TIMEZONE='Asia/Ho_Chi_Minh'
)

# remove default handler để dùng logger
app.logger.removeHandler(default_handler)

# ket noi database va migrate
# db = SQLAlchemy(app)
db.init_app(app)
ma.init_app(app)
jwt_token.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db, compare_type=True)


# sched.start()
scheduler.init_app(app)
scheduler.start()

# test swagger
app.register_blueprint(documented_endpoint)

@app.route('/')
def index():
    return "<a href='v1/documentation'>API's documentation</a>"


@app.route('/timezone')
def time_zone():
    local = datetime.now()
    local_utc = datetime.utcnow()
    datetime_utc = datetime.now(pytz.utc)
    vi = pytz.timezone('Asia/Ho_Chi_Minh')
    datetime_vi = datetime.now(vi)
    data = {
        "local": local.strftime("%m/%d/%Y, %H:%M:%S"),
        "local_utc": local_utc.strftime("%m/%d/%Y, %H:%M:%S"),
        "timezone": TimeHelper.localTzname(),
        "raw": datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'),
        "vi": datetime_vi.strftime('%Y:%m:%d %H:%M:%S %Z %z')
    }
    return "<pre>"+json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))+"</pre>"


@app.after_request
def after_request(response):

    if int(response.status_code) == 401:
        response = check_message_token(response)
    return response
# Database creation flask commands


@app.cli.command('db-create')
def db_create():
    db.create_all()


@app.cli.command('db-seed')
def db_seed():
    # Thêm seed để chạy
    pass
@app.cli.command('db-truncate')
def clear_data():
    db.drop_all()
    db.create_all()
  

# MiddleWare
if __name__ == "__main__":
    app.run(port=5000,debug=app.config['DEBUG'], host="0.0.0.0")


