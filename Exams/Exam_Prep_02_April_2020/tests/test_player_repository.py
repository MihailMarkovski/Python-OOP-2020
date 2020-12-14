import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init(self):
        repo = PlayerRepository()
        self.assertEqual(0, repo.count)
        self.assertEqual(0, len(repo.players))

    def test_add_raises(self):
        repo = PlayerRepository()
        p = Advanced('test')
        repo.add(p)
        with self.assertRaises(ValueError) as ex:
            repo.add(p)
        self.assertEqual(str(ex.exception), "Player test already exists!")

    def test_add(self):
        repo = PlayerRepository()
        p = Advanced('test')
        self.assertEqual(0, len(repo.players))
        self.assertEqual(0, repo.count)
        repo.add(p)
        self.assertEqual(1, len(repo.players))
        self.assertEqual(1, repo.count)

    def test_remove_raises(self):
        repo = PlayerRepository()
        with self.assertRaises(ValueError) as ex:
            repo.remove('')
        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")

    def test_remove(self):
        repo = PlayerRepository()
        p = Advanced('test')
        repo.add(p)
        self.assertEqual(1, len(repo.players))
        self.assertEqual(1, repo.count)
        repo.remove('test')
        self.assertEqual(0, len(repo.players))
        self.assertEqual(0, repo.count)

    def test_find(self):
        repo = PlayerRepository()
        p = Advanced('test')
        repo.add(p)
        self.assertEqual(p, repo.find('test'))
