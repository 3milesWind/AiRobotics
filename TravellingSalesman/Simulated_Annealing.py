import math
import random
import time
import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def randomSwap(array):
    index1 = random.randint(0, len(array) - 1)
    index2 = random.randint(0, len(array) - 1)
    while index1 == index2:
        index2 = random.randint(0, len(array) - 1)
    temp = copy.deepcopy(array[index1])
    array[index1] = array[index2]
    array[index2] = temp
    return array


def calDistanceScore(array):
    # print(arr)
    score = 0
    for i in range(len(array)):
        if i == 0:
            continue
        else:
            score += math.sqrt(abs(array[i][0] - array[i - 1][0]) ** 2 + abs(array[i][1] - array[i - 1][1]) ** 2)
    return score


def init():
    np.random.seed(40)
    array_size = (15, 2)
    array = np.random.randint(0, 100, size=array_size)
    return array


temperature = 1000
init_array = init()
arr = init_array
Score = float('inf')
x = [x1[0] for x1 in arr]
y = [x1[0] for x1 in arr]
count = 0
start = time.time()
animation = None
pattern = 1

# ----- print the table for Temperature
temperature_list = []
possible_change = []
accept_list = []

def animate(i):
    global arr, temperature, Score, x, y, count
    count += 1
    newArray = randomSwap(arr)
    newScore = calDistanceScore(newArray)
    if newScore >= Score:
        temperature_list.append(temperature)
        possible_change.append(np.exp(-(newScore - Score) / temperature))

        if np.exp(-(newScore - Score) / temperature) >= np.random.uniform(0, 1):
            accept_list.append("x")
            arr = newArray
            x = [x1[0] for x1 in arr]
            y = [x1[1] for x1 in arr]
            x.append(arr[0][0])
            y.append(arr[0][1])
        else:
            accept_list.append("")
    else:
        Score = newScore
        arr = newArray
        x = [x1[0] for x1 in arr]
        y = [x1[1] for x1 in arr]
        x.append(arr[0][0])
        y.append(arr[0][1])
    # print(arr)

    # k = 1
    plt.clf()
    # while k < len(arr):
    plt.plot(x, y, color="r")
    plt.scatter(x, y, color='b')
    string = "Distance: " + str(round(Score, 2)) + "  " + "Count: " + str(count) + " Temp: " + str(
        round(temperature, 2))
    plt.title(string)
    for sx, sy in zip(x, y):
        label = f"({sx},{sy})"
        plt.annotate(label,
                     (sx, sy),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')
    if pattern == 1:
        temperature = temperature / count
    elif pattern == 2:
        temperature = 0.98 * temperature
    else:
        temperature = temperature * math.log(2) / math.log(count + 1)
        print(temperature)

    #print(temperature)
    if temperature < 10 ** (-10):
        animation.event_source.stop()
        # plt.clf()
        # while k < len(arr):
        # ------------print the acceptance rate
        # plt.plot(temperature_list, possible_change)
        # i = 0
        # for sx, sy in zip(temperature_list, possible_change):
        #     label = accept_list[i]
        #     plt.annotate(label,
        #                  (sx, sy),
        #                  textcoords="offset points",
        #                  xytext=(0, 10),
        #                  ha='center')
        #     i+=1
        # if pattern == 1:
        # plt.scatter(x, y, color='b')
        printResult()


def printResult():
    current = time.time()
    print("Total Time for Simulated Annealing:  " + str(current - start))
    print("The Score: ", Score)

def RunTask(k,temp):
    global animation, pattern, temperature, arr, Score, x, \
        y, count, start, animation, temperature_list, possible_change,accept_list
    temperature = temp
    arr = init_array
    Score = float('inf')
    pattern = k
    x = [x1[0] for x1 in arr]
    y = [x1[0] for x1 in arr]
    count = 0
    temperature_list = []
    possible_change = []
    accept_list = []
    start = time.time()
    animation = None
    animate(0)
    animation = FuncAnimation(plt.gcf(), func=animate, frames=np.arange(0, 1000, 1), interval=1)
    plt.tight_layout()
    plt.show()






if __name__ == '__main__':
    print("Select the Annealing Schedule: \nFast Annealing: 1\n Exponential Annealing: 2\nLog Annealing: 3\n")
    # RunTask(2, 10)
    # RunTask(2, 100)
    # RunTask(2, 500)
    RunTask(2, 10000)
    RunTask(2, 100000)
