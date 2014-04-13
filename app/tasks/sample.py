from . import celery

@celery.task(name='addition')
def addition(x,y):
    return x + y

