print(all(['alpha', 'beta', '']))

print(all(['one', 'two', 'three']))

print(all([]))

gen = (i for i in ['0', (), {}, 51, 89])  # generator
print(all(gen))