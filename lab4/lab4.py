import numpy as np
def f1(x):
    return np.cos(x)

def df1(x):
    return -np.sin(x)


def f2(x):
    return np.cos(x/2)

def df2(x):
    return -1/2 * np.sin(x/2)

def ddf2(x):
    return -1/4 * np.cos(x/2)


def lagrange(x, X, Y):
    n = len(X)
    result = 0
    for i in range(n):
        term = Y[i]
        for j in range(n):
            if i != j:
                term *= (x - X[j]) / (X[i] - X[j])
        result += term
    return result

def left(x):
    return (f1(x)-f1(x-h))/h

def right(x):
    return (f1(x+h)-f1(x))/h

def center(x):
    return (f1(x+h)-f1(x-h))/(2*h)

def eitken(x, X, Y, left, right):
    if (abs(left - right) == 1):
        return((Y[left] * (X[right] - x))-((X[left] - x) * Y[right])) / (X[right] - X[left])
    else:
        return (eitken(x, X, Y, left, right - 1) * (X[right] - x) -
                eitken(x, X, Y, left + 1, right) * (X[left] - x)) / (X[right]-X[left])

h=10**(-5)
x=1.15
X_array=[1, 1.1, 1.2, 1.3]
Y_array=[0.5403, 0.4536, 0.36236, 0.2675]

print('Часть 1\nПункт 1')
print("Интерполяционный многочлен Лагранжа L(x) = ", lagrange(x, X_array, Y_array))
print("Аналитическое значение f(x) = ", f1(x))
print("Оценка погрешности решения = ", abs(lagrange(x, X_array, Y_array)-f1(x)),'\n')
print("Производная слева = ", left(x))
print("Производная справа = ", right(x))
print("Центральная производная = ", center(x))
print('Точное значение производной = ', df1(x),'\n')
print("Погрешность производной слева", abs(df1(x)-left(x)))
print("Погрешность производной справа", abs(df1(x)-right(x)))
print("Погрешность центральной производной", abs(df1(x)-center(x)))

print("Пункт 2")
x2=1.018
X_2=[1, 1.08, 1.2, 1.27, 1.31, 1.38]
Y_2=[1.1752, 1.30254, 1.50946, 1.2173, 1.22361, 1.2347]
print("Значение в точке x* с помощью схемы Эйткена",eitken(x2, X_2, Y_2, 0, len(X_2)-1), '\n')


def left2(x):
    return (f2(x)-f2(x-h))/h

def right2(x):
    return (f2(x+h)-f2(x))/h

def center2(x):
    return (f2(x+h)-f2(x-h))/(2*h)

def second(x):
    return (f2(x-h) - 2*f2(x) + f2(x+h)) / h**2

a=2
b=2.5
m=2.06
n=5
l=(b-a)/(n-1)
X_3=[]
for i in range(n):
    X_3.append(a + i * l)
X_3.append(m)

for i in range(len(X_3)):
    print("Для x = ", X_3[i])
    if (i != 0):
        print("Производная слева =",left2(X_3[i]))
        print("Погрешность производной слева = ", abs(df2(X_3[i])-left2(X_3[i])))
    else:
        print("Производная слева = - ")
        print("Погрешность производной слева = - ")

    if (i != len(X_3)-2):
        print("Производная справа = ",right2(X_3[i]))
        print("Погрешность производной справа = ", abs(df2(X_3[i]) - right2(X_3[i])))
    else:
        print("Производная справа = - ")
        print("Погрешность производной справа = - ")


    if (i != 0):
        print("Центральная производная  = ",center2(X_3[i]))
        print("Погрешность центральной производной = ", abs(df2(X_3[i]) - center2(X_3[i])))
    else:
        print("Центральная производная  = - ")
        print("Погрешность центральной производной = -")


    if (i != 0 and i != len(X_3)-2):
        print("Вторая численная производная = ", second(X_3[i]))
        print("Погрешность второй численной производной = ", abs(ddf2(X_3[i]) - second(X_3[i])))
    else:
        print("Вторая численная производная = - ")
        print("Погрешность второй численной производной = -")

    print("Первая точная поизводная = ", df2(X_3[i]))
    print("Вторая точная поизводная = ", ddf2(X_3[i]),'\n')

Y_3=[]
for i in range(len(X_3)):
    Y_3.append(f2(X_3[i]))
print("Интерполированное значение = ", lagrange(m, X_3, Y_3))
print("Аналитическое значение f(m) = ", f2(m))