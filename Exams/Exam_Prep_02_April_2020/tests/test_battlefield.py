import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def test_player_is_dead(self):
        a = Advanced('attacker')
        e = Beginner('enemy')
        a.health = 0
        bf = BattleField()
        with self.assertRaises(ValueError) as ex:
            bf.fight(a, e)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_beginner_health_increase(self):
        a = Advanced('attacker')
        e = Beginner('enemy')
        self.assertEqual(50, e.health)
        bf = BattleField()
        bf.fight(a, e)
        self.assertEqual(90, e.health)

    def test_bonus(self):
        a = Advanced('attacker')
        e = Beginner('enemy')
        c = MagicCard('magic')
        a.card_repository.add(c)
        self.assertEqual(a.health, 250)
        bf = BattleField()
        bf.fight(a, e)
        self.assertEqual(a.health, 330)

    def test_fight_logic_is_dead(self):
        a = Advanced('attacker')
        e = Beginner('enemy')
        c = TrapCard('trap')
        a.card_repository.add(c)
        bf = BattleField()
        with self.assertRaises(ValueError) as ex:
            bf.fight(a, e)
        self.assertEqual(str(ex.exception), 'Player\'s health bonus cannot be less than zero.')
