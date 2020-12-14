from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, (salary_one + salary_two), (2 + len(children)))
        self.room_cost = 30
        self.children = [c for c in children]
        self.members = 2 + len(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members
        self.expenses = sum(a.get_monthly_expense() for a in self.appliances) + sum(c.cost * 30 for c in self.children)
