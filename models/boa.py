from models.exotic_animal import ExoticAnimal

class Boa(ExoticAnimal):

    def __init__(self, origin_country: str, taxes: float, name: str, weight: float, age: int) -> None:
        super().__init__(origin_country, taxes, name, weight, age)
        self.miece_eaten = 0

    def eat_mouse(self):
        if (self.miece_eaten >= 20):
            raise ValueError("¡Demasiados ratones!")
        else:
            self.miece_eaten += 1

    @classmethod
    def make_sound(clc):
        return "¡Tsss!"
    
    @property
    def miece_eaten(self) -> int:
        """ Devuelve el valor del atributo privado 'miece_eaten' """
        return self.__miece_eaten
    
    @miece_eaten.setter
    def miece_eaten(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'miece_eaten'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__miece_eaten = value
        else:
            raise ValueError('Expected int')
