# import os

class Config:
    APP_NAME = 'Pyle'
    # APP_VERSION

'''
Configuration for development environment
'''
class DevConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8080

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