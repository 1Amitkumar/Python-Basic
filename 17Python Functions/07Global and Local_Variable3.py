t = 1


def increment():
    global t  # now t inside the function is same as t outside the function
    t = t + 1
    print(t)  # Displays 2


increment()
print(t)  # Displays 2