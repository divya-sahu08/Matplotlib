import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 0, 1]
y = [2, 3, 4, 4, 3, 2, 1, 1, 0, 1, 2, 2, 2, 2]

plt.step(x,y)
plt.grid()
plt.show()
