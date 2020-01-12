from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "mysql+pymysql://example:password@mysql/example?charset=utf8"

engine = create_engine(
        SQLALCHEMY_DB_URL,
        connect_args={}
        )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
