from timeit import timeit

import integrate_cy
import integrate


i1 = timeit(
    "integrate.integrate_f(2,5,10)", 
    setup="import integrate",
    number=1_000_000)

i2 = timeit(
    "integrate_cy.integrate_f(2,5,10)",
     setup="import integrate_cy",
     number=1_000_000)

# print(i1)
print(i1, i2)
print(i1/i2)