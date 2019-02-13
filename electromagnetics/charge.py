# -*- coding: utf-8 -*-
"""Charge : Charge is a property of matter that creates force."""
from electromagnetics.constants import *


def positive_charge(weight):
    """
    This calculates the total amount of positive in a item

    :param weight: weight in kgs

    :return: charge : charge in coulomb
    """
    return (weight/(PROTON_MASS+NEUTRON_MASS))*PROTON_CHARGE


def negative_charge(weight):
    """
    This calculates the total amount of negative charge in a item

    :param weight: weight in kgs

    :return: charge : charge in coulomb
    """
    return (weight/(PROTON_MASS+NEUTRON_MASS))*ELECTRON_CHARGE
