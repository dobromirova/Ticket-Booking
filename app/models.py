from ast import List
from datetime import datetime


from sqlalchemy import (
    String,
    ForeignKey,
    Table,
    Column,
    DateTime,
    Float, UniqueConstraint,
)


from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base

booking_seats = Table(
    "booking_seats",
    Base.metadata,
    Column(
        "booking_id",
        ForeignKey("bookings.id"),
        primary_key=True,
    ),
    Column(
        "seat_id",
        ForeignKey("seats.id"),
        primary_key=True,
    ),
)


class Venue(Base):
    __tablename__ = "venues"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable = False
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable = False
    )

    capacity: Mapped[int] = mapped_column(
        nullable=False
    )

    events: Mapped[list["Event"]] = relationship(back_populates="venue")
    seats: Mapped[list["Seat"]] = relationship(back_populates="venue")


class Seat(Base):
    __tablename__ = "seats"
    __table_args__ = (
        UniqueConstraint("venue_id", "seat_number"),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    venue_id: Mapped[int] = mapped_column(
        ForeignKey("venues.id"),
        nullable=False
    )

    seat_numer: Mapped[int] = mapped_column(
        nullable=False
    )

    venue: Mapped["Venue"] = relationship(
        back_populates="seats"
    )

    bookings: Mapped[list["Booking"]] = relationship(
        secondary=booking_seats,
        back_populates="seats",
    )

    ## TODO: explanations on secondary, back populates and relations.


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    venue_id: Mapped[int] = mapped_column(
        ForeignKey("venues.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(

        String(100),
        nullable = False
    )

    date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )



class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id"),
        nullable=False
    )

    seats: Mapped[list["Seat"]] = relationship(
        secondary=booking_seats
    )

    booking_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    total_price: Mapped[float] = mapped_column(
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        nullable=False
    )

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    booking_id: Mapped[int] = mapped_column(
        ForeignKey("bookings.id"),
        nullable=False
    )

    amount:Mapped[float] = mapped_column(
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        nullable=False
    )

    date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        nullable=False
    )





