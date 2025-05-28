from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y 
print(bieuthuc)

giatri = bieuthuc.subs({x:3, y:2})
print(giatri)

print(x)
print(y)

#Tình huông 1
giatri1 = bieuthuc.subs({x:3, y:x})
print(giatri1)

#Tình huông 2
giatri2 = bieuthuc.subs({x:y, y:3})
print(giatri2)

#Tình huông 3
giatri3 = bieuthuc.subs({y:x}).subs({x:3})
print(giatri3)