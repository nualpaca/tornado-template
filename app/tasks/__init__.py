from ..settings import config
from celery import Celery

celery = Celery()
celery.config_from_object(config)

from ..tasks import *

