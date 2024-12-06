from abc import abstractmethod
from models.ianimal import IAnimal

class Animal(IAnimal):

    def __init__(self, name: str, weight: float, age: int):
        self._name = name
        self._weight = weight
        self._age = age
        self._kilos_eaten = 0.0

    @classmethod
    @abstractmethod
    def make_sound(clc):
        pass

    def eat(self, kilograms):
        self.kilos_eaten += kilograms
        

    @property
    def kilos_eaten(self) -> float:
        """ Devuelve el valor del atributo privado 'kilos_eaten' """
        return self._kilos_eaten
    
    @kilos_eaten.setter
    def kilos_eaten(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'kilos_eaten'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._kilos_eaten = value
        else:
            raise ValueError('Expected float')


    @property
    def name(self) -> str:
        """ Devuelve el valor del atributo privado 'name' """
        return self._name
    
    @name.setter
    def name(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'name'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('Expected str')
        
    @property
    def weight(self) -> float:
        """ Devuelve el valor del atributo privado 'weight' """
        return self._weight
    
    @weight.setter
    def weight(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'weight'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._weight = value
        else:
            raise ValueError('Expected float')
        
    @property
    def age(self) -> int:
        """ Devuelve el valor del atributo privado 'age' """
        return self._age
    
    @age.setter
    def age(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'age'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError('Expected int')


    