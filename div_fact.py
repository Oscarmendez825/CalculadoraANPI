
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
    if y <= 1 or int(x) != x:
        return "Error: La base debe ser entero positivo mayor a 1"

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
    return 0


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
