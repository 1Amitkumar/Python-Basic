import math


class Circle_Detail:

    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, another_circle):
        return Circle_Detail(self.__radius + another_circle.__radius)


c1 = Circle_Detail(4)
print(c1.get_radius())

c2 = Circle_Detail(5)
print(c2.get_radius())

c3 = c1 + c2  # This is possible because we have overloaded + operator by adding a    method named __add__
print(c3.get_radius())
