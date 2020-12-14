from project.rooms.room import Room
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += (room.room_cost + room.expenses)
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        strings = []
        for room in self.rooms:
            total_expenses = room.room_cost + room.expenses
            if room.budget >= total_expenses:
                strings.append(f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= total_expenses
            else:
                strings.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(strings)

    def status(self):
        result = f'Total population: {sum(r.members_count for r in self.rooms)}\n'
        for r in self.rooms:
            result += f'{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n'
            if r.__class__.__name__ == 'YoungCoupleWithChildren':
                for i, c in enumerate(r.children):
                    result += f'--- Child {i + 1} monthly cost: {c.cost * 30:.2f}$\n'
            result += f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in r.appliances):.2f}$\n'
        return result
