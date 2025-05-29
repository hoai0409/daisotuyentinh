from sympy import Symbol 
x = Symbol('x') 
f = x + x + x + 2 
print(f)
#ví dụ
a = Symbol('Noi') 
b = Symbol('Chim')
print(3*b + 7*a)

print(a.name)
print(b.name)

#ví dụ khác
x1 = Symbol('x')
y1 = Symbol('y') 
s = x*y1 + y1*x1
print(s)

p = x1*(x1+2*x1)
print(p)

p = (x1+2)*(y1+3) 
print(p)

p = (x1+2)*(y1+3) + (x1+2)*(x1-3)
print(p)
