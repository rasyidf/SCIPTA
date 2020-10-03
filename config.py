# -*- encoding: utf-8 -*-


import os
from decouple import config

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))
 
    SECRET_KEY = config('SECRET_KEY', default='8BA3F37F-85AD-42A2-AE3A-27C22D137E1D')
    SERVER_NAME = '127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY  = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
 
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config( 'DB_ENGINE'   , default='mongodb'   ),
        config( 'DB_USERNAME' , default='sipta'     ),
        config( 'DB_PASS'     , default='pass'      ),
        config( 'DB_HOST'     , default='localhost' ),
        config( 'DB_PORT'     , default=27017       ),
        config( 'DB_NAME'     , default='sipta-db'  )
    )

class DebugConfig(Config):
    DEBUG = True
    ENV = "development"

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
