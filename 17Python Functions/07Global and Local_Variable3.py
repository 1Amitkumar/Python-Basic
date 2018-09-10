t = 1


def incre():
    global t  # now t inside the function is same as t outside the function
    t = t + 1
    print(t)  # Displays 2


incre()
print(t)  # Displays 2
