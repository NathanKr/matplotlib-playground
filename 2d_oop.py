import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

#1. create a figure,like canvas
fig = plt.figure() 

#2. add plots inside that figure you just created
ax = fig.add_subplot(111) # (nrows, ncols, index)

#3. set all the parameters for the plot inside that ax 
ax.set(title='plt x vs y',ylabel='y', xlabel='x')

#4. do the plotting       
ax.plot(xpoints, ypoints)
plt.show()
