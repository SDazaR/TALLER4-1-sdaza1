from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def eat(self, kilograms):
        pass

    @abstractmethod
    def kilos_eaten(self) -> float:
        pass