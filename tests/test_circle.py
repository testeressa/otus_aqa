import pytest
from src.Circle import Circle


@pytest.mark.parametrize(("radius", "area"),
                         [(3, 28.27),
                          (3.5, 38.48)],
                         ids=["integer", "float"])
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.area == area, f'Circle area with radius {radius} must be {area}'


@pytest.mark.parametrize(("radius", "perimeter"),
                         [(3, 18.85),
                          (3.5, 21.99)],
                         ids=["integer", "float"])
def test_circle_perimeter(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == perimeter, f'Circle perimeter with radius {radius} must be {perimeter}'
