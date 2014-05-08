from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()
session = sessionmaker(engine)()
