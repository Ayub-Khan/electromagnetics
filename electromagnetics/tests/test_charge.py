# -*- coding: utf-8 -*-
"""Charge : Charge is a property of matter that creates force."""
from electromagnetics.charge import *


def test_positive_charge():
    """Tests the functionality of function positive_charge()"""
    assert positive_charge(30) == 1435835392.5743103


def test_negative_charge():
    """Tests the functionality of function positive_charge()"""
    assert negative_charge(30) == -1435835392.5743103
