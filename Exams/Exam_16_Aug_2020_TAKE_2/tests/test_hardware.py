import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hw = Hardware('name', 'type', 100, 1000)

    def test_init(self):
        self.assertEqual('name', self.hw.name)
        self.assertEqual('type', self.hw.type)
        self.assertEqual(100, self.hw.capacity)
        self.assertEqual(1000, self.hw.memory)
        self.assertListEqual([], self.hw.software_components)
        self.assertEqual(0, len(self.hw.software_components))

    def test_install_proper(self):
        sw = ExpressSoftware('test', 1, 1)
        self.hw.install(sw)
        self.assertIn(sw, self.hw.software_components)
        self.assertEqual(1, len(self.hw.software_components))

    def test_install_raises(self):
        sw = ExpressSoftware('test', 9999, 9999)
        with self.assertRaises(Exception) as ex:
            self.hw.install(sw)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall(self):
        sw = ExpressSoftware('test', 1, 1)
        self.hw.install(sw)
        self.hw.uninstall(sw)
        self.assertTrue(sw not in self.hw.software_components)
        self.assertEqual(0, len(self.hw.software_components))
