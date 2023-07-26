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

# =====================================================================================
# PUNTO 2: Escribe el codigo en Python para para aproximar raíces de una ecuacion utilizando el ´
# metodo de Newton, con una precisión de hasta tres posiciones decimales.
# =====================================================================================

def funcion(x):
    return x**6 - x**5 - 6*x**4 - x**3 + x + 10

def derivada(x):
    return 6*x**5 - 5*x**4 - 24*x**3 - 3*x**2 + 1

def newton(precision, valor_inicial, max_iteraciones=100):
    x_actual = valor_inicial
    for i in range(max_iteraciones):
        x_siguiente = x_actual - funcion(x_actual) / derivada(x_actual)
        if abs(funcion(x_siguiente)) < precision:  # abs hace el valor absoluto
            return x_siguiente
        x_actual = x_siguiente
    return x_actual

raiz_aproximada = newton(0.001, 1)
print("Raíz aproximada:", round(raiz_aproximada, 3))
print("-------------------------------------------------------------------------------")

# =====================================================================================
# EL MISMO CÓDIGO PERO PARA LA 2DA FUNCIÓN: 
# =====================================================================================

def funcion(x):
    return x*2 * (2 - x - x*2)**0.5 - 1

def newton(precision, valor_inicial, max_iteraciones=100):
    x_actual = valor_inicial
    for _ in range(max_iteraciones):
        x_siguiente = x_actual - funcion(x_actual) / ((funcion(x_actual + 1e-5) - funcion(x_actual - 1e-5)) / (2e-5))
        if abs(funcion(x_siguiente)) < precision:
            return x_siguiente
        x_actual = x_siguiente
    return x_actual

raiz_aproximada = newton(0.001, 0.5)
print("Raíz aproximada:", raiz_aproximada)
print("-------------------------------------------------------------------------------")
