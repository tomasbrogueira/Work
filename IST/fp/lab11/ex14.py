def polinomio(g0,g1,g2):
    def calc(x):
        return g0 + g1*x + g2*x**2
    return calc