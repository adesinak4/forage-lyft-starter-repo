import unittest
from datetime import date

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_a = 0.6
        tire_b = 0.3
        tire_c = 0.9
        tire_d = 1.0
        tires = CarriganTires(tire_a, tire_b, tire_c, tire_d)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_a = 0.6
        tire_b = 0.3
        tire_c = 0.1
        tire_d = 0.8
        tires = CarriganTires(tire_a, tire_b, tire_c, tire_d)
        self.assertFalse(tires.needs_service())