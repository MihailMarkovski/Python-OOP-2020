import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('name', 'type', 1000, 512)

    def test_init(self):
        self.assertEqual('name', self.hardware.name)
        self.assertEqual('type', self.hardware.type)
        self.assertEqual(1000, self.hardware.capacity)
        self.assertEqual(512, self.hardware.memory)
        self.assertListEqual([], self.hardware.software_components)

    def test_install_proper(self):
        software = ExpressSoftware('test', capacity_consumption=100, memory_consumption=100)
        self.hardware.install(software)
        self.assertListEqual([software], self.hardware.software_components)

    def test_install_raises(self):
        with self.assertRaises(Exception) as ex:
            software = ExpressSoftware('test', capacity_consumption=10000, memory_consumption=10000)
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall(self):
        software = ExpressSoftware('test', capacity_consumption=100, memory_consumption=100)
        self.hardware.install(software)
        self.assertListEqual([software], self.hardware.software_components)
        self.hardware.uninstall(software)
        self.assertListEqual([], self.hardware.software_components)
