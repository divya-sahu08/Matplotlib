
import matplotlib.pyplot as plt

x=["warsaw","keev","mogadishu","helsinli","dublin","bern"]
y=[12000,80000,45000,55000,85000,165000]
colors=["red","green","blue","yellow","cyan","purple"]
plt.bar(x,y,color=colors) # barh for horizontal graph and bar is by default vertical graph
plt.xticks(fontsize=10, fontstyle='italic',rotation=45)
plt.show()

