import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def test_init(self):
        hw = Hardware('name', 'type', 1000, 512)
        self.assertEqual('name', hw.name)
        self.assertEqual('type', hw.type)
        self.assertEqual(1000, hw.capacity)
        self.assertEqual(512, hw.memory)
        self.assertEqual(0, len(hw.software_components))

    def test_install_raise(self):
        hw = Hardware('name', 'type', 1000, 512)
        with self.assertRaises(Exception) as ex:
            sw = ExpressSoftware('test', 111111111, 111111)
            hw.install(sw)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

    def test_install(self):
        hw = Hardware('name', 'type', 1000, 512)
        sw = ExpressSoftware('test', 100, 100)
        hw.install(sw)
        self.assertEqual(1, len(hw.software_components))

    def test_uninstall(self):
        hw = Hardware('name', 'type', 1000, 512)
        sw = ExpressSoftware('test', 100, 100)
        hw.install(sw)
        self.assertEqual(1, len(hw.software_components))
        hw.uninstall(sw)
        self.assertEqual(0, len(hw.software_components))