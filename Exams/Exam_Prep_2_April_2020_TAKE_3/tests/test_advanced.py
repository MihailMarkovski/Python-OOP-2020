import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Advanced('test')

    def test_init(self):
        self.assertEqual('test', self.player.username)
        self.assertEqual(250, self.player.health)
        self.assertEqual(0, len(self.player.card_repository.cards))
        self.assertEqual(0, self.player.card_repository.count)

    def test_username_raises(self):
        with self.assertRaises(ValueError):
            self.player.username = ''

    def test_username_proper(self):
        self.player.username = 'new'
        self.assertEqual('new', self.player.username)

    def test_health_raises(self):
        with self.assertRaises(ValueError):
            self.player.health = -1

    def test_health_proper(self):
        self.player.health = 3
        self.assertEqual(3, self.player.health)

    def test_is_dead(self):
        self.player.health = 3
        self.assertFalse(self.player.is_dead)

    def test_take_damage_raises(self):
        with self.assertRaises(ValueError):
            self.player.take_damage(-1)

    def test_take_damage_proper(self):
        self.player.health = 5
        self.player.take_damage(1)
        self.assertEqual(4, self.player.health)