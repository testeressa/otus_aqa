import math
from src.figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        s = self.radius ** 2 * math.pi
        return round(s, 2)

    def get_perimeter(self):
        circle = 2 * math.pi * self.radius
        return round(circle, 2)


c = Circle(4)
print(c.get_area())
print(c.get_perimeter())
print(c.add_area(c))

