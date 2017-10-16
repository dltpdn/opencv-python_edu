import numpy as np


a= np.arange(3)  #[0,1,2]
b= np.arange(3.0) #[0.0, 1.0, 2.0]
c = np.arange(3,7) #[3,4,5,6]
d= np.arange(3,7,2) #[3,5]


e = np.random.rand(2,3)
print(a, a.dtype, a.shape)
print(b, b.dtype, b.shape)
print(c, c.dtype, c.shape)
print(d, d.dtype, d.shape)
print(e, e.dtype, e.shape)