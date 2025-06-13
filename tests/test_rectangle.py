import pytest
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(3, 5, 15),
                          (3.5, 5.5, 19.25)],
                         ids=["integer", "float"])
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Rectangle area with sides {side_a} and {side_b} must be {area}'


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(0, 5),
                          (-3.5, 5)],
                         ids=["zero value", "negative value"])
def test_rectangle_area_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [(3, 5, 16),
                          (3.5, 5.5, 18)],
                         ids=["integer", "float"])
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f'Rectangle perimeter with sides {side_a} and {side_b} must be {perimeter}'


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(0, 5),
                          (-3.5, 5)],
                         ids=["zero value", "negative value"])
def test_rectangle_perimeter_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(3, 5),
                          (3.5, 5.5)],
                         ids=["integer", "float"])
def test_rectangle_add_area_positive(side_a, side_b):
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    assert r.add_area(s) == r.area + s.area, f'The Sum of {r.area} and {s.area} must be {r.add_area}'


@pytest.mark.parametrize("side_a",
                         [0, -3.5],
                         ids=["zero value", "negative value"])
def test_rectangle_add_area_negative(side_a):
    with pytest.raises(ValueError):
        Rectangle(3, 5).add_area(Square(side_a))
