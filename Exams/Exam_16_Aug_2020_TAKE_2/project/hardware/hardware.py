from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.available_capacity = self.capacity
        self.available_memory = self.memory

    def install(self, software: Software):
        if self.available_memory >= software.memory_consumption \
                and self.available_capacity >= software.capacity_consumption:
            self.software_components.append(software)
            self.available_capacity -= software.capacity_consumption
            self.available_memory -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.available_capacity += software.capacity_consumption
        self.available_memory += software.memory_consumption
