import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x **2
y2 = x*5 + 2

plt.plot(x,y, 'b', label='first')
plt.plot(x,y2, 'r', label='second')
plt.legend(loc='upper right')
plt.show()