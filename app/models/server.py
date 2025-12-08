from sqlalchemy import BigInteger, Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class Server(Base):
    __tablename__ = 'server'

    id = Column(BigInteger, primary_key=True)
    discord_server_id = Column(String(45), nullable=False)
    boj_group_id = Column(BigInteger, nullable=False)
    workbook_daily_enable = Column(Boolean, nullable=False)
    workbook_weekly_enable = Column(Boolean, nullable=False)
    problem_format_daily_id = Column(ForeignKey('problem_format_daily.id'), nullable=False, index=True)
    problem_format_weekly_id = Column(ForeignKey('problem_format_weekly.id'), nullable=False, index=True)

    problem_format_daily = relationship('ProblemFormatDaily')
    problem_format_weekly = relationship('ProblemFormatWeekly')
