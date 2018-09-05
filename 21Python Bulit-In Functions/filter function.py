def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


f = filter(is_even, [1, 3, 10, 45, 6, 50])

print(f)

for i in f:
    print(i)

print(list(filter(is_even, [1, 3, 10, 45, 6, 50])))
