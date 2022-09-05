
import numpy as np


# Power Unsigned
def pow_u(x, p):
    if p < 0 or int(p) != p:
        return "Error: Solo exponentes enteros positivos"
    return np.power(x, p)


# Funcion que retorna el factorial, solo acepta numeros naturales
def fact_t(x):
    if x < 0 or int(x) != x:
        return "Error: Solo numeros naturales"

    result = np.double(1)

    for i in range(1, x + 1):
        result = np.multiply(result, i)

    return result


# Retorna el valor de 1/a
def div_t(t):
    if t <= 0:
        return "Error: Solo numeros positivos"

    eps = 2.2204e-16
    x = np.double(t)
    x1 = np.double(0)

    if x > 0 and x <= fact_t(20):
        x1 = np.double(pow_u(eps, 2))
    elif x > fact_t(20) and x <= fact_t(40):
        x1 = np.double(pow_u(eps, 4))
    elif x > fact_t(40) and x <= fact_t(60):
        x1 = np.double(pow_u(eps, 8))
    elif x > fact_t(60) and x <= fact_t(80):
        x1 = np.double(pow_u(eps, 11))
    elif x > fact_t(80) and x < fact_t(100):
        x1 = np.double(pow_u(eps, 15))
    else:
        return 0

    for i in range(2500):

        x0 = x1
        x1 = np.multiply(x0, np.subtract(2, np.multiply(x, x0)))

        error = np.abs(np.subtract(x1, x0))
        if error < np.multiply(10**-8, np.abs(x1)):
            break

    return x1
