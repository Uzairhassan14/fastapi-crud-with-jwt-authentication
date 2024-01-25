from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = ""


engine = create_engine(SQLALCHEMY_DATABASE_URL)


# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlush=False)
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
)  # this line of code is working but above line not worked

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
