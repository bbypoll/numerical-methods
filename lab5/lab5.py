import numpy as np
def f1(x,y):
    return np.cos(1.5 + x) + 0.1 * y**2

def f2(x,y):
    return np.cos(1.5*x + y) + (x -y)

eps = 10**(-3)
a = 0
b = 0.5
y_0 = 0

def error(new_y, old_y):
    max = -1
    for i in range(0,len(old_y)):
        if (abs(new_y[i*2]-old_y[i])>max):
            max=abs(new_y[i*2]-old_y[i])

    if (max<eps):
        return False

    return True

def euler_cauchy(a,b):
    print('Метод Эйлера-Коши: ')
    n = 4
    h = (b - a) / n
    old_y = np.zeros(n+1)
    old_x = [a+i*h for i in range(n+1)]
    for i in range(n):
       old_y[i+1]= old_y[i]+h*f1(old_x[i]+h/2,old_y[i]+h/2*f1(old_x[i],old_y[i]))

    while True:
        n *= 2
        h /= 2
        new_y = np.zeros(n+1)
        new_x = [a+i*h for i in range(n+1)]

        for i in range(n):
            new_y[i+1] = new_y[i]+h*f1(new_x[i]+h/2,new_y[i]+h/2*f1(new_x[i],new_y[i]))

        if (not error(new_y, old_y)):
            break

        old_y = new_y
        old_x = new_x

    print('Количество точек: ', n+1,'\n')
    for i in range(len(new_x)):
        print('x = ',new_x[i],'y = ',new_y[i])

print(euler_cauchy(a,b))

def k1(x, y, h):
    return h * f1(x,y)
def k2(x, y, h):
    return h * f1(x+h/2, y + k1(x,y,h)/2)
def k3(x, y ,h):
    return h * f1(x+h/2, y + k2(x, y, h)/2 )
def k4(x, y ,h):
    return h * f1(x + h, y + k3(x, y, h))

def runge_kutt(a,b):
    print('Метод Рунге-Кутта: ')
    n = 4
    h = (b - a) / n
    old_y = np.zeros(n+1)
    old_x = [a+i*h for i in range(n+1)]
    for i in range(n):
        old_y[i+1] = old_y[i]+ 1/6 * \
                     (k1(old_x[i],old_y[i],h)+2*k2(old_x[i],old_y[i],h) +
                      2*k3(old_x[i],old_y[i],h)+k4(old_x[i],old_y[i],h))

    while True:
        n *= 2
        h /= 2
        new_y = np.zeros(n+1)
        new_x = [a+i*h for i in range(n+1)]
        for i in range(n):
            new_y[i+1] = new_y[i] + 1/6 * \
                     (k1(new_x[i], new_y[i],h)+2*k2(new_x[i], new_y[i],h) +
                      2*k3(new_x[i], new_y[i],h)+k4(new_x[i], new_y[i],h))

        if (not error(new_y, old_y)):
            break

        old_y = new_y
        old_x = new_x
    print('Количество точек: ', n + 1, '\n')
    for i in range(len(new_x)):
        print('x = ', new_x[i], 'y = ', new_y[i])

print(runge_kutt(a,b))

def adams_3(a, b):
    print('Метод Адамса 3-го порядка: ')
    n = 10
    h = (b - a) / n
    old_g = [1 for i in range(n+1)]
    old_y = np.zeros(n+1)
    old_x = [a+i*h for i in range(n+1)]
    for i in range(n):
        if i < 3:
            old_g[i+1] = old_g[i]+h*f2(old_x[i], old_y[i])
            old_y[i+1] = old_y[i]+h*old_g[i]
        else:
            old_g[i+1] = old_g[i]+h*(23*f2(old_x[i], old_y[i])-16*f2(old_x[i-1], old_y[i-1]) +
                                     5*f2(old_x[i-2], old_y[i-2]))/12
            old_y[i+1] = old_y[i]+h*(23*old_g[i]-16*old_g[i-1]+5*old_g[i-2])/12

    while True:
        n *= 2
        h /= 2
        g = [1 if i == 0 else 0 for i in range(n+1)]
        new_y = np.zeros(n+1)
        new_x = [a+h*i for i in range(n+1)]

        for i in range(n):
            if i < 3:
                g[i+1] = g[i]+h*f2(new_x[i], new_y[i])
                new_y[i+1] = new_y[i]+h*g[i]
            else:
                g[i+1] = g[i]+h*(23*f2(new_x[i], new_y[i])-16*f2(new_x[i-1], new_y[i-1])
                                 + 5*f2(new_x[i-2], new_y[i-2]))/12
                new_y[i+1] = new_y[i]+h*(23*g[i]-16*g[i-1]+5*g[i-2])/12

        if (not error(new_y,old_y)):
            break

        old_y = new_y
        old_x = new_x
    print('Количество точек: ', n + 1, '\n')
    for i in range(len(new_x)):
        print('x = ', new_x[i], 'y = ', new_y[i])

print(adams_3(a,b))

def adams_4(a, b):
    print('Метод Адамса 4-го порядка: ')
    n = 10
    h = (b - a) / n
    old_g = [1 for i in range(n+1)]
    old_y = np.zeros(n+1)
    old_x = [a+i*h for i in range(n+1)]
    for i in range(n):
        if i < 4:
            old_g[i+1] = old_g[i]+h*f2(old_x[i], old_y[i])
            old_y[i+1] = old_y[i]+h*old_g[i]
        else:
            old_g[i+1] = old_g[i]+h*(55*f2(old_x[i], old_y[i])-59*f2(old_x[i-1], old_y[i-1]) +
                                     37*f2(old_x[i-2], old_y[i-2])-9*f2(old_x[i-3], old_y[i-3]))/24
            old_y[i+1] = old_y[i]+h*(55*old_g[i]-59*old_g[i-1]+37*old_g[i-2]-9*old_g[i-3])/24

    while True:
        n *= 2
        h /= 2
        g = [1 if i == 0 else 0 for i in range(n+1)]
        new_y = np.zeros(n+1)
        new_x = [a+h*i for i in range(n+1)]

        for i in range(n):
            if i < 4:
                g[i+1] = g[i]+h*f2(new_x[i], new_y[i])
                new_y[i+1] = new_y[i]+h*g[i]
            else:
                g[i+1] = g[i]+h*(55*f2(new_x[i], new_y[i])-59*f2(new_x[i-1], new_y[i-1]) +
                                 37*f2(new_x[i-2], new_y[i-2])-9*f2(new_x[i-3], new_y[i-3]))/24
                new_y[i+1] = new_y[i]+h*(55*g[i]-59*g[i-1]+37*g[i-2]-9*g[i-3])/24

        if (not error(new_y,old_y)):
            break

        old_y = new_y
        old_x = new_x
    print('Количество точек: ', n + 1, '\n')
    for i in range(len(new_x)):
        print('x = ', new_x[i], 'y = ', new_y[i])

print(adams_4(a,b))