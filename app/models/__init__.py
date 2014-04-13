from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..settings import config

Base = declarative_base()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, 
					   echo=config.SQLALCHEMY_ECHO)

db = scoped_session(sessionmaker(bind=engine))