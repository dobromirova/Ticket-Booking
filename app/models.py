from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    String,
    ForeignKey,
    Table,
    Column,
    DateTime,
    UniqueConstraint,
    Numeric,
)


from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base

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

    events: Mapped[list["Event"]] = relationship(
        back_populates="venue"

    )
    seats: Mapped[list["Seat"]] = relationship(
        back_populates="venue"
    )


class Seat(Base):
    __tablename__ = "seats"
    __table_args__ = (
        UniqueConstraint("venue_id", "seat_num"),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    seat_num: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    venue_id: Mapped[int] = mapped_column(
        ForeignKey("venues.id"),
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

    venue: Mapped["Venue"] = relationship(
        back_populates="events")

    bookings: Mapped[list["Booking"]] = relationship(
        back_populates="event"
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

    booking_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now
    )

    total_price: Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(39),
        nullable=False,
        default="pending"
    )

    event: Mapped["Event"] = relationship(
        back_populates="bookings"
    )

    seats: Mapped[list["Seat"]] = relationship(
        secondary=booking_seats,
        back_populates="bookings",
    )

    payments: Mapped[list["Payment"]] = relationship(
        back_populates="booking"
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

    amount:Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending"
    )

    booking: Mapped["Booking"] = relationship(
        back_populates="payments"
    )





