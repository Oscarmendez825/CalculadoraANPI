import array as arr


# Power Unsigned
def pow_u(x, p):
    if p < 0 or int(p) != p:
        return "Error: Solo exponentes enteros positivos"
    return pow(x, p)


# Funcion que retorna el factorial, solo acepta numeros naturales
def fact_t(x):
    if x < 0 or int(x) != x:
        return "Error: Solo numeros naturales"

    result = 1

    for i in range(1, int(x) + 1):
        result = result * i

    return result


# Retorna el valor de 1/a, con a positivo diferente de 0
def div_t(x):
    if x <= 0:
        return "Error: Solo numeros positivos"

    eps = 2.2204e-16
    x1 = 0

    if x > 0 and x <= fact_t(20):
        x1 = pow_u(eps, 2)
    elif x > fact_t(20) and x <= fact_t(40):
        x1 = pow_u(eps, 4)
    elif x > fact_t(40) and x <= fact_t(60):
        x1 = pow_u(eps, 8)
    elif x > fact_t(60) and x <= fact_t(80):
        x1 = pow_u(eps, 11)
    elif x > fact_t(80) and x < fact_t(100):
        x1 = pow_u(eps, 15)
    else:
        return 0

    for i in range(2500):

        x0 = x1
        x1 = x0 * (2 - (x * x0))

        error = abs(x1 - x0)
        if error < (10**-8) * abs(x1):
            break

    return x1


# Funcion que retorna el valor de e^a
def exp_t(a):
    Sk = 0
    Sk1 = pow_u(a, 0) * div_t(fact_t(0))

    for k in range(1, 2500):

        Sk = Sk1
        Sk1 += pow_u(a, k) * div_t(fact_t(k))

        error = abs(Sk1 - Sk)
        if error < 10**-8:
            break

    return Sk1


# Funcion que retorna el valor de logaritmo natural de x
def ln_t(x):
    if x <= 0:
        return "Error: Solo numeros positivos"

    coef = 2*(x-1)*div_t(x+1)
    Sk = 0
    Sk1 = coef

    for k in range(1, 2500):

        Sk = Sk1
        Sk1 += coef * (1*div_t(2*k+1)) * pow_u((x-1)*div_t(x+1), 2*k)

        error = abs(Sk1 - Sk)
        if error < 10**-8:
            break

    return Sk1


# Funcion que retorna el logaritmo en base y de x
def log_t(x, y):
    if x <= 0:
        return "Error: El arguento debe ser un numero positivo"
    if y == 1 or y <= 0:
        return "Error: La base debe ser positiva diferente de 1"

    return ln_t(x) * div_t(ln_t(y))


# Funcion que retorna el seno inverso de a
def asin_t(a):
    if a > 1 or a < -1:
        return "Error: Los valores deben estar entre -1 y 1"
    Sk = 0
    Sk1 = a

    for k in range(1, 2500):

        Sk = Sk1
        denm = div_t(pow_u(4, k) * pow_u(fact_t(k), 2) * (2*k+1))
        Sk1 += fact_t(2*k) * pow_u(a, 2*k+1) * denm

        error = abs(Sk1 - Sk)
        if error < 10**-8:
            break

    return Sk1


# Funcion que retorna el coseno inverso de a
def acos_t(a):
    if a > 1 or a < -1:
        return "Error: Los valores deben estar entre -1 y 1"

    pi = 3.141592653589793

    return pi*div_t(2) - asin_t(a)


# Funcion que retorna la tangente inversa de a
def atan_t(a):
    Sk = 0
    Sk1 = 0
    pi = 3.141592653589793

    if a > 1:
        Sk1 += pi*div_t(2) - div_t(a)
    elif a < -1:
        Sk1 += -pi*div_t(2) + div_t(-a)
    else:
        Sk1 = a

    for k in range(1, 2500):

        comun = pow_u(-1, k) * div_t(2*k+1)
        Sk = Sk1

        if a > 1:
            Sk1 += comun * div_t(pow_u(a, 2*k+1))
        elif a < -1:
            Sk1 += comun * (-div_t(pow_u(-a, 2*k+1)))
        else:
            Sk1 += comun * pow_u(a, 2*k+1)

        error = abs(Sk1 - Sk)
        if error < 10**-8:
            break

    return Sk1


# seno de x
def sin_t(x):
    sk = 0.0
    for i in range(0, 2500):
        numerador = pow_u(-1, i) * pow_u(x, (2 * i) + 1)
        denominador = fact_t((2 * i) + 1)
        division = div_t(denominador)
        sk += numerador * division
        numerador1 = pow_u(-1, i + 1) * pow_u(x, (2 * (i + 1)) + 1)
        denominador1 = fact_t((2 * (i + 1)) + 1)
        division1 = div_t(denominador1)
        sk1 = sk + (numerador1 * division1)
        if abs(sk1 - sk) < 10 ** (-18):
            break
    return sk


