import pickle
f = open('pick.dat', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()