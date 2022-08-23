# cython: language_level=3
import cython

cdef double my_function(double x):
    return x ** 2 - x

cpdef double integrate_f(double a, double b, int n):
    cdef int i
    cdef double s
    cdef double dx

    s = 0
    dx = (b - a) / n

    for i in range(n):
      s += my_function(a + (i+0.5) * dx)

    return s * dx

