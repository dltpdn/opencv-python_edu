import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x**2

plt.plot(x,y)
plt.annotate('here', xy=(4,16), xytext=(5,20), arrowprops={'color':'green'})
plt.show()