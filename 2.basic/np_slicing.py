import numpy as np

a = np.arange(10)
print(a)
print(a[5])
print(a[1:5])
print(a[5:])
print(a[:5])
print(a[:])

b = np.arange(16).reshape(4,-1)

print(b)
print(b[2, 2])
print(b[2, :])
print(b[:, 2])
print(b[1:3, :])


