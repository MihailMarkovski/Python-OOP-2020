from project.rooms.room import Room
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = 0
        for room in self.rooms:
            expenses += (room.room_cost + room.expenses)
        return f"Monthly consumption: {expenses:.2f}$."

    def pay(self):
        all_strings = []
        for room in self.rooms:
            current_expenses = room.expenses + room.room_cost
            if room.budget >= current_expenses:
                all_strings.append(f"{room.family_name} paid {current_expenses:.2f}$ and"
                                   f" have {room.budget - current_expenses:.2f}$ left.")
                room.budget -= current_expenses
            else:
                all_strings.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(all_strings)

    def status(self):
        status_string = ''
        status_string += f'Total population: {sum(r.members_count for r in self.rooms)}\n'
        for r in self.rooms:
            counter = 0
            status_string += f'{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$,' \
                             f' Expenses: {r.expenses:.2f}$\n'
            if isinstance(r, YoungCoupleWithChildren):
                for c in r.children:
                    counter += 1
                    status_string += f'--- Child {counter} monthly cost: {c.cost * 30:.2f}$\n'
            status_string += f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in r.appliances):.2f}$\n'
        return status_string
