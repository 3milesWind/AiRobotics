import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

plt.plot(x, y, color="r")
plt.scatter(x, y, color='b')
for sx, sy in zip(x, y):
    label = f"({sx},{sy})"
    plt.annotate(label,
                 (sx, sy),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')
plt.show()