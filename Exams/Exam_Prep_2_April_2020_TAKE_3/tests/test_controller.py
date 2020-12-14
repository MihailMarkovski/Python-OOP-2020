import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.ctrl = Controller()

    def test_init(self):
        self.assertEqual(0, self.ctrl.card_repository.count)
        self.assertEqual(0, self.ctrl.player_repository.count)
        self.assertEqual(0, len(self.ctrl.card_repository.cards))
        self.assertEqual(0, len(self.ctrl.player_repository.players))

    def test_add_player(self):
        res = self.ctrl.add_player('Beginner', 'name')
        self.assertEqual(1, self.ctrl.player_repository.count)
        self.assertEqual(1, len(self.ctrl.player_repository.players))
        self.assertEqual("Successfully added player of type Beginner with username: name", res)

    def test_add_card(self):
        res = self.ctrl.add_card('Trap', 'name')
        self.assertEqual(1, self.ctrl.card_repository.count)
        self.assertEqual(1, len(self.ctrl.card_repository.cards))
        self.assertEqual("Successfully added card of type TrapCard with name: name", res)

    def test_add_player_card(self):
        pl = Beginner('beg')
        crd = MagicCard('mc')
        self.ctrl.player_repository.add(pl)
        self.ctrl.card_repository.add(crd)
        res = self.ctrl.add_player_card('beg', 'mc')
        self.assertEqual("Successfully added card: mc to user: beg", res)

    def test_fight(self):
        pl1 = Beginner('beg1')
        pl2 = Beginner('beg2')
        self.ctrl.player_repository.add(pl1)
        self.ctrl.player_repository.add(pl2)
        battlefield = BattleField()
        battlefield.fight(pl1, pl2)
        res = self.ctrl.fight('beg1', 'beg2')
        self.assertEqual('Attack user health 130 - Enemy user health 130', res)

    def test_report(self):
        pl = Beginner('test')
        c = MagicCard('name')
        self.ctrl.card_repository.add(c)
        self.ctrl.player_repository.add(pl)
        self.ctrl.add_player_card('test', 'name')
        expected = 'Username: test - Health: 50 - Cards 1\n### Card: name - Damage: 5\n'
        self.assertEqual(expected, self.ctrl.report())
