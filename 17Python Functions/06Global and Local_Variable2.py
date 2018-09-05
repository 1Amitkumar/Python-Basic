xy = 100


def cool():
    xy = 200  # xy inside the function is totally different from xy outside the function
    print(xy)  # this will print local xy variable i.e 200


cool()

print(xy)  # this will print global xy variable i.e 100