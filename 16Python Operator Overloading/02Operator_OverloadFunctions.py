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

    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius

    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius

    def __str__(self):
        return "Circle with radius " + str(self.__radius)


c1 = Circle_Detail(4)
print(c1.get_radius())

c2 = Circle_Detail(5)
print(c2.get_radius())

c3 = c1 + c2
print(c3.get_radius())

print(c3 > c2)  # Became possible because we have added __gt__ method

print(c1 < c2)  # Became possible because we have added __lt__ method

print(c3)  # Became possible because we have added __str__ method
