import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x **2

plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('money')
plt.title('money for time')
plt.show()