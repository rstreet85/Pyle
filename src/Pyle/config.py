import os

class Config:
    APP_NAME = 'Pyle'
    # APP_VERSION
    SECRET_KEY = os.environ.get('SECRET_KEY')

'''
Configuration for development environment
'''
class DevConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000

'''
Configuration for testing environment
'''
class TestConfig(Config):
    DEBUG = False
    # HOST = 
    # PORT = 

'''
Configuration for production environments
'''
class ProdConfig(Config):
    DEBUG = False
    # HOST = 
    # PORT = 