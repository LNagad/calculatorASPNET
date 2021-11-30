
from sympy import *
init_printing()

        # fun = '6x'
x = symbols("x")
e = symbols("e")
pi = symbols("π")
f = sec(x)*2


# for i in range(len(f)):
#         if "x**" in f[i]:


pprint(Integral(f, x), use_unicode= True)
lol = integrate(f,x)
print('\n')
pprint(Integral(lol, x), use_unicode= True)

    

    
    


