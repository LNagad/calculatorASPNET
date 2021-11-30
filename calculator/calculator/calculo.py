from sympy import *
init_printing()

def bobito(fun):

    try:
        # fun = '6x'
        x = symbols("x")
        e = symbols("e")

        f = fun
        # f = fun.strip('"')


        
        f = f.replace('x', '*x')

        for i in range(len(f)):
            if "x**" in f:
                pass


        for i in range(len(f)):
            if "e" in f[i]:
                f = f.replace('e', '*e')
                    
        

        # f = 5*x
    
        print(f)
        print(f)
        print(f)
        print(f)
        
        return integrate(f, x)
    except:
        return ''
