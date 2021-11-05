import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []
index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.clf()  # clear out previous layout
    plt.plot(x_vals, y_vals)  # re-plot the graph


animation = FuncAnimation(plt.gcf(), animate, interval=100)
plt.tight_layout()
plt.show()  # Show the data
