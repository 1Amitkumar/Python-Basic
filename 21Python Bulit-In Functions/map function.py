print(map(ord, ['a', 'b', 'c', 'd']))


print(list(map(ord, ['a', 'b', 'c', 'd'])))


def twice(x):
    return x*2


print(list(map(twice, [11, 22, 33, 44, 55])))
