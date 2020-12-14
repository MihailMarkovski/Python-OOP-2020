from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        return sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        # d =√((x_2 - x_1)²+(y_2-y_1)²)
