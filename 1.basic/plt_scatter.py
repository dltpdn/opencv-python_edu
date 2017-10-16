import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y = np.arange(2, 6)
x2 = np.arange(1.5,5.5)
y2 = np.arange(2.5,6.5)
plt.scatter(x, y)
plt.scatter(x2, y2, s=80, c='r', marker='^')
plt.show()