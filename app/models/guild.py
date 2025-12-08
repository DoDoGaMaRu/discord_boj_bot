from sqlalchemy import Integer, Column, String, Boolean
from .base import Base

metadata = Base.metadata

class Guild(Base):
    __tablename__ = 'guild'

    id = Column(Integer, primary_key=True, autoincrement=True)
    guild_id = Column(String(45), nullable=False)
    boj_group_id = Column(Integer, nullable=True)
    workbook_daily_enable = Column(Boolean, nullable=False, default=False)
    workbook_weekly_enable = Column(Boolean, nullable=False, default=False)
