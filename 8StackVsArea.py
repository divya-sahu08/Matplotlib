import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
area1=[2,3,9,3,2,1]
area2=[4,5,6,7,2,1]

l=["area1","area2"]
plt.stackplot(x,area1,area2,labels=l,baseline="sym") # by default base line is zero
plt.legend(loc=2)
plt.show()