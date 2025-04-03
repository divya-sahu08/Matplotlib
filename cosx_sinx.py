import numpy as np
import matplotlib.pyplot  as plt


x=np.arange(0, 5*np.pi, 0.1)
y=np.cos(x) ## y=np.sin(x)
plt.grid(True,color="red")
plt.plot(x,y,color="green")
plt.show()








