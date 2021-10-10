# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
Ejercicio 2: Integración - Fórmulas de cuadratura compuestas.
-----------------------------------------------------------------------------
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


"""
Ejercicio 2a: Integración - Fórmula del punto medio compuesta.
-----------------------------------------------------------------------------
Función punto_medio_comp: Halla la integral aproximada utilizando la fórmula del 
punto medio compuesta para una función f en un intervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
    n:  número de subintervalos (número entero).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula del punto medio compuesta de la función
        f en [a,b] (número real).
    
Ejemplos:
    f = lambda x : x**2
    I = punto_medio_comp(f,0,2,4)
    print('Ejemplo de prueba con punto medio compuesta =', I)
    Salida:
        Ejemplo de prueba con punto medio compuesta = 2.625
"""


# Función punto_medio_comp
#--------------------------------------
def punto_medio_comp(f,a,b,n):
    h = (b-a)/float(n)              # longitud de los subintervalos
    x = np.arange(a,b+h,h) # vector que contiene los puntos medios de los subintervalos
    I = 0.0
    for i in range(1,n+1):
        I += f((x[i-1]+x[i])/2.0)
    I = h*I       # fórmula del punto medio compuesta
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
f = lambda x : x**2
I = punto_medio_comp(f,0,2,4)
print('Ejemplo de prueba con punto medio compuesta =', I)

#--------------------------------------
# Ejercicio 2a
#--------------------------------------

# Cálculo de la integral aproximada
#---------------------------------------
f = lambda x :np.exp(x)
a = 0
b = 3
n = 5
Ipmc = punto_medio_comp(f,a,b,n)

print ('El valor aproximado con punto medio compuesta es:', Ipmc)


"""
Ejercicio 2b: Integración - Fórmula del trapecio compuesta.
-----------------------------------------------------------------------------
Función trapecio_comp: Halla la integral aproximada utilizando la fórmula del 
trapecio compuesta para una función f en un intervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
    n:  número de subintervalos (número entero).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula del trapecio compuesta de la función
        f en [a,b] (número real).
    
Ejemplos:
    f = lambda x : x**2
    I = trapecio_comp(f,0,2,4)
    print('Ejemplo de prueba con trapecio compuesta =', I)
    Salida:
        Ejemplo de prueba con trapecio compuesta = 2.75
"""


# Función trapecio_comp
#--------------------------------------
def trapecio_comp(f,a,b,n):
    h = (b-a)/float(n)            # longitud del intervalo
    x = np.arange(a,b+h,h) # vector que contiene los nodos intermedios
    I = 0.0
    for i in range(1,n):
        I += f(x[i])
    I = (h/2.0)*(f(a)+f(b)) + h*I           # fórmula del trapecio compuesta
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
f = lambda x : x**2
I = trapecio_comp(f,0,2,4)
print('Ejemplo de prueba con trapecio compuesta =', I)

#--------------------------------------
# Ejercicio 2b
#--------------------------------------

# Cálculo de la integral aproximada
#---------------------------------------
f = lambda x :np.exp(x)
a = 0
b = 3
n = 4
Itc = trapecio_comp(f,a,b,n)

print ('El valor aproximado con trapecio compuesta es:', Itc)


"""
Ejercicio 2c: Integración - Fórmula de Simpson compuesta.
-----------------------------------------------------------------------------
Función simpson_comp: Halla la integral aproximada utilizando la fórmula de 
Simpson compuesta para una función f en un intervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
    n:  número de subintervalos (número entero).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula de Simpson compuesta de la función
        f en [a,b] (número real).
    
Ejemplos:
    f = lambda x : x**2
    I = simpson_comp(f,0,2,6)
    print('Ejemplo de prueba con Simpson compuesta =', I)
    Salida:
        Ejemplo de prueba con Simpson compuesta = 2.6666666666666665
"""

# Función simpson_comp
#--------------------------------------
def simpson_comp(f,a,b,n):
    h = (b-a)/float(n)                                 # longitud de los subintervalos 
    x1 = np.arange(a,b+h,h) # nodos que separan los subintervalos
    I = 0.0                                 # fórmula de Simpson compuesta
    for i in range(1,n+1,1): 
        I += f(x1[i-1]) + 4.0*f((x1[i-1]+x1[i])/2.0) + f(x1[i])
    I = (h/6.0)*I
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
f = lambda x : x**2
I = simpson_comp(f,0,2,6)
print('Ejemplo de prueba con Simpson compuesta =', I)

#--------------------------------------
# Ejercicio 2c
#--------------------------------------

# Cálculo de la integral aproximada
#---------------------------------------
f = lambda x :np.exp(x)
a = 0
b = 3
n = 4
Its = simpson_comp(f,a,b,n)

print ('El valor aproximado con Simpson compuesta es:', Its)