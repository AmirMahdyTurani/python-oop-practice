from Zoo.abcClass.Animal import Animal  # import animal
from abc import ABC, abstractmethod  # import a library for create a abstract class


class Bird(Animal, ABC):  # create Bird Class
    def __init__(self, name):  # implement Bird class's constructor & super(Animal) Class's constructor
        super().__init__(name)

    @abstractmethod
    def playSound(self):  # implement a abstract method
        pass

    @abstractmethod  # create a abstract method for flying
    def fly(self, height):
        pass  # if a kind of Bird can not flying ypu can implement with pass Body or you can write this f"{self._name}
        # can not flying..."
