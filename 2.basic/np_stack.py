import numpy as np

a = np.arange(4).reshape(2,2)
b = np.arange(10,14).reshape(2,2)

print(a)
print(b)

c = np.vstack( (a, b))
print(c)

d = np.hstack((a,b))
print(d)