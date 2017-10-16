import numpy as np

a = np.arange(12)
print(a)
b = np.hsplit(a, 3)
print(b)

c = np.hsplit(a, (3,6))
print(c)