from sqlalchemy import BigInteger, Column, Integer, String, Boolean
from .base import Base

metadata = Base.metadata


class ProblemFormatDaily(Base):
    __tablename__ = 'problem_format_daily'

    id = Column(BigInteger, primary_key=True)
    min_tier = Column(String(45), nullable=False)
    max_tier = Column(String(45), nullable=False)
    no_dup = Column(Boolean, nullable=False)
    sequence = Column(Integer, nullable=False)