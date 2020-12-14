from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not searched_hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = searched_hardware[0]
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]
        if not searched_hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = searched_hardware[0]
        try:
            hardware.install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        searched_hardware = [h for h in System._hardware if h.name == hardware_name]
        searched_software = [s for s in System._software if s.name == software_name]
        if (not searched_hardware) or (not searched_software):
            return "Some of the components do not exist"
        hardware = searched_hardware[0]
        software = searched_software[0]
        hardware.uninstall(software)
        System._software.remove(software)  # !!!!!!!!!!!!

    @staticmethod
    def analyze():
        result = f'''System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}
Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}'''
        return result

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += f'''Hardware Component - {h.name}
Express Software Components: {len([s for s in h.software_components if isinstance(s, ExpressSoftware)])}
Light Software Components: {len([s for s in h.software_components if isinstance(s, LightSoftware)])}
Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}
Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}
Type: {h.type}
Software Components: {None if not h.software_components else ", ".join(s.name for s in h.software_components)}'''
        return result
