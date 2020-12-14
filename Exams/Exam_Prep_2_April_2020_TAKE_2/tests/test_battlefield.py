import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.bf = BattleField()
        self.att = Advanced('att')
        self.en = Beginner('en')

    def test_is_dead(self):
        self.att.health = 0
        with self.assertRaises(ValueError) as ex:
            self.bf.fight(self.att, self.en)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_beginner_bonus(self):
        self.assertEqual(50, self.en.health)
        self.bf.fight(self.att, self.en)
        self.assertEqual(90, self.en.health)

    def test_card_damage_increase(self):
        c = TrapCard('cardname')
        self.en.card_repository.add(c)
        self.bf.fight(self.att, self.en)
        self.assertEqual(150, c.damage_points)

    def test_health_bonus(self):
        c = TrapCard('cardname')
        self.en.card_repository.add(c)
        self.bf.fight(self.att, self.en)
        self.assertEqual(95, self.en.health)

    def test_final_fight_logic(self):
        ac = TrapCard('test')
        ec = MagicCard('test2')
        self.att.card_repository.add(ac)
        self.en.card_repository.add(ec)
        self.bf.fight(self.att, self.en)
        self.assertEqual(50, self.en.health)
