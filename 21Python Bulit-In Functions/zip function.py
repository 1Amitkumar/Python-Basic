print(zip([1, 2, 3, 4], "pow"))

print(list(zip([1, 2, 3, 4], "pow")))


for i, j, k, l in zip([1, 2, 3], "foo", ("one", "two", "three"), {"alpha", "beta", "gamma"}):
    print(i, j, k, l)


keys = ['alpha', 'beta', 'gamma']
values = [10, 20, 30]
d = dict(zip(keys, values))
print(d)
