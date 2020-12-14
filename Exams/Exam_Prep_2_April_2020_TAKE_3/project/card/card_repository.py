from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if [c for c in self.cards if c.name == card.name]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        card_to_go = [c for c in self.cards if c.name == card][0]
        self.cards.remove(card_to_go)
        self.count -= 1

    def find(self, name: str):
        return [c for c in self.cards if c.name == name][0]
