import math
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        s = self.radius ** 2 * math.pi
        return round(s, 2)

    @property
    def perimeter(self):
        circle = 2 * math.pi * self.radius
        return round(circle, 2)


c = Circle(4)
print(c.area)
print(c.perimeter)
print(c.add_area(c))

