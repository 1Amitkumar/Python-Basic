import pickle
f = open('pick.dat', 'wb')  # Your file name "Pick.dat"
pickle.dump(11, f)
pickle.dump("this is a line", f)
pickle.dump([1, 2, 3, 4], f)
f.close()
print("Binary Written")