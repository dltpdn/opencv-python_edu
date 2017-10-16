import numpy as np

a = np.zeros( (2,3))
b = np.zeros( (2,3,4), dtype=np.uint8)

c = np.ones( (2,3), dtype=np.float32)
d = np.empty( (2,3))
e = np.empty( (2,3), dtype=np.int16)
print(a, a.dtype, a.shape)
print(b, b.dtype, b.shape)
print(c, c.dtype, c.shape)
print(d, d.dtype, d.shape)