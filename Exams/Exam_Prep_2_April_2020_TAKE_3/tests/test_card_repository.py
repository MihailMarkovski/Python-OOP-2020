import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = CardRepository()

    def test_init(self):
        self.assertEqual(0, self.repo.count)
        self.assertListEqual([], self.repo.cards)

    def test_add_raises(self):
        card = MagicCard('test')
        self.repo.cards.append(card)
        with self.assertRaises(ValueError):
            self.repo.add(card)

    def test_add_proper(self):
        card = MagicCard('test')
        self.repo.add(card)
        self.assertEqual(1, self.repo.count)
        self.assertEqual(1, len(self.repo.cards))

    def test_remove_raises(self):
        with self.assertRaises(ValueError):
            self.repo.remove('')

    def test_remove_proper(self):
        card = MagicCard('test')
        self.repo.add(card)
        self.repo.remove('test')
        self.assertEqual(0, self.repo.count)
        self.assertEqual(0, len(self.repo.cards))

    def test_find(self):
        card = MagicCard('test')
        self.repo.add(card)
        self.assertEqual(card, self.repo.find('test'))