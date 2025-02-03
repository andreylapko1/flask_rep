class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    Testing = True