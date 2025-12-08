from sqlalchemy import create_engine

from models import Base

engine = create_engine('sqlite:///example.db', echo=True)  # echo=True: SQL 로그 출력
Base.metadata.create_all(engine)