import numpy as np


A = np.array([[2.01, 1.00, -0.24, 1.31],
              [0.45, 2.36, 0.58, 3.22],
              [0.30, -1.08, 1.00, -2.34],
              [1.12, 0.24, 2.55, -1.11]])

b = np.array([1.98, 3.69, 3.48, 10.36])
x = np.array([1, 2, 3, -1])
x0=np.zeros_like(b)


def gauss(A, b):
    n = len(A)
    # Прямой ход метода Гаусса с выбором максимального элемента
    for k in range(n - 1):
        max_idx = np.argmax(abs(A[k:, k])) + k
        if max_idx != k:
            A[[k, max_idx]] = A[[max_idx, k]]
            b[[k, max_idx]] = b[[max_idx, k]]

        for i in range(k+1, n):
            ko = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= ko * A[k][j]
            b[i] -= ko * b[k]
        print(A,'\n')

    # Обратный ход метода Гаусса
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum = b[i]
        for j in range(i + 1, n):
            sum -= A[i][j] * x[j]
        x[i] = sum / A[i][i]

    return x


def seidel(A, b, x0, max_iter, eps):
    n = len(A)
    for k in range(max_iter):
        x=x0.copy()
        for i in range(n):
            x0[i]=((b[i] - np.dot(A[i, :i], x0[:i]) - np.dot(A[i, i+1:],x[i+1:]))
                   / A[i, i])
            print(x0)
        if np.linalg.norm(x0-x) < eps:
            return x0


x1 = gauss(A, b)
error1 = np.linalg.norm(x - x1)
print('Метод Гаусса: ', x1,'\nПогрешность метода Гаусса: ',error1)
x2 = seidel(A, b,x0,1000, 10**(-10))
error2 = np.linalg.norm(x-x2)
print('Метод Зейделя: ', x2, 'Погрешность метода Зейделя', error2)

