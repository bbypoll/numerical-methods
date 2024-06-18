import numpy as np
import math as m
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm

eps = 0.01
a, b = c, d = 0, 10
matplotlib.use("TkAgg")
def f(x, y):
    return  x + 3 * y
def SimpleIterationMethod(x, N, h):
    X = np.copy(x)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            X[i][j] = 1 / 4 * (x[i][j - 1] + x[i][j + 1] + x[i - 1][j] + x[i + 1][j] + f(i * h,j * h) * (h ** 2))
    return X
def SimpleDiff(x, y):
    result = 0
    length = len(x)
    for i in range(length):
        for j in range(len(x[i])):
            result += (x[i][j] - y[i][j]) ** 2
    return m.sqrt(result)
def SeidelMethod(x, N, h):
    X = np.copy(x)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            X[i][j] = 1 / 4 * (X[1][j - 1] + x[i][j + 1] + x[i - 1][j] + x[i + 1][j] + f(1 * h,j * h) * (h ** 2))
    return X
def SeidelDiff(x, y):
    result = 0
    length = len(x)
    for i in range(length):
        for j in range(len(x[i])):
            result = max(abs(x[i][j] - y[i][j]), result)
    return result
def draw(a, b, c, d, h, u, method):
    x = np.arange(a, b, h)
    t = np.arange(c, d, h)
    x, t = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, t, u, cmap=cm.plasma)
    ax.set_title(method.title())
    plt.show()
def getMethod(a, b, c, d, h, method):
    count_x = int((b - a) / h)
    count_t = int((d - c) / h)
    u = np.zeros((count_t, count_x))
    for i in range(count_t):
        u[i][0] = i * h + a
        u[i][count_x - 1] = i * h + b
    for i in range(count_x):
        u[0][i] = i * h + c
        u[count_t - 1][i] = i * h + d
    for j in range(1, count_x - 1):
        for i in range(1, count_t - 1):
            u[i][j] = 0
    prev = next = u
    while True:
        prev = next
        if method.title() == 'Seidel Method':
            next = SeidelMethod(prev, count_x, h)
            if SeidelDiff(prev, next) * h < eps:
                break
        else:
            next = SimpleIterationMethod(prev, count_x, h)
            if SimpleDiff(prev, next) * h < eps:
                break
    return next

n1_10 = getMethod(a=0, b=10, c=0, d=10, h=1, method='Зейделя')
n1_5 = getMethod(a=0, b=5, c=0, d=5, h=1, method='Зейделя')
n2_10 = getMethod(a=0, b=10, c=0, d=10, h=1, method='Метод простых итераций')
n2_5 = getMethod(a=0, b=5, c=0, d=5, h=1, method='Метод простых итерация')
draw(a=0, b=10, c=0, d=10, h=1, u=n1_10, method='Метод Зейделя , 10 x 10')
draw(a=0, b=5, c=0, d=5, h=1, u=n1_5, method='Метод Зейделя , 5 x 5')
draw(a=0, b=10, c=0, d=10, h=1, u=n2_10, method='Метод простых итераций, 10 x 10')
draw(a=0, b=5, c=0, d=5, h=1, u=n2_5, method='Метод простых итераций, 5 x 5')