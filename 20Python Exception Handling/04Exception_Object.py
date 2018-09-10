try:
    num = eval(input("enter a number: "))
    print("the number entered is", num)
except NameError as ex:
    print("Exception:", ex)
