t = 1


def increment():
    # global t = 1   # this is error
    global t
    t = 100  # this is okay
    t = t + 1
    print(t)  # Displays 101


increment()
print(t)  # Displays 101