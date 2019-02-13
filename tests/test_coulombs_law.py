# -*- coding: utf-8 -*-
""" Coulomb's law : a law stating that like charges repel and opposite charges attract,
 with a force proportional to the product of the charges and inversely proportional to
  the square of the distance between them. """
import math
from unittest import TestCase

from electromagnetics.coulombs_law import *


class TestCoulombsLawMethods(TestCase):

    def test_two_charges_vector_force(self):
        """Tests the functionality of two_charges_vector_force."""
        self.assertEqual(two_charges_vector_force(10e-6, 10e-6, -1, .13), -53.180779806912284)

    def test_two_charges_vector_force_magnitude_only(self):
        """Tests the functionality of two_charges_vector_force_magnitude_only."""
        self.assertEqual(two_charges_vector_force_magnitude_only(10e-6, 10e-6, .13), 53.180779806912284)

    def test_accumulative_force_on_charge_by_other(self):
        """Tests the functionality of accumulative_force_on_charge_by_other."""
        self.assertEqual(accumulative_force_on_charge_by_other(
            10e-6,
            [
                {
                    'charge': 10e-6,
                    'distance': .15,
                    'unit_vector': -1
                },
                {
                    'charge': 10e-6,
                    'distance': .6,
                    'unit_vector': 1
                },
                {
                    'charge': 10e-6,
                    'distance': math.sqrt(.6*.6+.15*.15),
                    'unit_vector': -1
                }
            ]
        ), -39.79781918916301)
