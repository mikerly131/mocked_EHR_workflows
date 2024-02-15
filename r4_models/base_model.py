"""
This file creates the base sqlalchemy r4_models for the ORM
"""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


# Not going to use this initially, seems too complicated
# class ResourceBase(Base):
#     __abstract__ = True
#
#     resource_type = Column(String)
#     id = Column(Integer, primary_key=True)
#     text_status = Column(String)
#     text_div = Column(String)
