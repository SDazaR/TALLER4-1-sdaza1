from unittest import TestCase
from models.boa import Boa

class TestBoa(TestCase):
    def setUp(self) -> None:
        self.boa = Boa("Jamaica", 21.9, "Kled", 8.3, 7)

    def tearDown(self) -> None:
        pass

    def test_boa_sound(self):
        response = self.boa.make_sound()
        self.assertEqual(response, "¡Tsss!", "El sonido no corresponde con el sonido de una boa.")

    def test_boa_taxes(self):
        response = self.boa.calculate_freight()
        self.assertEqual(response, round(21.9*8.3, 2), "El flete no fue calculado exitosamente.")

    def test_boa_eat_mouse(self):
        previous_miece = self.boa.miece_eaten
        self.boa.eat_mouse()
        post_miece = self.boa.miece_eaten
        self.assertEqual(post_miece - previous_miece, 1, "La boa no comió un ratón.")