import funtras as f


def test():
    """
    Funcion que realiza el test de la operacion que se solicitaba en la descripcion de la tarea
    :return: resultado de la operacion
    """
    a = f.root_t(f.sin_t(3*f.div_t(7) + f.ln_t(2)), 3)
    b = f.sinh(f.sqrt_t(2))
    c = f.atan_t(f.exp_t(-1))

    return a*f.div_t(b) + c


print(test())
