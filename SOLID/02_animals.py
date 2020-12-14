from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, species):
        self.sound = 'meow'

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self):
        self.sound = 'woof'

    def make_sound(self):
        return self.sound


class Dinosaur(Animal):
    def __init__(self):
        self.sound = 'dude, i`m dead'

    def make_sound(self):
        return self.sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Dinosaur()]
animal_sound(animals)
