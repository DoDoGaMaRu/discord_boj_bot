from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata

class BestRecord(Base):
    __tablename__ = 'best_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    problem_id = Column(ForeignKey('problem.id'), nullable=False, index=True)
    member_id = Column(ForeignKey('member.id'), nullable=False, index=True)
    language = Column(ForeignKey('language.name'), nullable=False, index=True)
    result_byte = Column(Integer, nullable=False)
    result_time = Column(Integer, nullable=False)

    language1 = relationship('Language')
    member = relationship('Member')
    problem = relationship('Problem')