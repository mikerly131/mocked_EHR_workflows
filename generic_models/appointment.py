"""
A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time.
This may result in one or more Encounter(s).
FHIR Version: R4 or newer
"""
from generic_models.base_model import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, List, Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Appointment(Base):
    __tablename__ = 'appointment'

    resource_id
    resource_version
    resource_fhir


