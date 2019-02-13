# -*- coding: utf-8 -*-
"""Charge : Charge is a property of matter that creates force."""
from unittest import TestCase

from electromagnetics.charge import *


class TestChargeMethods(TestCase):

    def test_positive_charge(self):
        """Tests the functionality of function positive_charge()"""
        self.assertEqual(positive_charge(30), 1435835392.5743103)

    def test_negative_charge(self):
        """Tests the functionality of function positive_charge()"""
        self.assertEqual(negative_charge(30), -1435835392.5743103)
