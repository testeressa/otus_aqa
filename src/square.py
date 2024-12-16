from abc import ABC
from src.rectangle import Rectangle


class Square(Rectangle, ABC):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)




