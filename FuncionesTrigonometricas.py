import funtras as div


# seno de x
def sin_t(x):
    sk = 0.0
    for i in range(0, 2500):
        numerador = div.pow_u(-1, i) * div.pow_u(x, (2 * i) + 1)
        denominador = div.fact_t((2 * i) + 1)
        division = div.div_t(denominador)
        sk += numerador * division
        numerador1 = div.pow_u(-1, i + 1) * div.pow_u(x, (2 * (i + 1)) + 1)
        denominador1 = div.fact_t((2 * (i + 1)) + 1)
        division1 = div.div_t(denominador1)
        sk1 = sk + (numerador1 * division1)
        if abs(sk1 - sk) < trigh.power_t(10, -8):
            break
    return sk


# coseno de x
def cos_t(x):
    sk = 0.0
    for i in range(0, 2500):
        numerador = div.pow_u(-1, i) * div.pow_u(x, 2 * i)
        denominador = div.fact_t(2 * i)
        division = div.div_t(denominador)
        sk += numerador * division
        numerador1 = div.pow_u(-1, i + 1) * div.pow_u(x, 2 * (i + 1))
        denominador1 = div.fact_t(2 * (i + 1))
        division1 = div.div_t(denominador1)
        sk1 = sk + (numerador1 * division1)

        if abs(sk1 - sk) < trigh.power_t(10, -8):
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
            division = -div.div_t(-denominador)
        else:
            division = div.div_t(denominador)
        return numerador * division


# secante de x
def sec_t(x):
    coseno = cos_t(x)
    if coseno == 0:
        return "Error: No se permiten valores multiplos de pi/2"
    else:
        if coseno > 0:
            return div.div_t(coseno)
        else:
            return -div.div_t(-coseno)


# cosecante de x
def csc_t(x):
    seno = sin_t(x)
    if seno == 0:
        return "Error: No se permiten valores multiplos de pi o cero"
    else:
        if seno > 0:
            return div.div_t(seno)
        else:
            return -div.div_t(-seno)


# cotangente de x
def cot_t(x):
    tangente = tan_t(x)
    if tangente == 0:
        return "Error: No se permiten valores multiplos de pi o cero"
    else:
        if tangente > 0:
            return div.div_t(tangente)
        else:
            return -div.div_t(-tangente)
