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
            total += (room.expenses + room.room_cost)
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                result += f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.\n"
                room.budget -= total_expenses  # put it beneath to fit the test output
            else:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return result[:-1]

    def status(self):
        total_people = sum([x.members_count for x in self.rooms])
        result = f'Total population: {total_people}\n'
        for room in self.rooms:
            child_counter = 0
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if isinstance(room, YoungCoupleWithChildren):
                for child in room.children:
                    child_counter += 1
                    result += f'--- Child {child_counter} monthly cost: {child.cost * 30:.2f}$\n'
            result += f'--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$\n'
        return result[:-1]
