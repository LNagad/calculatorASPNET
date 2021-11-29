from sympy import *
init_printing()

def bobito(fun):

    try:
        x = symbols("x")

        f = fun
        f = fun.strip('"')
        return integrate(f, x)
    except:
        return ''

    
    


