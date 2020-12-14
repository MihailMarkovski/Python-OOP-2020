from project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory, memory_taken):
        super().__init__(memory, memory_taken)

    def install_software(self, software, software_memory):
        fn_value = self.get_capacity(self.memory - self.memory_taken, software_memory)
        if isinstance(fn_value, str):
            return f"You don't have enough space for {software}!"
        self.memory_taken += software_memory
        return fn_value
