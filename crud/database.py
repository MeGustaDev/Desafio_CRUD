from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://endwhzad:0rpfe-8geh5LTox2GcUjM7yPimiEJmKl@babar.db.elephantsql.com/endwhzad"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
# argumento pode ser desnessário utilizando o postgre


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
