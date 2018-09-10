class Car:

    # constructor or initializer
    def __init__(self, name):
        self.name = name  # name is data field also known as instance variables

    # method which returns a string

    def who(self):
        return "this is " + self.name


p1 = Car('audi_a6')  # now we have created a new car object p1
print(p1.who())
print(p1.name)
