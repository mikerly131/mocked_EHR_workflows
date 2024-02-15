"""
A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time.
This may result in one or more Encounter(s).
FHIR Version: R4 or newer
"""
from r4_models.base_model import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import String, List, Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Appointment(Base):
    pass
