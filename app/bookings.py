class Booking:
    def __init__(self, booking_id, event_id, seat_ids,
                 booking_date, total_price, status):
        self.booking_id = booking_id
        self.event_id = event_id
        self.seat_ids = seat_ids
        self.booking_date = booking_date
        self.total_price = total_price
        self.status = status
        ## SEAT IDS PLURAL BECAUSE IT IS A LIST
        ## EX: seat_ids = [12, 13, 14]