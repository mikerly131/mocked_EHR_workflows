"""
Initialization and functions for using Appointments
FHIR Version: R4
"""
from r4_models.appointment import AppointmentR4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def create_appointment(db: AsyncSession, appointment_data: dict) -> AppointmentR4:
    new_appointment = AppointmentR4(**appointment_data)
    db.add(new_appointment)
    await db.commit()
    await db.refresh(new_appointment)
    return new_appointment


async def get_appointment(db: AsyncSession, appointment_id: str) -> AppointmentR4:
    async with db.execute(select(AppointmentR4).filter(AppointmentR4.id == appointment_id)) as result:
        appointment = result.scalars().first()
    return appointment

