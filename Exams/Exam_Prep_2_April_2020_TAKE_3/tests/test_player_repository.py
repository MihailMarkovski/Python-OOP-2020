import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = PlayerRepository()

    def test_init(self):
        self.assertEqual(0, self.repo.count)
        self.assertListEqual([], self.repo.players)

    def test_add_raises(self):
        player = Advanced('test')
        self.repo.players.append(player)
        with self.assertRaises(ValueError):
            self.repo.add(player)

    def test_add_proper(self):
        player = Advanced('test')
        self.repo.add(player)
        self.assertEqual(1, self.repo.count)
        self.assertEqual(1, len(self.repo.players))

    def test_remove_raises(self):
        with self.assertRaises(ValueError):
            self.repo.remove('')

    def test_remove_proper(self):
        player = Advanced('test')
        self.repo.add(player)
        self.repo.remove('test')
        self.assertEqual(0, self.repo.count)
        self.assertEqual(0, len(self.repo.players))

    def test_find(self):
        player = Advanced('test')
        self.repo.add(player)
        self.assertEqual(player, self.repo.find('test'))