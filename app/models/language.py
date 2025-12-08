from sqlalchemy import Column, String
from .base import Base

metadata = Base.metadata


class Language(Base):
    __tablename__ = 'language'

    name = Column(String(45), primary_key=True)
