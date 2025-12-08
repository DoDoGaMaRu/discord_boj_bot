from sqlalchemy import BigInteger, Column, Date, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

metadata = Base.metadata


class WorkbookWeekly(Base):
    __tablename__ = 'workbook_weekly'

    id = Column(BigInteger, primary_key=True)
    server_id = Column(ForeignKey('server.id'), nullable=False, index=True)
    boj_workbook_id = Column(BigInteger, nullable=False)
    name = Column(String(45), nullable=False)
    date = Column(Date, nullable=False)
    created = Column(Boolean, nullable=False)

    server = relationship('Server')

