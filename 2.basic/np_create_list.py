import numpy as np

a = np.array([1,2,3,4])
b = np.array([[1,2,3,4],
              [5,6,7,8]])
c = np.array([1,2,3.14, 4])
d = np.array([1,2,3,4], dtype=np.float64)

print(a, a.dtype, a.shape)
print(b, b.dtype, b.shape)
print(c, c.dtype, c.shape)
print(d, d.dtype, d.shape)