import pickle
f = open('binary.dat', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()
