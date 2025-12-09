from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata

class Record(Base):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    problem_id = Column(ForeignKey('problem.id'), nullable=False, index=True)
    member_id = Column(ForeignKey('member.id'), nullable=False, index=True)
    language = Column(ForeignKey('language.name'), nullable=False, index=True)
    min_byte = Column(Integer, nullable=False)
    min_time = Column(Integer, nullable=False)
    try_count = Column(Integer, nullable=False)

    language1 = relationship('Language')
    member = relationship('Member')
    problem = relationship('Problem')