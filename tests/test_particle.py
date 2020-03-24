"""
Test cases for the partticle module.
"""
import pytest

from infectionsim import Particle


def setup_particle():
    """
    Configure the particle object to run tests on.

    Returns
    -------
    Particle
        The configured particle object.
    """
    return Particle(1.0, 1.0, 0.1, 0.1, False, 100., 0.3, 0.2, 0.7)


def test_initialize():
    """
    Test that public members are initialized correctly.
    """
    particle = setup_particle()

    assert particle.x == pytest.approx(1.0)
    assert particle.y == pytest.approx(1.0)
    assert particle.is_alive == True


def test_update_position_advection():
    """
    Test that updating the position of the particle works correctly.
    """
    particle = setup_particle()
    particle.update_position(1.0)

    assert particle.x == pytest.approx(1.1)
    assert particle.y == pytest.approx(1.1)
