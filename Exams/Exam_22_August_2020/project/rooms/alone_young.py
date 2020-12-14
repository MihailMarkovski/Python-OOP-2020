from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        tv = TV()
        self.appliances = [tv]
        self.expenses = sum([a.get_monthly_expense() for a in self.appliances])
