# from Inheritance.mix_it_06E.project.technology.technology import Technology
from project.technology.technology import Technology


class SmartPhone(Technology):

    def install_apps(self, app, app_memory):
        try:
            memory_left = self.get_capacity(self.memory, app_memory + self.memory_taken)
            self.memory_taken += app_memory
            return memory_left
        except Exception:
            return f"You don't have enough space for {app}!"
