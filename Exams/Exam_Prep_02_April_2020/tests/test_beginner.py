import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_init(self):
        beg = Beginner('test')
        self.assertEqual('test', beg.username)
        self.assertEqual(50, beg.health)
        self.assertEqual(0, len(beg.card_repository.cards))
        self.assertEqual(0, beg.card_repository.count)

    def test_username_raise(self):
        beg = Beginner('test')
        with self.assertRaises(ValueError) as ex:
            beg.username = ''
        self.assertEqual(str(ex.exception), 'Player\'s username cannot be an empty string.')

    def test_username_setter(self):
        beg = Beginner('test')
        beg.username = 'new'
        self.assertEqual('new', beg.username)

    def test_health_raise(self):
        beg = Beginner('test')
        with self.assertRaises(ValueError) as ex:
            beg.health = -100
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_health_setter(self):
        beg = Beginner('test')
        beg.health = 100
        self.assertEqual(100, beg.health)

    def test_is_dead(self):
        beg = Beginner('test')
        self.assertFalse(beg.health <= 0)
        beg.health = 0
        self.assertTrue(beg.health <= 0)

    def test_take_damage_raises(self):
        beg = Beginner('test')
        with self.assertRaises(ValueError) as ex:
            beg.take_damage(-100)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage(self):
        beg = Beginner('test')
        beg.take_damage(25)
        self.assertEqual(25, beg.health)
