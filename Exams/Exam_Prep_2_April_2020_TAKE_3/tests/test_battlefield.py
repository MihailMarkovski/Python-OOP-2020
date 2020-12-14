import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.bf = BattleField()
        self.attacker = Advanced('att')
        self.enemy = Beginner('en')

    def test_player_is_dead(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError):
            self.bf.fight(self.attacker, self.enemy)

    def test_beginner_bonus(self):
        card = TrapCard('test')
        self.enemy.card_repository.add(card)
        self.bf.fight(self.attacker, self.enemy)
        self.assertEqual(95, self.enemy.health)
        self.assertEqual(150, card.damage_points)

    def test_fight_logic(self):
        card = MagicCard('test')
        self.attacker.card_repository.add(card)
        self.bf.fight(self.attacker, self.enemy)
        self.assertEqual(85, self.enemy.health)
