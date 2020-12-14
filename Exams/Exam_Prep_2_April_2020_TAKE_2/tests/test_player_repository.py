import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.pr = PlayerRepository()

    def test_init(self):
        self.assertEqual(0, self.pr.count)
        self.assertEqual(0, len(self.pr.players))

    def test_add_raises(self):
        p = Advanced('test')
        self.pr.add(p)
        with self.assertRaises(ValueError) as ex:
            self.pr.add(p)
        self.assertEqual("Player test already exists!", str(ex.exception))

    def test_add_proper(self):
        p = Advanced('test')
        self.pr.add(p)
        self.assertEqual(1, self.pr.count)
        self.assertEqual(1, len(self.pr.players))

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pr.remove('')
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_remove_proper(self):
        p = Advanced('test')
        self.pr.add(p)
        self.assertEqual(1, self.pr.count)
        self.assertEqual(1, len(self.pr.players))
        self.pr.remove('test')
        self.assertEqual(0, self.pr.count)
        self.assertEqual(0, len(self.pr.players))

    def test_find(self):
        p = Advanced('test')
        self.pr.add(p)
        self.assertEqual(p, self.pr.find('test'))
