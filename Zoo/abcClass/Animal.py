from abc import ABC, abstractmethod  # import library for create Abstract class
from random import randint  # import random for Determination gender


class Animal(ABC):  # Create a Abstract Class for All Classes
    _name = ""  # Animal's name
    _gender = randint(0, 1)  # Animal's Gender

    def getName(self):  # get Animal's name
        return self._name

    @abstractmethod
    def playSound(self):  # a abstract method for Animal's Sound
        pass

    def eat(self, food):  # eating methods for Animal
        return f"{self._name} eating {food}..."

    def __init__(self, name):  # Constructor for Animal Class
        self._name = name  # set Name
        # set Gender
        if self._gender == 0:
            self._gender = "M"
        else:
            self._gender = "F"

    # implement __repr__ method
    def __repr__(self):
        sound = self.playSound()
        return f"{self._name} say {sound}..."
