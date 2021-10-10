# -*- coding: utf-8 -*-
"""
Ejercicio 3: Integración - Fórmulas de cuadratura gaussianas.
-----------------------------------------------------------------------------
Función gauss: Halla la integral aproximada utlizando la fórmula de 
Gauss-Legendre para una función f en unintervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
    n:  número de nodos (número entero).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula de Gauss-Legendre con n nodos de la función
        f en [a,b] (número real).
    
Ejemplos:
    f = lambda x : x**2
    I = gauss(f,0,2,6)
    print('Ejemplo de prueba con Gauss-Legendre =', I)
    Salida:
        Ejemplo de prueba con Gauss-Legendre = 2.666666666666666
"""

import numpy as np
import sympy as sym

# Cálculo de la integral exacta de la función f(x) = exp(x) en [0,3]
#---------------------------------------------------------------------
x = sym.Symbol('x', real=True)            # definimos la variable x simbólica
f = sym.exp(x)            # definimos la función f simbólica 
I_exacta = sym.integrate(f,(x,0,3))
I_exacta = float(I_exacta)
print ('El valor exacto es: ',I_exacta)   


# Función gauss
#--------------------------------------
def gauss(f,a,b,n):
    [x, w] = np.polynomial.legendre.leggauss(n)         # se obtienen los nodos x (en [-1,1]) y los pesos w
    y = ((b-a)/2.0)*x+(a+b)/2.0              # nodos en [a,b]
    I = 0.0              # fórmula de cuadratura de Gauss-Legendre
    for i in range(0,len(y)):
        I += w[i]*f(y[i])*((b-a))/2.0
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
f = lambda x : x**2
I = gauss(f,0,2,6)
print('Ejemplo de prueba con Gauss-Legendre =', I)

#--------------------------------------
# Ejercicio 3
#--------------------------------------

#-----------------------
f = lambda x :np.exp(x) 
a = 0 
b = 3 
n = 1
I1 = gauss(f,a,b,n)
print ('El valor aproximado con 1 nodo es:', I1)
#-----------------------
n = 2
I2 = gauss(f,a,b,n)
print ('El valor aproximado con 2 nodos es:', I2)
#-----------------------
n = 3
I3 = gauss(f,a,b,n)
print ('El valor aproximado con 3 nodos es:', I3)
   


#-----------------------