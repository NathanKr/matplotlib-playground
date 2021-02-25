import matplotlib.pyplot as plt
import numpy as np

xpoints = np.arange(10)
ypoints = xpoints ** 2

plt.plot(xpoints, ypoints,'o')
plt.title('plt x vs y')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
