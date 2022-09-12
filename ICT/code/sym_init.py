# base

from sympy import init_printing
from sympy import symbols

# sqrt
from sympy import sqrt
from sympy import exp
from sympy import cos, sin

from sympy import subs
from sympy import expand, factor

from sympy import simplify

from sympy import solve, limit
from sympy import Integral
from sympy import diff, integrate


init_printing()
x, y, z = symbols("x y z")
expr = x + 2 * y
x2 = x ** 2

x * expr
x_cos = cos(x)
x_sin = sin(x)

# factor expand

expanded_expr = expand(x * expr)
factor(expanded_expr)

# diff
diff(sin(x) * exp(x), x)

integrate(exp(x) * sin(x) + exp(x) * cos(x), x)

integrate(sin(x2), (x, -oo, oo))

solve(x2 - 2, x)
limit(x_sin / x, x, 0)

Integral(sqrt(1 / x), x)

expr.subs(x, 1)
