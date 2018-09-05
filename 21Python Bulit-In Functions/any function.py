print(any([10, "", "one"]))

print(any(("", {})))

print(any([]))

gen = (i for i in [5, 0, 0.0, 4])  # generator
print(any(gen))
