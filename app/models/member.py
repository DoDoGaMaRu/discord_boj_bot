from sqlalchemy import Integer, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guild_id = Column(ForeignKey('guild.id'), nullable=False, index=True)
    discord_id = Column(String(45), nullable=False)
    boj_id = Column(String(45), nullable=True)
    is_activated = Column(Boolean, nullable=False, default=False)

    guild = relationship('Guild')
