from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats, ticket_price):
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def get_ticket(self, tickets_count):
        fn_value = self.get_capacity(self.available_seats, tickets_count)
        if isinstance(fn_value, str):
            return fn_value
        self.tickets_sold += tickets_count
        self.available_seats -= tickets_count

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price
