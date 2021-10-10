# -*- coding: utf-8 -*-
"""
Ejercicios 3: Aproximación numérica de la segunda derivada de la función
f(x) = sen(2xpi).
"""

import numpy as np

# Función f(x) = sen(2xpi) y su derivada segunda f''
f = lambda x: np.sin(2*np.pi*x)      # función f
d2f = lambda x: -4*np.pi**2*np.sin(2*np.pi*x)    # derivada segunda exacta f''

h = 0.01      # paso

a = 0      # extremo inferior del intervalo
b = 1      # extremo superior del intervalo
x = np.arange(a,b+h,h)      # vector con 1º coordenada a, última coordenanda b y diferencia entre coordenadas h

# Aproximación numérica de f''
fx = f(x)     # valores de f en el vector x
d2f_c = (fx[0:-2]-2*fx[1:-1]+fx[2:])/h**2 # derivada segunda aproximada

# Error
x_c = x[1:-1]        # puntos interiores de x (sin los extremos)
Error_d2f = np.linalg.norm(d2f(x_c)-d2f_c)/np.linalg.norm(d2f(x_c))  # error relativo
print("Error relativo = ",Error_d2f)       # escribimos en pantalla el error relativo
