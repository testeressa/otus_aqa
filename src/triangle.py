from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if (side_a + side_b + side_c) / 2 <= max(side_a, side_b, side_c):
            raise ValueError("The figure is not a triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        s = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return round(s, 2)

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


t = Triangle(5, 5, 5)
print(t.get_area())
print(t.get_perimeter())
print(t.add_area(t))
