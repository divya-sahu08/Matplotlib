import matplotlib.pyplot as plt

x=[1,2,3,4,-5,4,3,2]
y=[2,3,-5,6,7,8,9,8]

plt.stem(x,y,bottom=2,basefmt="g",markerfmt="ro",label="python")
plt.show()