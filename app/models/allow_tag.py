from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata

class AllowTag(Base):
    __tablename__ = 'allow_tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String, primary_key=True)
    problem_template_daily_id = Column(ForeignKey('problem_template_daily.id'), nullable=True, index=True)
    problem_template_weekly_id = Column(ForeignKey('problem_template_weekly.id'), nullable=True, index=True)

    tag = relationship('Tag')
    problem_template_daily = relationship('ProblemTemplateDaily')
    problem_template_weekly = relationship('ProblemTemplateWeekly')
