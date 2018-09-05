a = 10

b = 5

print(id(a), id(b))

a = b  # a now references same object as b

print(id(a), id(b))
