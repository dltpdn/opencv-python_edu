import numpy as np

a = np.arange(10)
print(a)
b = a >4
print(b)
print(a[b])
print(a[a>4])

a[a>4] = 0
print(a)

names = np.array(['John', 'Tom', 'Lee', 'Tom'])
scores = np.random.rand(4,4) * 50 + 50
print(scores)
print(names=='Tom')
print(scores[names=='Tom',  :])