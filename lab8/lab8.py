import numpy as np
import matplotlib.pyplot as plt
def Ux0(x):
   return x
def Ux1(x):
   return -2
def U0t(t):
   return 0
def Ult(t):
   return 1

h = 0.1
r = 0.01
a = 1
p = int(1 / h) + 1
q = int(10 / r) + 1
l = pow(a * r / h, 2)
U = [0] * p
for i in range(p):
   U[i] = [0] * q
for i in range(0, p):
   x = h * i
   U[i][0] = Ux0(x)
   U[i][1] = U[i][0] + r * Ux1(x)
for j in range(1, q):
   t = r * j
   U[0][j] = U0t(t)
   U[p - 1][j] = Ult(t)
for j in range(1, q - 1):
   for i in range(1, p - 1):
       x = h * i
       t = r * j
       U[i][j + 1] = 2 * (1 - l) * U[i][j] + l * (U[i + 1][j] + U[i - 1][j]) - U[i][j - 1]
u, v = np.mgrid[0:p, 0:q]
x = h * u
y = r * v
z = x - x
for i in range(0, p):
   for j in range(0, q):
       z[i][j] = U[i][j]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=15, cmap='magma')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('U(x,t)')
plt.show()
U = [0] * p
for i in range(p):
   U[i] = [0] * q
for i in range(0, p):
   x = h * i
   U[i][0] = Ux0(x)
   U[i][1] = U[i][0] + r * Ux1(x)
for j in range(1, q):
   t = r * j
   U[0][j] = U0t(t)
   U[p - 1][j] = Ult(t)
for j in range(1, q - 1):
   mb = [0] * p
   for i in range(1, p - 2):
       mb[i] = -l
   mc = [0] * p
   for i in range(1, p - 1):
       mc[i] = 1 + 2 * l
   ma = [0] * p
   for i in range(2, p - 1):
       ma[i] = -l
   mf = [0] * p
   mf[1] = 2 * U[1][j] - U[1][j - 1] + l * U[0][j]
   for i in range(2, p - 2):
       mf[i] = 2 * U[i][j] - U[i][j - 1]
   mf[p - 2] = 2 * U[p - 2][j] - U[p - 2][j - 1] + l * U[p - 1][j]
   for i in range(2, p - 1):
       m = ma[i] / mc[i - 1]
       mc[i] = mc[i] - m * mb[i - 1]
       mf[i] = mf[i] - m * mf[i - 1]
   U[p - 2][j + 1] = mf[p - 2] / mc[p - 2]
   for i in range(p - 3, 0, -1):
       U[i][j + 1] = (mf[i] - mb[i] * U[i + 1][j + 1]) / mc[i]
u, v = np.mgrid[0:p, 0:q]
x = h * u
y = r * v
z = x - x
for i in range(0, p):
   for j in range(0, q):
       z[i][j] = U[i][j]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=15, cmap='magma')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('U(x,t)')
plt.show()
U = [0] * p
for i in range(p):
   U[i] = [0] * q
for i in range(0, p):
   x = h * i
   U[i][0] = Ux0(x)
   U[i][1] = U[i][0] + r * Ux1(x)
for j in range(1, q):
   t = r * j
   U[0][j] = U0t(t)
   U[p - 1][j] = Ult(t)
for j in range(1, q - 1):
   mb = [0] * p
   for i in range(1, p - 2):
       mb[i] = -l
   mc = [0] * p
   for i in range(1, p - 1):
       mc[i] = 1 + 2 * l
   ma = [0] * p
   for i in range(2, p - 1):
       ma[i] = -l
   mf = [0] * p
   mf[1] = 2 * U[1][j] - U[1][j - 1] + l * U[0][j]
   for i in range(2, p - 2):
       mf[i] = 2 * U[i][j] - U[i][j - 1]
   mf[p - 2] = 2 * U[p - 2][j] - U[p - 2][j - 1] + l * U[p - 1][j]
   for i in range(2, p - 1):
       m = ma[i] / mc[i - 1]
       mc[i] = mc[i] - m * mb[i - 1]
       mf[i] = mf[i] - m * mf[i - 1]
   U[p - 2][j + 1] = mf[p - 2] / mc[p - 2]
   for i in range(p - 3, 0, -1):
       U[i][j + 1] = (mf[i] - mb[i] * U[i + 1][j + 1]) / mc[i]
u, v = np.mgrid[0:p, 0:q]
x = h * u
y = r * v
z = x - x
for i in range(0, p):
   for j in range(0, q):
       z[i][j] = U[i][j]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=15, cmap='magma')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('U(x,t)')
plt.show()






