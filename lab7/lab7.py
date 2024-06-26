import numpy as np
import matplotlib.pyplot as plt

def Ux0(x):
    if (x >= 0.5):
        return 0
    else:
        return 3
h = 0.1
T = 0.001
a = 1
d = 1
eps=0.01
p = int(a / h) + 1
q = int(d / T) + 1
U = [0] * p
for i in range(p):
    U[i] = [0] * q
for i in range(0, p):
    x = h * i
    U[i][0] = Ux0(x)
for j in range(0, q - 1):
    for i in range(1, p-1):
        x = h * i
        t = T * j
        U[i][j + 1] = (U[i][j] - T/h * U[i][j] * (U[i][j] - U[i - 1][j]) - eps ** 2 * T /
                       (2 * h ** 3) * (U[i + 1][j] - U[i - 1][j]) * (U[i + 1][j] - 2 * U[i][j] + U[i - 1][j]))
        U[p - 1][j + 1] = U[i][j] - T / h * U[i][j] * (U[i][j] - U[i - 1][j])
u, v = np.mgrid[0:p, 0:q]
x = h * u
y = T * v
z = x - x
for j in range(0, q):
    for i in range(0, p):
        z[i][j] = U[i][j]
fig = plt.figure(figsize=plt.figaspect(0.5))
axes = fig.add_subplot(1, 2, 1, projection='3d')
axes.set_xlabel("x")
axes.set_ylabel("t")
axes.set_zlabel("U(x,t)")
axes.plot_surface(x, y, z, rstride=1, cstride=15, cmap='magma')
plt.show()


def Ux0_2(x):
    if (x >= 0.5):
        return 0
    else:
        return 3
h = 0.1
T = 0.001
a = 1
d = 2
p = int(a / h) + 1
q = int(d / T) + 1
U = [0] * p
for i in range(p):
    U[i] = [0] * q
for i in range(0, p):
    x = h * i
    U[i][0] = Ux0_2(x)
for j in range(0, q - 1):
    for i in range(1, p):
        x = h * i
        t = T * j
        U[i][j + 1] = U[i][j] - T / (2 * h) * (U[i][j] ** 2 - U[i - 1][j] ** 2)
u, v = np.mgrid[0:p, 0:q]
x = h * u
y = T * v
z = x - x
for j in range(0, q):
    for i in range(0, p):
        z[i][j] = U[i][j]
fig = plt.figure(figsize=plt.figaspect(0.5))
axes = fig.add_subplot(1, 2, 1, projection='3d')
axes.set_xlabel("x")
axes.set_ylabel("t")
axes.set_zlabel("U(x,t)")
axes.plot_surface(x, y, z, rstride=1, cstride=15, cmap='magma')
plt.show()



