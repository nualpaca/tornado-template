from tornado.options import define, options
import os

class Config(object):
    """Configuration object for celery""" 
    # BROKER_URL = os.getenv('RABBITMQ_URL', 'amqp://')

    BROKER_URL = os.getenv('BROKER_URL','amqp://')
    CELERY_RESULT_BACKEND = 'amqp'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'US/Central'
    CELERY_ENABLE_UTC = True
    CELERY_REDIRECT_STDOUTS = True
    CELERY_REDIRECT_STDOUTS_LEVEL = 'DEBUG'
    CELERY_TRACK_STARTED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@localhost:5432/app_development')

    PORT = 5000

class Development(Config):
    DEBUG=True

class Production(Config):
    DEBUG=False

environment = os.environ.get('TORNADO_ENV', 'development')
config = eval(environment.title())