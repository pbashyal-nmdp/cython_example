from setuptools import setup
from Cython.Build import cythonize


setup(
    name="Integrate App",
    ext_modules=cythonize("integrate_cy.pyx", annotate=True), 
    zip_safe=False,
)
