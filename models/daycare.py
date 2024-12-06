from models.boa import Boa

class Daycare():

    boa_1 = Boa("Francia", 21.1, "Lucy", 8.0, 2)
    boa_2 = Boa("Alemania", 21.7, "Nilah", 3.0, 6)

    def feed_boa(self, name: str) -> None:

        try:
            if name == self.boa_1.name:
                self.boa_1.eat_mouse()
                return "Éxito"
            elif name == self.boa_2.name:
                self.boa_2.eat_mouse()
                return "Éxito"
            else:
                return "Esta boa no existe"
        except ValueError as e:
            return "La boa está llena"