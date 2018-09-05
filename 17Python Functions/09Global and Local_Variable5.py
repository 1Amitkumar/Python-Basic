def foo():
    global x  # x is declared as global so it is available outside the function
    x = 100


foo()
print(x)