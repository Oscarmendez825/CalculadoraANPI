from cmath import sqrt
import div_fact as d
import FuncionesTrigonometricas as f
import trigonometricasHiperbolicas as h


def test():
    a = h.root_t(f.sin_t(3*d.div_t(7) + d.ln_t(2)), 3)
    b = h.sinh(h.sqrt_t(2))
    c = d.atan_t(d.exp_t(-1))

    return a*d.div_t(b) + c


print(test())
