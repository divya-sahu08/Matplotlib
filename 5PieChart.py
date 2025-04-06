
import matplotlib.pyplot as plt

# x=[10,20,30,40]
# y=["c","java","c++","python"]
# plt.pie(x,labels=y)
# plt.show()

# x=[20,30,10]
# y=["java","cpp","python"]
# ex=[0.1,0.0,0.0]
# c=["r","b","g"]
# plt.pie(x,labels=y,explode=ex,colors=c,shadow="True",radius=0.3,textprops={"fontsize":15},counterclock=False)
# plt.show()


x=["india","china","russia","germany","poland"]
y=[12,32,15,20,22]

c=["red","green","blue","purple","white"]
plt.pie(y,labels=x,colors=c,autopct="%.0f", wedgeprops={'edgecolor': 'black'}) #autopct="%,2f"(for displaying in the form of percentage)
plt.show()