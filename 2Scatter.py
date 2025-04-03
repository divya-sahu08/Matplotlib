import matplotlib.pyplot as plt

# for different color coordinate
x=[12,32,11,45,67,21]
y=[43,21,90,54,32,11]
colors=["red","green","blue","yellow","cyan","purple"]
size=[120,150,180,220,630,360]
plt.scatter(x,y,color=colors,sizes=size)
plt.title("temp vs vol")
plt.xlabel("temp")
plt.ylabel("vol")
plt.grid(True,color="green")
plt.show()
