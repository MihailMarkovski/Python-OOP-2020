from project.appliances.appliance import Appliance


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for lst in args:
            for x in lst:
                if isinstance(x, Appliance):
                    total_cost += x.get_monthly_expense()
                else:
                    total_cost += x.cost
        self.expenses = total_cost
