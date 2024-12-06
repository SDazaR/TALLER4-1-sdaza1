from models.animal import Animal
from abc import abstractmethod

class ExoticAnimal(Animal):

    def __init__(self, origin_country: str, taxes: float, name: str, weight: float, age: int) -> None:
        super().__init__(name, weight, age)
        self.origin_country = origin_country
        self.taxes = taxes

    def calculate_freight(self):
        return round(self.taxes*self.weight, 2)
    
    @abstractmethod
    def make_sound(self):
        pass

    @property
    def origin_country(self) -> str:
        """ Devuelve el valor del atributo privado 'origin_country' """
        return self._origin_country
    
    @origin_country.setter
    def origin_country(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'origin_country'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._origin_country = value
        else:
            raise ValueError('Expected str')
        
    @property
    def taxes(self) -> float:
        """ Devuelve el valor del atributo privado 'taxes' """
        return self._taxes
    
    @taxes.setter
    def taxes(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'taxes'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._taxes = value
        else:
            raise ValueError('Expected float')