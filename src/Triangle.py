from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("The figure is not a triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        s = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return round(s, 2)

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

