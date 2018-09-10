globalVar = 12  # a global variable


def func():
    localVar = 100  # this is local variable
    print(globalVar)  # you can access global variables in side function


func()  # calling function func()

# print(localVar)        """{you can't access local_var outside the
                          # function, because as soon as function
                          # ends localVar is destroyed}"""
