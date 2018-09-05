class Person:

    # constructor or initializer
    def __init__(self, name):
        self.name = name  # name is data field also commonly known as instance variables

    # method which returns a string

    def who(self):
        return "You are " + self.name


p1 = Person('tom')  # now we have created a new person object p1
print(p1.who())
print(p1.name)