from models.animal import Animal

class Dog(Animal):

    def __init__(self, name: str, weight: float, age: int) -> None:
        super().__init__(name, weight, age)

    @classmethod
    def make_sound(clc):
        return "¡Guau!"
    
