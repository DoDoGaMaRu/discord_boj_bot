from sqlalchemy import BigInteger, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class Member(Base):
    __tablename__ = 'member'

    id = Column(BigInteger, primary_key=True)
    server_id = Column(ForeignKey('server.id'), nullable=False, index=True)
    discord_id = Column(String(45), nullable=False)
    boj_id = Column(String(45), nullable=False)
    is_activated = Column(Boolean, nullable=False, default=True)

    server = relationship('Server')
