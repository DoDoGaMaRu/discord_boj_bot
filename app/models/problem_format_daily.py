from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class ProblemFormatDaily(Base):
    __tablename__ = 'problem_format_daily'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guild_id = Column(ForeignKey('guild.id'), nullable=False, index=True)
    min_tier = Column(String(45), nullable=False)
    max_tier = Column(String(45), nullable=False)
    no_dup = Column(Boolean, nullable=False)
    sequence = Column(Integer, nullable=False)

    guild = relationship('Guild')