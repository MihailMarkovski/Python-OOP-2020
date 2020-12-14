from collections import defaultdict


class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = defaultdict(int)

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        capacity = size / 2
        return cls(name, type, capacity)

    def add_item(self, item_name: str):
        if not self.capacity:
            return "Not enough capacity in the store"
        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        self.capacity += amount
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with" \
               f" capacity {self.capacity}"
