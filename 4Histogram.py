import matplotlib.pyplot as plt
import numpy as np

# no=[12,34,56,78,98,76,54,34,22,34,54,55,66,77,88,99,12,32,43,54,16]
# plt.hist(no,color="white",edgecolor="green",bottom=10,cumulative=1,histtype="stepfilled",orientation="horizontal") #cumulative=1(increasing order) and -1 for decreasing
# #bottom=10 it means origin of graph will be (10,10)                                                        
# plt.title("HISTOGRAM GRAPH")
# plt.xlabel("Python")
# plt.ylabel("No")
# plt.axvline(45,color="g")
# plt.show()


# Generate random data
data = np.random.randn(1000)  # 1000 values from a normal distribution
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()




