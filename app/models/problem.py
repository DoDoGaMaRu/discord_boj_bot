from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True, autoincrement=True)
    boj_problem_id = Column(Integer, nullable=False)
    sequence = Column(Integer, nullable=False)
    workbook_daily_id = Column(ForeignKey('workbook_daily.id'), nullable=False, index=True)
    workbook_weekly_id = Column(ForeignKey('workbook_weekly.id'), nullable=False, index=True)

    workbook_daily = relationship('WorkbookDaily')
    workbook_weekly = relationship('WorkbookWeekly')
