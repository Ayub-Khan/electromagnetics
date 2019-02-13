# -*- coding: utf-8 -*-
""" Coulomb's law : a law stating that like charges repel and opposite charges attract,
 with a force proportional to the product of the charges and inversely proportional to
  the square of the distance between them. """
from electromagnetics.constants import *


def two_charges_vector_force(charge_1, charge_2, unit_vector, distance):
    """
    This will calculate the amount of repulsion or attraction force between two charges.
    This returns the vector force from charge_1 to charge_2
    param : charge_1 (Charge 1,  unit = C)
    param : charge_2 (Charge 2,  unit = C)
    param : unit_vector (Direction of force)
    param : distance (Distance between both charges, unit = m)
    :return: Total amount of repulsion or attraction force between charges.  unit : N

    Usage :
            two_charges_vector_force(10e-6, 10e-6 ,-1, .13)
    """
    return (COULOMBS_CONSTANT * charge_1 * charge_2) / (distance * distance) * unit_vector


def two_charges_vector_force_magnitude_only(charge_1, charge_2, distance):
    """
    This will calculate the amount of repulsion or attraction force between two charges.
    :param charge_1: Charge 1  unit : C
    :param charge_2: Charge 2  unit : C
    :param distance: Distance between both charges : m
    :return: Total amount of repulsion or attraction force between charges.  unit : N

    Usage:
        two_charges_vector_force(10e-6, 10e-6, .10)
    """
    return abs(two_charges_vector_force(charge_1, charge_2, 1, distance))


def accumulative_force_on_charge_by_other(main_charge, charges_dict_with_distance):
    """
    This returns the accumulative force on charge one by other charges.
    :param main_charge: Charge on which we are measuring force.  unit : C
    :param charges_dict_with_distance: list of charges with their distance and charge
            example= [
                {charge: amount, distance: amount, unit_vector: 1},
                {charge: amount, distance: amount, unit_vector: -1},
                {charge: amount, distance: amount, unit_vector: 1},
                ]
    :return: Total Accumulative force on main charge. unit : N

    Usage :
    accumulative_force_on_charge_by_other(
        10e-6,
        [
            {'charge':10e-6,'distance':.15,'unit_vector':-1},
            {'charge':10e-6,'distance':.6,'unit_vector':1},
            {'charge':10e-6,'distance':math.sqrt(.6*.6+.15*.15),'unit_vector':-1}
        ]
    )
    """
    accumulative_force = 0
    for item in charges_dict_with_distance:
        accumulative_force += two_charges_vector_force(
            main_charge,
            item['charge'],
            item['unit_vector'],
            item['distance']
        )
    return accumulative_force
