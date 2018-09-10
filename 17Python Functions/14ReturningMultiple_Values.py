def big(a, b):
    if a > b:
        return a, b
    else:
        return b, a


s = big(12, 100)
print(s)
print(type(s))
