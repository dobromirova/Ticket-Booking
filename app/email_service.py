class EmailService:

    def send_email(self, recipient, subject, message):
        print(f"Sending email to: {recipient}")
        print(f"Subject: {subject}")
        print(f"{message}")

    def send_booking_confirmation(self, recipient, booking):
        subject = "Booking confirmation"

        message = (

            f"Your booking #{booking.booking_id} has been confirmed. "
            f"\nEvent ID: {booking.event_id}"
            f"\nSeats: {booking.seat_ids}"
            f"\nTotal price: {booking.total_price:.2f}"


        )

        self.send_email(recipient, subject, message)

    def send_cancellation_email(self, recipient, booking):
        subject = "Booking Cancellation"

        message = (
            f"Your booking #{booking.booking_id} "
            f"has been cancelled."
        )

        self.send_email(recipient, subject, message)