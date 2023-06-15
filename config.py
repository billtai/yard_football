from datetime import timedelta


class Config(object):
    DEBUG = False
    JSON_SORT_KEYS = False
    # ConnectString Database Main
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@localhost/{}'.format(
        'root', '', 'yard_football')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ConnectString Database Extra
    SQLALCHEMY_BINDS = {
        # KEY : CONNECT_STRING
    }
    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'  # 'none', 'list' or 'full'
    # Enable Validate RestPlus
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    #Seeder
    FLASK_SEEDER_AUTOCOMMIT = 0

    # JWT settings
    JWT_SECRET_KEY = "super-secret-key-haha"

    # Token
    TOKEN_EXPIRED = 3
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    #KEY
    KEY_HASHCODE = "OYhVrnbaJIcKb39VKeag2ER69Ki6-vsou1nxQzlqd-4="
    PROPAGATE_EXCEPTIONS = False

    BASE_URL = "http://localhost:5000"

   



    # Vietravel

    SERVER_IP = '103.104.121.12'
    LOCATION = "Việt Nam"

  
    # Telegram
    TELEGRAM_APP = 'Error bot'
    TELEGRAM_TO = '-999229138'
    # Errors - Announcer (DIDOTEK)
    TELEGRAM_BOT = '6091432285:AAE3kaBEzGDCK3gkEqLK5aLm5_14B3w1UJo'

    TRAP_HTTP_EXCEPTIONS = True


class ProductionConfig(Config):
    LOG_FILE = 'errorlog.txt'
    pass


class DevelopmentConfig(Config):
    LOG_FILE = 'errorlog.txt'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
