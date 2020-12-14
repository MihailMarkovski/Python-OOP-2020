import unittest

from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self):
        self.ctrl = Controller()

    def test_init(self):
        self.assertTrue(isinstance(self.ctrl.player_repository, PlayerRepository))
        self.assertTrue(isinstance(self.ctrl.card_repository, CardRepository))

    def test_add_player(self):
        expected = self.ctrl.add_player('Beginner', 'testname')
        self.assertEqual(1, len(self.ctrl.player_repository.players))
        self.assertEqual(expected, "Successfully added player of type Beginner with username: testname")

    def test_add_card(self):
        expected = self.ctrl.add_card('Trap', 'testname')
        self.assertEqual(1, len(self.ctrl.card_repository.cards))
        self.assertEqual(expected, "Successfully added card of type TrapCard with name: testname")

    def test_add_player_card(self):
        card = MagicCard('test')
        player = Beginner('name')
        self.ctrl.card_repository.add(card)
        self.ctrl.player_repository.add(player)
        expected = self.ctrl.add_player_card('name', 'test')
        self.assertEqual(expected, "Successfully added card: test to user: name")

    def test_fight(self):
        attacker = Advanced('p1')
        enemy = Advanced('p2')
        ac = MagicCard('card1')
        attacker.card_repository.add(ac)
        ec = MagicCard('card2')
        enemy.card_repository.add(ec)
        self.ctrl.player_repository.add(attacker)
        self.ctrl.player_repository.add(enemy)
        expected = "Attack user health 325 - Enemy user health 325"
        self.assertEqual(expected, self.ctrl.fight('p1', 'p2'))

    def test_report(self):
        self.ctrl.add_player('Beginner', 'name')
        self.ctrl.add_card('Magic', 'cardname')
        self.ctrl.add_player_card('name', 'cardname')
        expected = f'Username: name - Health: 50 - Cards 1\n### Card: cardname - Damage: 5\n'
        res = self.ctrl.report()
        self.assertEqual(expected, res)
