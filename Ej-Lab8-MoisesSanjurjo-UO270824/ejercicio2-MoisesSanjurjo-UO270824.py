# -*- coding: utf-8 -*-
"""
Ejercicio 2: Aproximación numérica de orden 1 y de orden 2 de la 
derivada de la función f(x) = 1/x.

"""

import numpy as np
import matplotlib.pyplot as plt

# Función f(x)= 1/x y su derivada f'
f = lambda x:1/x      # función f
df = lambda x:(-1)/x**2     # derivada exacta f'

#---------------------------------------------------------------
# Derivación numérica de orden 1
#--------------------------------------------------------------- 
h = 0.01     # paso

a = 0.2     # extremo inferior del intervalo
b = 1.2     # extremo superior del intervalo
x = np.arange(a,b+h,h)     # vector con 1º coordenada a, última coordenanda b y diferencia entre coordenadas h

# Diferencias progresiva y regresivas
df_p = np.diff(f(x))/h      # vector que contiene los valores de las diferencias progresivas
df_r = df_p      # vector que contiene los valores de las diferencias regresivas

# Para los puntos interiores con aproximación centrada
df_c = (df_p[1:] + df_r[0:-1])/2 
# Extremo izquierdo con aproximación progresiva (orden 1)
df_a = df_p[0]
# Extremo derecho con aproximación regresiva (orden 1)
df_b = df_r[-1]

# Construimos un vector que contenga todos los valores de la der. num de orden 1
# El vector será de la forma [aprox. en extremo izdo, aprox. en puntos interiores, aprox. en extremo dcho.]
df_a = np.array([df_a])  # transformamos df_a en un vector
df_b = np.array([df_b])  # transformamos df_b en un vector
Aprox_1 = np.concatenate((df_a,df_c,df_b))  # vector que contiene los valores de la der. num. de orden 1

Error_1 = np.linalg.norm(df(x)-Aprox_1)/np.linalg.norm(df(x))          # error de orden 1
print("Error con derivacion de orden 1 = ",Error_1)             # escribimos el error en pantalla


#---------------------------------------------------------------
# Derivación numérica de orden 2
#---------------------------------------------------------------
# Para los puntos interiores la aproximación centrada es la misma que en el caso anterior
 
# Extremo izquierdo: aproximación progresiva (orden 2)
df_a2 = (-3*f(x[0])+4*f(x[0]+h)-f(x[0]+2*h))/(2*h)  
# Extremo derecho: aproximación regresiva (orden 2)
df_b2 = (f(x[-1]-2*h)-4*f(x[-1]-h)+3*f(x[-1]))/(2*h)

# Construimos un vector que contenga todos los valores de la der. num de orden 2
# El vector será de la forma [aprox. en extremo izdo, aprox. en puntos interiores, aprox. en extremo dcho.]
df_a2 = np.array([df_a2])       # transformamos df_a2 en un vector
df_b2 = np.array([df_b2])       # transformamos df_b2 en un vector
Aprox_2 = np.concatenate((df_a2,df_c,df_b2))     # vector que contiene los valores de la der. num. de orden 2

Error_2 = np.linalg.norm(df(x)-Aprox_2)/np.linalg.norm(df(x))     # error de orden 2
print("Error con derivacion de orden 2 = ",Error_2)        # escribimos el error en pantalla


