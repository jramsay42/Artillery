""" Unit testing the Gun class. """
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import Gun
import pytest

def test_gun_setup():
    """ Tests guns are constructed properly. """
    test_gun = Gun.Gun(2, 2)
    assert test_gun.get_azimuth() == 45
    assert test_gun.get_elevation() == 45
    assert test_gun.__repr__() == "Gun with position x: 2 y: 2"
    assert test_gun.calculate_trajectory() == (1041, 1041)
