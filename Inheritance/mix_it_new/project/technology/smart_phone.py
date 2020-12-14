from project.technology.technology import Technology


class SmartPhone(Technology):
    def __init__(self, memory, memory_taken):
        super().__init__(memory, memory_taken)

    def install_apps(self, app, app_memory):
        fn_value = self.get_capacity(self.memory - self.memory_taken, app_memory)
        if isinstance(fn_value, str):
            return f"You don't have enough space for {app}!"
        self.memory_taken += app_memory
        return fn_value
