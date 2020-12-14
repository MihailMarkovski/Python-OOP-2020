# from Attributes_and_Methods.hotel_04.project.room import Room

# Comments are Doncho`s implementation
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        searched_rooms = [r for r in self.rooms if r.number == room_number]
        if searched_rooms:
            room = searched_rooms[0]
            if room.capacity >= people and not room.is_taken:
                room.is_taken = True
                room.guests += people
                self.guests += people

    #     def take_room(self, room_number, people):
    #         room = [r for r in self.rooms if r.number == room_number][0]
    #         result = room.take_room(people)
    #         if result:
    #             return result
    #         self.guests += people
    def free_room(self, room_number):
        searched_rooms = [r for r in self.rooms if r.number == room_number]
        if searched_rooms:
            room = searched_rooms[0]
            if room.is_taken:
                room.is_taken = False
                self.guests -= room.guests
                room.guests = 0

    #     def free_room(self, room_number):
    #         room = [r for r in self.rooms if r.number == room_number][0]
    #         result = room.free_room()
    #         guests_to_remove = room.guests
    #         if result:
    #             return result
    #         self.guests -= guests_to_remove
    def print_status(self):
        print(f'Hotel {self.name} has {self.guests} total guests')
        free_rooms = [str(s.number) for s in self.rooms if not s.is_taken]
        taken_rooms = [str(s.number) for s in self.rooms if s.is_taken]
        if free_rooms:
            print(f'Free rooms: {", ".join(free_rooms)}')
        if taken_rooms:
            print(f'Taken rooms: {", ".join(taken_rooms)}')

# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()
