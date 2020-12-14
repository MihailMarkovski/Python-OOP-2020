# from Inheritance.mix_it_06E.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats, ticket_price):
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def get_ticket(self, tickets_count):
        try:
            self.get_capacity(self.available_seats, tickets_count)
            self.tickets_sold += tickets_count
            self.available_seats -= tickets_count
        except Exception as ex:
            return str(ex)

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price
