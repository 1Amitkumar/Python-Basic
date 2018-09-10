class NegativeAge(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age


def enter_age(age):
    if age < 0:
        raise NegativeAge("only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")


try:
    num = int(input("enter your age: "))
    enter_age(num)
except NegativeAge:
    print("only positive integers are allowed")
except:
    print("something is wrong")
