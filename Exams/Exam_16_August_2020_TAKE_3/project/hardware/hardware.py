from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.capacity_left = self.capacity
        self.memory_left = self.memory

    def install(self, software: Software):
        if self.capacity_left >= software.capacity_consumption and \
                self.memory_left >= software.memory_consumption:
            self.software_components.append(software)
            self.capacity_left -= software.capacity_consumption
            self.memory_left -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.capacity_left += software.capacity_consumption
        self.memory_left += software.memory_consumption
