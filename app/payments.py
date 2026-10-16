class Payment:
    def __init__(self, payment_id, booking_id, amount, payment_method, date, status):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.payment_method = payment_method
        self.date = date
        self.status = status
