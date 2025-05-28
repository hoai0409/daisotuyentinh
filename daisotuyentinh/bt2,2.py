from sympy import factor, Symbol, expand
x = Symbol('x') 
y = Symbol('y')
bieuthuc = x**3 - y**3
print(factor(bieuthuc))

bieuthuc = (x - y)*(x**2 + x*y + y**2) 
print(expand(bieuthuc)) 