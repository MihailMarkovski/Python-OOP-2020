# from Inheritance.mix_it_06E.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class Vehicle(CapacityMixin):
    def __init__(self, available_seats):
        self.available_seats = available_seats
