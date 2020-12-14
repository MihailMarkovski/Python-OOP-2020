class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if milliliters <= self.size - self.quantity:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
