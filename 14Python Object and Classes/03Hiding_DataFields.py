class Account:

    # constructor or initializer
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money  # __balance is private now, so it is only accessible inside the class

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.__balance


b1 = Account('raj', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.check_balance())
print(b1.withdraw(800))
print(b1.check_balance())
