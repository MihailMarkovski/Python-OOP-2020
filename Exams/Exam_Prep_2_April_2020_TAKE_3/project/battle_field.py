from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if isinstance(attacker, Beginner):
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if isinstance(enemy, Beginner):
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        att_bonus = sum(c.health_points for c in attacker.card_repository.cards)
        attacker.health += att_bonus

        en_bonus = sum(c.health_points for c in enemy.card_repository.cards)
        enemy.health += en_bonus

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                return

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
            if attacker.is_dead:
                return
