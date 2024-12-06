from models.boa import Boa
from models.ferret import Ferret

lucas = Boa("Bolivia", 100, "Lucas", 12.3, 2)
garret = Ferret("México", 112, "Garret", 6.2, 7)

print("El flete de la boa es: " + str(lucas.calculate_freight()))
print("Lucas ha comido estos ratones: " + str(lucas.miece_eaten))

lucas.eat_mouse()

print("Lucas ahora ha comido estos ratones: " + str(lucas.miece_eaten))
print("Lucas hace el sonido: " + str(lucas.make_sound()))

print("Garret hace el sonido: " + str(garret.make_sound()))