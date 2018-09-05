class Vehicle:

    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color

    def get_color(self):  # get_color() function is accessible to class Car
        return self.__color

    def set_color(self, color):  # set_color is accessible outside the class
        self.__color = color

    def get_name(self):  # get_name() is accessible outside the class
        return self.__name


class Car(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color
        super().__init__(name, color)
        self.__model = model

    def get_description(self):
        return self.get_name() + self.__model + " in " + self.get_color() + " color"


# in method get_description we are able to call get_name(), get_color() because they are
# accessible to child class through inheritance

c = Car("Ford Mustang", "red", "GT350")
print(c.get_description())
print(c.get_name())  # car has no method get_name() but it is accessible through class Vehicle