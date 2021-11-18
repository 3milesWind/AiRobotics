import math
import random
import time
import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def Swap(array, i , j):
    temp = copy.deepcopy(array[i])
    array[i] = array[j]
    array[j] = temp
    return array

def init():
    np.random.seed(40)
    array_size = (15, 2)
    array = np.random.randint(0, 100, size=array_size)
    return array

init_array = init()
arr = init_array

def animate(i):
    global arr
    minimumNode = i
    minimumValue = float('inf')
    for j in range (i + 1, len(arr)):
        temp = math.sqrt(abs(arr[j][0] - arr[i - 1][0]) ** 2 + abs(arr[j][1] - arr[i - 1][1]) ** 2)
        if minimumValue < temp:
            minimumNode = j
            minimumValue = temp
    print(arr)
    arr = Swap(arr, i, minimumNode)
    x = [x1[0] for x1 in arr]
    y = [x1[1] for x1 in arr]
    x.append(arr[0][0])
    y.append(arr[0][1])
    # k = 1
    # while k < len(arr):
    plt.clf()
    plt.plot(x, y, color="r")
    plt.scatter(x, y, color='b')
    time.sleep(1)
    # animation.event_source.stop()

animation = FuncAnimation(plt.gcf(), func=animate, frames=np.arange(1, len(arr), 1), interval=1)
plt.tight_layout()
plt.show()