from fractions import Fraction



f = Fraction(3,4)


f


from sympy import *


x = symbols('X')


a = Integral(cos(x)*exp(x),x)


Eq(a,a.doit())


x, y = symbols('x y')


expr = x + 2*y


expr


x*expr


expanded_expr = expand(x*expr)


expanded_expr


integrate(exp(x)*sin(x)+ exp(x)*cos(x),x)


a = (x + 1)**2
b = x**2 +2*x +1


simplify(a)


a - b


Rational(1,2)


a.subs(x,1)


expr = x**y


expr


expr = expr.subs(y, x**y)


expr


expr = sin(2*x) + cos(2*x)


expand_trig(expr)


expr = x**3 + 4*x*y


expr.subs([(x,2), (y,3)])



