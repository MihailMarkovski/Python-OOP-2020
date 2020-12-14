import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.cr = CardRepository()

    def test_init(self):
        self.assertEqual(0, self.cr.count)
        self.assertEqual(0, len(self.cr.cards))

    def test_add_raises(self):
        c = MagicCard('test')
        self.cr.add(c)
        with self.assertRaises(ValueError) as ex:
            self.cr.add(c)
        self.assertEqual("Card test already exists!", str(ex.exception))

    def test_add_proper(self):
        c = MagicCard('test')
        self.cr.add(c)
        self.assertEqual(1, self.cr.count)
        self.assertEqual(1, len(self.cr.cards))

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cr.remove('')
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_remove_proper(self):
        c = MagicCard('test')
        self.cr.add(c)
        self.assertEqual(1, self.cr.count)
        self.assertEqual(1, len(self.cr.cards))
        self.cr.remove('test')
        self.assertEqual(0, self.cr.count)
        self.assertEqual(0, len(self.cr.cards))

    def test_find(self):
        c = MagicCard('test')
        self.cr.add(c)
        self.assertEqual(c, self.cr.find('test'))
