t = 1


def incre():
    # global t = 1   # this is error
    global t
    t = 100  # this is okay
    t = t + 1
    print(t)  # Displays 101


incre()
print(t)  # Displays 101
