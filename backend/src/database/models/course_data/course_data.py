from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey
from sqlalchemy.sql import func

from ...base import Base
from .module import Module


__all__ = ("CourseData",)

class CourseData(Base):
    __tablename__ = 'courses_data'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    modules = Column(list[ForeignKey(Module.id)], default=[])
