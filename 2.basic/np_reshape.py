import numpy as np


a = np.arange(6)
b = a.reshape(2,3)

c = np.arange(24).reshape(2,3,4)

d = np.arange(100).reshape(-1, 5)
e = np.arange(100).reshape(2, -1)

f = np.ravel(c)

print(a, a.shape)
print(b, b.shape)
print(c, c.shape)
print(d, d.shape)
print(e, e.shape)
print(f, f.shape)
