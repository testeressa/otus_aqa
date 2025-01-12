import pytest
from src.Square import Square


@pytest.mark.parametrize(("side_a", "area"),
                         [(3, 9), (3.5, 12.25)],
                         ids=["integer", "float"])
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f'Square with side {side_a} must be {area}'


@pytest.mark.parametrize("side_a",
                         [0, -3.5],
                         ids=["zero value", "negative value"])
def test_rectangle_area_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
