from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.live_capacity = self.capacity
        self.live_memory = self.memory

    def install(self, software: Software):
        if software.capacity_consumption > self.capacity or software.memory_consumption > self.memory \
                or software.memory_consumption > self.live_memory \
                or software.capacity_consumption > self.live_capacity:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)
        self.live_memory -= software.memory_consumption
        self.live_capacity -= software.capacity_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.live_memory += software.memory_consumption
        self.live_capacity += software.capacity_consumption
