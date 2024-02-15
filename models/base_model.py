"""
This file creates the base sqlalchemy models for the ORM
"""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class ResourceBase(Base):
    id = Column(Integer, primary_key=True)
    text_status = Column(String)
    text_div = Column(String)
