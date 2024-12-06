from models.exotic_animal import ExoticAnimal

class Ferret(ExoticAnimal):

    def __init__(self, origin_country: str, taxes: float, name: str, weight: float, age: int) -> None:
        super().__init__(origin_country, taxes, name, weight, age)

    @classmethod
    def make_sound(clc):
        return "¡Eek, Eek!"