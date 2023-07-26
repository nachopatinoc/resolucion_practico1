"""
@author: Ignacio Patiño
Trabajo Práctico - Git Essentials
"""


import sympy as sp
import math

# Trabajo Práctico primero:

# =====================================================================================
# PUNTO 1: Escribe el codigo en Python para aproximar funciones con Serie de Taylor, para distintas ´
# funciones y distintos ordenes del polinomio.
# =====================================================================================

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def serie_de_taylor(func, x, a, orden):
    aprox = 0
    derivada = func
    for n in range(orden):
        term = derivada.subs(x, a) * ((x - a) ** n) / factorial(n)
        aprox += term
        derivada = derivada.diff(x)
    return aprox

x = sp.Symbol("x")
funcion = sp.sqrt(x + 1)
a = 0

for orden in [1, 2, 3]:
    aproximacion = serie_de_taylor(funcion, x, a, orden)
    print(f"Aproximación de la función {funcion} en orden {orden} alrededor de x = {a}:")
    print(aproximacion)
    print("-------------------------------------------------------------------------------")

# Aproximaciones utilizando la Serie de Taylor para x / (x + 1)
funcion = x / (x + 1)
a = 1

for orden in [1, 2, 3]:
    aproximacion = serie_de_taylor(funcion, x, a, orden)
    print(f"Aproximación de la función {funcion} en orden {orden} alrededor de x = {a}:")
    print(aproximacion)
    print("-------------------------------------------------------------------------------")

