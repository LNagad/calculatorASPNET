from sympy import *
init_printing()

def bobito(fun):

    try:
        # fun = '6x'
        x = symbols("x")
        e = symbols("e")
        pi = symbols("π")

        f = fun
        # f = fun.strip('"')


        if f[0] == 't' or  f[0] == 'c':
            pass
        elif f[0] != 'x':
            f = f.replace('x', '*x')
        else:
            pass            

        


        for i in range(len(f)):
            if "x**" in f:
                pass


        for i in range(len(f)):
            if "e" in f[i]:
                f = f.replace('e', '*e')

        for i in range(len(f)):
            if "π" in f[i]:
                f = f.replace('π', '*π')
                    
        # f = 5*x
    
        print(f)
        value = integrate(f, x)
        pprint(Integral(value, x), use_unicode= False)

        return integrate(f, x)
    except:
        return ''
