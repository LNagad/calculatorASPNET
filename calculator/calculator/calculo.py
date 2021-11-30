from sympy import *
init_printing()

def integrar(fun):

    try:
        # fun = '6x'
        x = symbols("x")
        e = symbols("e")
        pi = symbols("π")

        f = fun
        # f = fun.strip('"')

    # --------------------- validaciones necesarias

        if f[0] == 't' or  f[0] == 'c':
            pass
        elif f[0] == 's':
            pass
        elif f[0] != 'x':
            f = f.replace('x', '*x')
        else:
            pass            

        for i in range(len(f)):
            if "x**" in f:
                pass

        for i in range(len(f)):
            if f[0] == 'e' or f[1] == 'e':
                pass
        
        

        for i in range(len(f)):
            if "π" in f[i]:
                f = f.replace('π', '*π')
                
        
        f = f.replace('e', '*e')

        # for i in range(len(f)):
        #     if ")" in f[i]:
        #         f = f.replace(')', '*)')
                    
        # f = 5*x
    
        print(f)
        value = integrate(f, x)

        pprint(Integral(f, x), use_unicode= True)
        print('\n')

        pprint(Integral(value, x), use_unicode= True)
        html = '''
        
        '''
        return integrate(f, x)
    except:
        return ''
