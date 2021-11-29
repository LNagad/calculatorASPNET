from sympy import *
init_printing()

def bobito(fun):

    try:
        # fun = '6x'
        x = symbols("x")
        f = fun
        # f = fun.strip('"')
        f = f.replace('x', '*x')
        # f = 5*x
    
        print(f)
        
        return integrate(f, x)
    except:
        return ''
