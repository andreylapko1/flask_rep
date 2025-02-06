class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///datab.db'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    Testing = True

