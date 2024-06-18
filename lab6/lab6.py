import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def f(x, t):
    return x
def f0(x,t):
    return 0
def Ux(x):
    return x**2
def Ut0(t):
    return t**2

def Ut1(t):
    return t**2+1

tau = 0.05
h = 0.1
x_bounds = (0, 1)
t_bounds = (0, 10)
I = int((x_bounds[1] - x_bounds[0]) / h)
J = int((t_bounds[1] - t_bounds[0]) / tau)

def init_rectangle(U, I, J, fx, ft, h, tau, a):
    i = np.arange(I + 1)
    x = h * i
    U[:, 0] = fx(x)
    j = np.arange(J + 1)
    t = tau * j
    start_x = 0 if a > 0 else I
    U[start_x, 1:] = ft(t[1:])
    return x, t, U
def init_half_plane(U, I, J, fx, ft, h, tau, a):
    i = np.arange(I + 1)
    x = h * (i - (J if a > 0 else 0))
    U[:, 0] = fx(x)
    j = np.arange(J + 1)
    t = tau * j
    return x, t, U

def init(I, J, h, tau, fx, ft, is_rect, a):
    if not is_rect:
        I = I + J
    U = np.zeros((I + 1, J + 1))
    if is_rect:
        return init_rectangle(U, I, J, fx, ft, h, tau, a)
    else:
        return init_half_plane(U, I, J, fx, ft, h, tau, a)

def scheme1(I, J, tau, U, fx, x, t, a, h):
    lam = a * tau / h
    for i in range(1, I):
        for j in range(0, J):
            U[i][j + 1] = lam * U[i - 1][j] + (1 - lam) * U[i][j] + tau *fx(x[i], t[j])
    return U

def scheme2(I, J, tau, U, fx, x, t, a, h):
    lam = a * tau / h
    for i in range(I - 2, -1, -1):
        for j in range(0, J):
            U[i][j + 1] = -lam * U[i + 1][j] + (1 + lam) * U[i][j] + tau *fx(x[i], t[j])
    return U

def scheme3(I, J, tau, U, fx, x, t, a):
    if a > 0:
        for i in range(1, I + 1):
            for j in range(0, J):
                U[i][j + 1] = (U[i][j] + U[i - 1][j + 1] + tau * fx(x[i], t[j]))/2
    else:
        for i in range(I - 1, -1, -1):
            for j in range(0, J):
                U[i][j + 1] = (U[i][j] + U[i + 1][j + 1] - tau * fx(x[i], t[j]))/2
    return U

def scheme4(I, J, tau, U, fx, x, t, a, h):
    if a > 0:
        for i in range(1, I + 1):
            for j in range(0, J):
                U[i][j + 1] = U[i - 1][j] + tau * fx(x[i] + h / 2, t[j] + tau /2)
    else:
        for i in range(I - 1, -1, -1):
            for j in range(0, J):
                U[i][j + 1] = U[i + 1][j] - tau * fx(x[i] + h / 2, t[j] + tau /2)
    return U
def draw(x, t, U):
    x, t = np.meshgrid(x, t)
    x, t = x.T, t.T
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("U")
    ax.plot_surface(x, t, U, cmap=cm.get_cmap("plasma"))
    plt.show()

a=2
is_rect=False
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme1(I + J + 1, J, tau, U, f0, x, t, a, h)
draw(x[x>=0],t,U[-11:,:])

a=-2
is_rect=False
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme2(I + J + 1, J, tau, U, f0, x, t, a, h)
draw(x[x<=1],t,U[:11,:])

a=2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme1(I + 1, J, tau, U, f0, x, t, a, h)
draw(x,t,U)

a=2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme3(I, J, tau, U, f0, x, t, a)
draw(x,t,U)

a=2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme4(I, J, tau, U, f0, x, t, a, h)
draw(x,t,U)

a=-2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme2(I + 1, J, tau, U, f0, x, t, a, h)
draw(x,t,U)

a=-2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme3(I, J, tau, U, f0, x, t, a)
draw(x,t,U)

a=-2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme4(I, J, tau, U, f0, x, t, a, h)
draw(x,t,U)

a=2
is_rect=False
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme1(I + J + 1, J, tau, U, f, x, t, a, h)
draw(x[x>=0],t,U[-11:,:])

a=-2
is_rect=False
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme2(I + J + 1, J, tau, U, f, x, t, a, h)
draw(x[x<=1],t,U[:11,:])

a=2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme1(I + 1, J, tau, U, f, x, t, a, h)
draw(x,t,U)

a=2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme3(I, J, tau, U, f, x, t, a)
draw(x,t,U)

a=2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme4(I, J, tau, U, f, x, t, a, h)
draw(x,t,U)

a=-2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme4(I, J, tau, U, f, x, t, a, h)
draw(x,t,U)

a=-2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme3(I, J, tau, U, f, x, t, a)
draw(x,t,U)

a=-2
is_rect=True
x,t,U=init(I,J,h,tau, Ux,Ut0, is_rect, a)
U=scheme2(I + 1, J, tau, U, f, x, t, a, h)
draw(x,t,U)


