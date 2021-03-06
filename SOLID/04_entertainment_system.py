from abc import abstractmethod, ABC


class Connector(ABC):
    @abstractmethod
    def connect(self, device):
        pass


class PowerConnector(Connector):
    def connect(self, device):
        self.connect_device_to_power_outlet(device)

    def connect_device_to_power_outlet(self, device): pass


class HDMIConnector(Connector):
    def connect(self, device):
        self.connect_to_device_via_hdmi_cable(device)

    def connect_to_device_via_hdmi_cable(self, device): pass


class RCAConnector(Connector):
    def connect(self, device):
        self.connect_to_device_via_rca_cable(device)

    def connect_to_device_via_rca_cable(self, device): pass


class EthernetConnector(Connector):
    def connect(self, device):
        self.connect_to_device_via_ethernet_cable(device)

    def connect_to_device_via_ethernet_cable(self, device): pass


class Television(RCAConnector, HDMIConnector, PowerConnector):
    def connect_to_dvd(self, dvd_player):
        RCAConnector.connect(self, dvd_player)

    def connect_to_game_console(self, game_console):
        HDMIConnector.connect(self, game_console)

    def plug_in_power(self):
        PowerConnector.connect(self)


class dvd_player(HDMIConnector, PowerConnector):
    def connect_to_tv(self, television):
        HDMIConnector.connect(television)

    def plug_in_power(self):
        PowerConnector.connect(self)


# continue the logic below
class GameConsole(HDMIConnector, EthernetConnector, PowerConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetConnector, PowerConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
