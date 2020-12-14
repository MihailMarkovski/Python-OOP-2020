# from Inheritance.mix_it_06E.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class Technology(CapacityMixin):
    def __init__(self, memory, memory_taken):
        self.memory = memory
        self.memory_taken = memory_taken
