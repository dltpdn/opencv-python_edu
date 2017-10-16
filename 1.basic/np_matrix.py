import numpy as np

a = np.arange(6).reshape(2,3)
b = np.array([1,2,3])

c = a + b
d = a * b
e = np.dot(a , b)
f = a.T

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a.dot(b))

