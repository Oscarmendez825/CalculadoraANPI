import div_fact as div
import array as arr


def power(base, exponente):
    result = 1.0
    while exponente != 0:
        result *= base
        exponente -= 1
    return result


def power_t(x, y):
    result = 1.0
    exponenteI = y
    exponenteIterativo = abs(y)
    base = x
    if (exponenteI > 0 and isinstance(exponenteI, int)):
        result = power(x, y)
    elif (exponenteI < 0 and isinstance(exponenteI, int)):
        potencia = power(x, exponenteIterativo)
        result = div.div_t(potencia)
    elif isinstance(exponenteI, float) and exponenteI > 0:
        result = base ** exponenteI
    elif isinstance(exponenteI, float) and exponenteI < 0:
        result = base ** abs(exponenteI)
        result = div.div_t(result)
    return result


def sqrt_t(x):
    result = 0.0
    a = arr.array('f', [])
    if (x >= 0):
        xk = x * div.div_t(2)
        xk1 = xk - (power_t(xk, 2) - x) * div.div_t(2 * power_t(xk, 2 - 1))
        a.append(xk)
        for i in range(0, 2500):
            xk1 = a[i] - (power_t(a[i], 2) - x) * div.div_t(2 * power_t(a[i], 2 - 1))
            a.append(xk1)
            result = a[i]
            if abs(a[i + 1] - a[i]) < power_t(10, -8) * abs(a[i + 1]):
                break
        return result
    else:
        return "Solo se permiten numeros positivos"


def root_t(x, y):
    result = 0.0
    a = arr.array('f', [])
    xk = x * div.div_t(2)

    if (isinstance(y, int) and x >= 0):
        xk1 = xk - (power_t(xk, y) - x) * div.div_t(y * power_t(xk, y - 1))
        a.append(xk)
        for i in range(0, 2500):
            xk1 = a[i] - (power_t(a[i], y) - x) * div.div_t(y * power_t(a[i], y - 1))
            a.append(xk1)
            result = a[i]
            if abs(a[i + 1] - a[i]) < power_t(10, -8) * abs(a[i + 1]):
                break
    elif (isinstance(y, float)):
        result = power_t(x, 1 / y)
    elif (isinstance(y, int) and y % 2 != 0 and x <= 0):
        xk1 = xk - (power_t(xk, y) - x) * div.div_t(y * power_t(xk, y - 1))
        a.append(xk)
        for i in range(0, 2500):
            xk1 = a[i] - (power_t(a[i], y) - x) * div.div_t(y * power_t(a[i], y - 1))
            a.append(xk1)
            result = a[i]
            if abs(a[i + 1] - a[i]) < power_t(10, -8) * abs(a[i + 1]):
                break
    elif (isinstance(y, int) and y % 2 == 0 and x <= 0):
        return "No es posible brindar una solucion real"
    return result


def sinh(a):
    arra = arr.array('f', [])
    result = power_t(a, 1)
    result_aux = result
    arra.append(result)
    for n in range(1, 2500):
        i = 2 * n + 1
        fact = div.fact_t(i)
        valor = power_t(a, i) * div.div_t(fact)
        result_aux = result_aux + valor
        arra.append(result_aux)
        result = result_aux
        if abs(arra[n] - arra[n - 1]) < power_t(10, -8):
            break
    return result


def cosh(a):
    arra = arr.array('f', [])
    result = 1
    result_aux = result
    arra.append(result)
    for n in range(1, 2500):
        i = 2 * n
        fact = div.fact_t(i)
        valor = power_t(a, i) * div.div_t(fact)
        result_aux = result_aux + valor
        arra.append(result_aux)
        result = result_aux
        if abs(arra[n] - arra[n - 1]) < power_t(10, -8):
            break
    return result


def tanh(a):
    result = sinh(a) * div.div_t(cosh(a))
    return result

# print(power(14,9))
#
# print(root_t(2,1/3))
#
# print(sqrt_t(0.2))
#
# print(sinh(0))
#
# print(cosh(0))
#
# print(tanh(2))
