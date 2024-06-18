import numpy as np

def f(x):
    return (np.log(x)**2)/x

a = 1
b = 5
eps = 10**(-4)
expected_res = round((np.log(5)**3)/3, 4)

def left_rectangle(a, b, eps):
    I0=0
    n=3
    while True:
        h = (b - a) / n
        I = sum(f(a + h * i) for i in range(0,n-1)) * h
        if abs(I - I0) < eps:
            print('Метод левых прямоугольников')
            print( 'Значение интеграла:', I, '\nПоследний шаг: ', h, '\nЧисло точек разбиения: ', n)
            print('Относительная погрешность: ', round(abs((expected_res - I)/expected_res)*100, 5),'%')
            return I
        I0 = I
        n = n * 2

left_rectangle(a, b, eps)
print("\n")

def right_rectangle(a, b, eps):
    I0=0
    n=3
    while True:
        h = (b - a) / n
        I = sum(f(a + h * i) for i in range(1,n)) * h
        if abs(I - I0) < eps:
            print('Метод правых прямоугольников')
            print( 'Значение интеграла:', I, '\nПоследний шаг: ', h, '\nЧисло точек разбиения: ', n)
            print('Относительная погрешность: ', round(abs((expected_res - I)/expected_res)*100, 5),'%')
            return I
        I0 = I
        n = n * 2

right_rectangle(a, b, eps)
print('\n')

def middle_rectangle(a, b, eps):
    I0=0
    n=3
    while True:
        h = (b - a) / n
        I = sum(f(a + h * (i - 1) + h/2) for i in range(1,n)) * h
        if abs(I - I0) < eps:
            print('Метод средних прямоугольников')
            print( 'Значение интеграла:', I, '\nПоследний шаг: ', h, '\nЧисло точек разбиения: ', n)
            print('Относительная погрешность: ', round(abs((expected_res - I)/expected_res)*100, 5),'%')
            return I
        I0 = I
        n = n * 2

middle_rectangle(a, b, eps)
print('\n')

def trapezoid(a, b, eps):
    I0=0
    n=3
    while True:
        h = (b - a) / n
        I = ((f(a) + f(b)) / 2 + sum(f(a + h*i) for i in range(1,n-1))) * h
        if abs(I - I0) < eps:
            print('Метод трапеций')
            print( 'Значение интеграла:', I, '\nПоследний шаг: ', h, '\nЧисло точек разбиения: ', n)
            print('Относительная погрешность: ', round(abs((expected_res - I)/expected_res)*100, 5),'%')
            return I
        I0 = I
        n = n * 2

trapezoid(a, b , eps)
print('\n')

def simpson(a, b, eps):
    I0=0
    n=3
    while True:
        h = (b - a) / n
        sum1 = 0
        sum2 = 0
        for i in range(1,n-1):
            if(i%2==0):
                sum1 += f(a + i*h)

        for i in range(1,n):
            if(i%2!=0):
                sum2 += f(a+ i*h)

        I = (f(a) + 2 * sum1 + 4 * sum2 + f(b)) * h/3
        if abs(I - I0) < eps:
            print('Метод Симпсона')
            print( 'Значение интеграла:', I, '\nПоследний шаг: ', h, '\nЧисло точек разбиения: ', n)
            print('Относительная погрешность: ', round(abs((expected_res - I)/expected_res)*100, 5),'%')
            return I
        I0 = I
        n = n * 2

simpson(a, b, eps)
print('\n')