# coseno de x
def cos_t(x):
    sk = 0.0
    for i in range(0, 2500):
        numerador = pow_u(-1, i) * pow_u(x, 2 * i)
        denominador = fact_t(2 * i)
        division = div_t(denominador)
        sk += numerador * division
        numerador1 = pow_u(-1, i + 1) * pow_u(x, 2 * (i + 1))
        denominador1 = fact_t(2 * (i + 1))
        division1 = div_t(denominador1)
        sk1 = sk + (numerador1 * division1)

        if abs(sk1 - sk) < 10 ** (-18):
            break
    return sk


# tangente de x
def tan_t(x):
    numerador = sin_t(x)
    denominador = cos_t(x)
    if denominador == 0:
        return "Error: No se permiten valores multiplos de pi/2"
    else:
        if denominador < 0:
            division = -div_t(-denominador)
        else:
            division = div_t(denominador)
        return numerador * division


# secante de x
def sec_t(x):
    coseno = cos_t(x)
    if coseno == 0:
        return "Error: No se permiten valores multiplos de pi/2"
    else:
        if coseno > 0:
            return div_t(coseno)
        else:
            return -div_t(-coseno)


# cosecante de x
def csc_t(x):
    seno = sin_t(x)
    if seno == 0:
        return "Error: No se permiten valores multiplos de pi o cero"
    else:
        if seno > 0:
            return div_t(seno)
        else:
            return -div_t(-seno)


# cotangente de x
def cot_t(x):
    tangente = tan_t(x)
    if tangente == 0:
        return "Error: No se permiten valores multiplos de pi o cero"
    else:
        if tangente > 0:
            return div_t(tangente)
        else:
            return -div_t(-tangente)


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
    if(exponenteI > 0 and isinstance(exponenteI, int)):
        result = power(x, y)
    elif(exponenteI < 0 and isinstance(exponenteI, int)):
        potencia = power(x, exponenteIterativo)
        result = div_t(potencia)
    elif isinstance(exponenteI, float) and exponenteI > 0:
        result = base**exponenteI
    elif isinstance(exponenteI, float) and exponenteI < 0:
        result = base ** abs(exponenteI)
        result = div_t(result)
    return result


def sqrt_t(x):
    result = 0.0
    a = arr.array('f', [])
    if(x >= 0):
        xk = x * div_t(2)
        xk1 = xk - (power_t(xk, 2) - x) * div_t(2 * power_t(xk, 2 - 1))
        a.append(xk)
        for i in range(0, 2500):
            xk1 = a[i] - (power_t(a[i], 2) - x) * \
                div_t(2 * power_t(a[i], 2 - 1))
            a.append(xk1)
            result = a[i]
            if abs(a[i + 1] - a[i]) < power_t(10, -8) * abs(a[i + 1]):
                break
        return result
    else:
        return "Error: Solo se permiten numeros positivos"


def root_t(x, y):
    result = 0.0
    a = arr.array('f', [])
    xk = x*div_t(2)

    if(isinstance(y, int) and x >= 0):
        xk1 = xk - (power_t(xk, y) - x) * div_t(y * power_t(xk, y - 1))
        a.append(xk)
        for i in range(0, 2500):
            xk1 = a[i] - (power_t(a[i], y)-x)*div_t(y*power_t(a[i], y-1))
            a.append(xk1)
            result = a[i]
            if abs(a[i+1] - a[i]) < power_t(10, -8) * abs(a[i+1]):
                break
    elif (isinstance(y, float)):
        result = power_t(x, 1/y)
    elif (isinstance(y, int) and y % 2 != 0 and x <= 0):
        xk1 = xk - (power_t(xk, y) - x) * div_t(y * power_t(xk, y - 1))
        a.append(xk)
        for i in range(0, 2500):
            xk1 = a[i] - (power_t(a[i], y) - x) * \
                div_t(y * power_t(a[i], y - 1))
            a.append(xk1)
            result = a[i]
            if abs(a[i + 1] - a[i]) < power_t(10, -8) * abs(a[i + 1]):
                break
    elif (isinstance(y, int) and y % 2 == 0 and x <= 0):
        return "Error: No es posible brindar una solucion real"
    return result


def sinh(a):
    arra = arr.array('f', [])
    result = power_t(a, 1)
    result_aux = result
    arra.append(result)
    for n in range(1, 2500):
        i = 2*n+1
        fact = fact_t(i)
        valor = power_t(a, i)*div_t(fact)
        result_aux = result_aux + valor
        arra.append(result_aux)
        result = result_aux
        if abs(arra[n] - arra[n-1]) < power_t(10, -8):
            break
    return result


def cosh(a):
    arra = arr.array('f', [])
    result = 1
    result_aux = result
    arra.append(result)
    for n in range(1, 2500):
        i = 2*n
        fact = fact_t(i)
        valor = power_t(a, i) * div_t(fact)
        result_aux = result_aux + valor
        arra.append(result_aux)
        result = result_aux
        if abs(arra[n] - arra[n - 1]) < power_t(10, -8):
            break
    return result


def tanh(a):
    result = sinh(a)*div_t(cosh(a))
    return result
