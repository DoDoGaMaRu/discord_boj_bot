from sqlalchemy import Column, String
from .base import Base

metadata = Base.metadata

class Tag(Base):
    __tablename__ = 'tag'

    tag_code = Column(String, primary_key=True)
    tag_name = Column(String, nullable=False)