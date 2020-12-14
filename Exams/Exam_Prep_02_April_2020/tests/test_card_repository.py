import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestCardRepository(unittest.TestCase):
    def test_init(self):
        repo = CardRepository()
        self.assertEqual(0, repo.count)
        self.assertEqual(0, len(repo.cards))

    def test_add_raises(self):
        repo = CardRepository()
        c = MagicCard('test')
        repo.add(c)
        with self.assertRaises(ValueError) as ex:
            repo.add(c)
        self.assertEqual(str(ex.exception), "Card test already exists!")

    def test_add(self):
        repo = CardRepository()
        c = MagicCard('test')
        self.assertEqual(0, len(repo.cards))
        self.assertEqual(0, repo.count)
        repo.add(c)
        self.assertEqual(1, len(repo.cards))
        self.assertEqual(1, repo.count)

    def test_remove_raises(self):
        repo = CardRepository()
        with self.assertRaises(ValueError) as ex:
            repo.remove('')
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_remove(self):
        repo = CardRepository()
        c = MagicCard('test')
        repo.add(c)
        self.assertEqual(1, len(repo.cards))
        self.assertEqual(1, repo.count)
        repo.remove('test')
        self.assertEqual(0, len(repo.cards))
        self.assertEqual(0, repo.count)

    def test_find(self):
        repo = CardRepository()
        c = MagicCard('test')
        repo.add(c)
        self.assertEqual(c, repo.find('test'))
