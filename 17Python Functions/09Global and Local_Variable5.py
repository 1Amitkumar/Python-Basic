def foo():
    global x  # x is declared as global available outside the function
    x = 100


foo()
print(x)
