"""Tests for the fairsharer_package.fair_sharer module.
"""
from fairsharer.fair_sharer import fair_sharer


def test_fair_sharer_single_iteration():
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert result == [100, 800, 900, 0]


def test_fair_sharer_two_iterations():
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert result == [100, 890, 720, 90]


def test_fair_sharer_conservation():
    values = [10, 20, 30]
    result = fair_sharer(values, 10)
    assert sum(result) == sum(values)
