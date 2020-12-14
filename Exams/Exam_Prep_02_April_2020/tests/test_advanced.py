import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_init(self):
        adv = Advanced('test')
        self.assertEqual('test', adv.username)
        self.assertEqual(250, adv.health)
        self.assertEqual(0, len(adv.card_repository.cards))
        self.assertEqual(0, adv.card_repository.count)

    def test_username_raise(self):
        adv = Advanced('test')
        with self.assertRaises(ValueError) as ex:
            adv.username = ''
        self.assertEqual(str(ex.exception), 'Player\'s username cannot be an empty string.')

    def test_username_setter(self):
        adv = Advanced('test')
        adv.username = 'new'
        self.assertEqual('new', adv.username)

    def test_health_raise(self):
        adv = Advanced('test')
        with self.assertRaises(ValueError) as ex:
            adv.health = -100
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_health_setter(self):
        adv = Advanced('test')
        adv.health = 100
        self.assertEqual(100, adv.health)

    def test_is_dead(self):
        adv = Advanced('test')
        self.assertFalse(adv.health <= 0)
        adv.health = 0
        self.assertTrue(adv.health <= 0)

    def test_take_damage_raises(self):
        adv = Advanced('test')
        with self.assertRaises(ValueError) as ex:
            adv.take_damage(-100)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage(self):
        adv = Advanced('test')
        adv.take_damage(100)
        self.assertEqual(150, adv.health)
