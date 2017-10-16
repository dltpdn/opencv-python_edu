import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x **2
plt.plot(x,y)
plt.xlim(2,5)
plt.ylim(5,20)
plt.show()