import unittest

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def test_init(self):
        c = Controller()
        self.assertEqual(0, c.player_repository.count)
        self.assertEqual(0, len(c.player_repository.players))
        self.assertEqual(0, c.card_repository.count)
        self.assertEqual(0, len(c.card_repository.cards))

    def test_add_player(self):
        c = Controller()
        res = c.add_player('Advanced', 'test')
        self.assertEqual(c.player_repository.count, 1)
        self.assertEqual(len(c.player_repository.players), 1)
        self.assertEqual(res, "Successfully added player of type Advanced with username: test")

    def test_add_card(self):
        c = Controller()
        res = c.add_card('Trap', 'test')
        self.assertEqual(c.card_repository.count, 1)
        self.assertEqual(len(c.card_repository.cards), 1)
        self.assertEqual(res, "Successfully added card of type TrapCard with name: test")

    def test_add_player_card(self):
        ctrl = Controller()
        p = Beginner('pname')
        c = TrapCard('cname')
        ctrl.player_repository.add(p)
        ctrl.card_repository.add(c)
        res = ctrl.add_player_card('pname', 'cname')
        self.assertEqual(res, "Successfully added card: cname to user: pname")

    def test_fight(self):
        ctrl = Controller()
        attacker = Advanced('p1')
        enemy = Advanced('p2')
        ac = MagicCard('card1')
        attacker.card_repository.add(ac)
        ec = MagicCard('card2')
        enemy.card_repository.add(ec)
        ctrl.player_repository.add(attacker)
        ctrl.player_repository.add(enemy)
        expected = "Attack user health 325 - Enemy user health 325"
        self.assertEqual(expected, ctrl.fight('p1', 'p2'))

    def test_report(self):
        ctrl = Controller()
        p = Beginner('pname')
        c = TrapCard('cname')
        p.card_repository.add(c)
        ctrl.player_repository.add(p)
        expected = f'Username: pname - Health: 50 - Cards 1\n' \
                   f'### Card: cname - Damage: 120\n'
        res = ctrl.report()
        self.assertEqual(res, expected)
