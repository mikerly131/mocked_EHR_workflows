"""
A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time.
This may result in one or more Encounter(s).
FHIR Version: R4
"""
from base_model import Base, ResourceBase
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import String, List, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Appointment(ResourceBase):
    __tablename__ = 'appointment'

    identifier: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String)
    cancelationReason: Mapped[str] = mapped_column(String)
    serviceCategory: Mapped[str] = mapped_column(String)
    serviceType: Mapped[str] = mapped_column(String)
    speciality: Mapped[str] = mapped_column(String)
    appointmentType: Mapped[str] = mapped_column(String)
    reasonCode: Mapped[str] = mapped_column(String)
    reasonReference: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    supportingInformation: Mapped[str] = mapped_column(String)
    start: Mapped[str] = mapped_column(String)
    end: Mapped[str] = mapped_column(String)
    minutesDuration: Mapped[str] = mapped_column(String)
    slot: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    comment: Mapped[str] = mapped_column(String)
    patientInstruction: Mapped[str] = mapped_column(String)
    basedOn: Mapped[str] = mapped_column(String)
    requestedPeriod: Mapped[str] = mapped_column(String)

    participants: Mapped[List["AppointmentParticipant"]] = relationship(
        back_populates="appointment"
    )


class AppointmentParticipant(Base):
    __tablename__ = 'appointment_participant'

    type: Mapped[str] = mapped_column(String)
    actor: Mapped[str] = mapped_column(String)
    required: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    period: Mapped[str] = mapped_column(String)

    appointment: Mapped["Appointment"] = relationship(back_populates="appointment_participant")



