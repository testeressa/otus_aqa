import pytest
from src.Triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(3, 4, 5, 6),
                          (3.5, 4.5, 5.5, 7.85)],
                         ids=["integer", "float"])
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == area, f'Triangle area with sides {side_a}, {side_b}, {side_c} must be {area}'


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(0, 0, 0),
                          (-3.5, 4.5, 5.5)],
                         ids=["zero value", "negative value"])
def test_triangle_area_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"),
                         [(3, 3, 3, 9),
                          (3.5, 3.5, 3.5, 10.5)],
                         ids=["integer", "float"])
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f'Triangle perimeter with sides {side_a}, {side_b}, {side_c} must be {perimeter}'


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(0, 0, 0),
                          (-3.5, -4, -5.05)],
                         ids=["zero value", "negative value"])
def test_triangle_perimeter_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
