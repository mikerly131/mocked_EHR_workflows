"""
A booking of a healthcare event among patient(s), practitioner(s), related person(s) and/or device(s) for a specific date/time.
This may result in one or more Encounter(s).
FHIR Version: R4
"""
from base_model import Base
from sqlalchemy import String, List, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AppointmentR4(Base):
    __tablename__ = 'appointment_r4'

    # Resource and Domain Resource FHIR data types. Resource type will always be "Appointment"
    resource_type: Mapped[str] = mapped_column(String, default="Appointment")
    id: Mapped[str] = mapped_column(String, primary_key=True)
    display_text_status: Mapped[str] = mapped_column(String, nullable=False)
    display_text_div: Mapped[str] = mapped_column(String, nullable=False)

    # Appointment Resource FHIR data types: primitives
    external_id: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    start: Mapped[str] = mapped_column(String)
    end: Mapped[str] = mapped_column(String)
    minutesDuration: Mapped[str] = mapped_column(String)
    created: Mapped[str] = mapped_column(String)
    comment: Mapped[str] = mapped_column(String)
    patientInstruction: Mapped[str] = mapped_column(String)

    # Appointment Resource FHIR data types: concepts and references
    cancelationReason: Mapped[str] = mapped_column(Text)
    serviceCategory: Mapped[str] = mapped_column(Text)
    serviceType: Mapped[str] = mapped_column(Text)
    speciality: Mapped[str] = mapped_column(Text)
    appointmentType: Mapped[str] = mapped_column(Text)
    reasonCode: Mapped[str] = mapped_column(Text)
    reasonReference: Mapped[str] = mapped_column(Text)
    supportingInformation: Mapped[str] = mapped_column(Text)
    slot: Mapped[str] = mapped_column(Text)
    basedOn: Mapped[str] = mapped_column(Text)
    requestedPeriod: Mapped[str] = mapped_column(Text)

    # Appointment Resource FHIR data types: child resource (backbone element)
    participants: Mapped[List["AppointmentParticipantR4"]] = relationship(
        back_populates="appointment_r4"
    )


class AppointmentParticipantR4(Base):
    __tablename__ = 'appointment_participant_r4'

    # Appointment Participant Resource FHIR data types: primitives
    required: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)

    # Appointment Resource FHIR data types: concepts and references
    type: Mapped[str] = mapped_column(Text)
    actor: Mapped[str] = mapped_column(Text)
    period: Mapped[str] = mapped_column(String)

    # Appointment Participant FHIR data types: parent resource (domain resource)
    appointment: Mapped["AppointmentR4"] = relationship(back_populates="appointment_participant_r4")



