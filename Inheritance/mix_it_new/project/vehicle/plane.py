from project.vehicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, available_seats, rows, seats_per_row):
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

    def buy_tickets(self, row_number, tickets_count):
        if row_number not in range(1, self.rows + 1):
            return f"There is no row {row_number} in the plane!"

        seats = self.seats_available[row_number] if row_number in self.seats_available else self.seats_per_row
        fn_value = self.get_capacity(seats, tickets_count)
        if isinstance(fn_value, str):
            return f"Not enough tickets on row {row_number}!"
        self.seats_available[row_number] = self.seats_per_row - tickets_count
        self.available_seats -= tickets_count
        return tickets_count
