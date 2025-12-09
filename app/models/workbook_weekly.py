from sqlalchemy import Column, Date, ForeignKey, String, Boolean, Integer
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class WorkbookWeekly(Base):
    __tablename__ = 'workbook_weekly'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guild_id = Column(ForeignKey('guild.id'), nullable=False, index=True)
    boj_workbook_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    created = Column(Boolean, nullable=False)

    guild = relationship('Guild')

