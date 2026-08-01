import os

'''
Base configuration
'''
class Config:
    APP_NAME = 'Pyle'
    # APP_VERSION =
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False

    HOST = '0.0.0.0'
    PORT = 5000

'''
Configuration for development environment
'''
class DevConfig(Config):
    DEBUG = True
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