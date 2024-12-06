from unittest import TestCase
from models.ferret import Ferret
from app import app

class TestFerret(TestCase):
    def setUp(self) -> None:
        self.ferret = Ferret("Angola", 23.9, "Joel", 2.3, 4)

    def tearDown(self) -> None:
        pass

    def test_ferret_sound(self):
        response = self.ferret.make_sound()
        self.assertEqual(response, "¡Eek, Eek!", "El sonido no corresponde con el sonido de un hurón.")

    def test_ferret_taxes(self):
        response = self.ferret.calculate_freight()
        self.assertEqual(response, round(23.9*2.3, 2), "El flete no fue calculado exitosamente.")
