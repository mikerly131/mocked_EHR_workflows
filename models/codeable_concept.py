"""
A CodeableConcept represents a value that is usually supplied by providing a reference to one or more terminologies or ontologies
but may also be defined by the provision of text. This is a common pattern in healthcare data.
"""
from base_model import ModelBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CancelationReason(ModelBase):
    __tablename__ = 'cancelation_reason'

class ServiceCategory(ModelBase):
    __tablename__ = 'service_category'

    system:
    version:
    code:
    display: Mapped[str] = mapped_column(String)
    userSelected: Mapped[bool] = mapped_column(default=False)
