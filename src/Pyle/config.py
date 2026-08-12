import os

'''
Base configuration
'''
class Config:
    APP_NAME = 'Pyle'
    # APP_VERSION =

    DEBUG = False

    HOST = '0.0.0.0'
    PORT = 5000

    # Environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQL ALchemy variables
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pyle.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
Configuration for development environment
'''
class DevConfig(Config):
    DEBUG = True

    # HOST = 
    PORT = 8080

'''
Configuration for testing environment
'''
class TestConfig(Config):
    # HOST = 
    # PORT = 
    pass

'''
Configuration for production environments
'''
class ProdConfig(Config):
    # HOST = 
    # PORT = 
    pass