# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
Ejercicio 1: Integración - Fórmulas de cuadratura simples.
-----------------------------------------------------------------------------
"""
import numpy as np
import sympy as sym


# Cálculo de la integral exacta de la función f(x) = exp(x) en [0,3]
#----------------------------------------------------------------------------
x = sym.Symbol('x', real=True)            # definimos la variable x simbólica
f = sym.exp(x)            # definimos la función f simbólica 
I_exacta = sym.integrate(f,(x,0,3))
I_exacta = float(I_exacta)
print ('El valor exacto es: ',I_exacta)   

"""
Ejercicio 1a: Integración - Fórmula del punto medio simple.
-----------------------------------------------------------------------------
Función punto_medio: Halla la integral aproximada utlizando la fórmula del 
punto medio simple para una función f en unintervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula del punto medio simple de la función
        f en [a,b] (número real).
    
Ejemplos:
    f = lambda x : x**2
    I = punto_medio(f,0,2)
    print('Ejemplo de prueba con punto medio simple =', I)
    Salida:
        Ejemplo de prueba con punto medio simple = 2.0
      
"""

# Función punto_medio
#--------------------------------------
def punto_medio(f,a,b):
    I = (b-a)*f((a+b)/2.0)      # fórmula del punto medio simple
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
print('Ejemplo de prueba con punto medio simple =', punto_medio(lambda x : x**2,0,2))

#--------------------------------------
# Ejercicio 1a
#--------------------------------------

# Cálculo de la integral aproximada
#---------------------------------------
f = lambda x :np.exp(x)   # función
a = 0
b = 3
Ipm = punto_medio(f,a,b)  # cálculo de la integral aproximada con

print ('El valor aproximado con punto medio simple es:', Ipm)


"""
Ejercicio 1b: Integración - Fórmula del trapecio simple.
-----------------------------------------------------------------------------
Función trapecio: Halla la integral aproximada utlizando la fórmula del 
trapecio simple para una función f en unintervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula del trapecio de la función
        f en [a,b].
    
Ejemplos:
    f = lambda x : x**2
    I = trapecio(f,0,2)
    print('Ejemplo de prueba con trapecio simple =', I)
    Salida:
       Ejemplo de prueba con trapecio simple = 4.0
"""

# Función trapecio
#--------------------------------------
def trapecio(f,a,b):
    I = ((b-a)/2.0)*(f(a)+f(b))    
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
print('Ejemplo de prueba con trapecio simple =', trapecio(lambda x : x**2,0,2))

#--------------------------------------
# Ejercicio 1b
#--------------------------------------

# Cálculo de la integral aproximada
#---------------------------------------
It = trapecio(f,a,b)
print ('El valor aproximado con trapecio simple es:', It)



"""
Ejercicio 1c: Integración - Fórmula de Simpson simple.
-----------------------------------------------------------------------------
Función simpson: Halla la integral aproximada utlizando la fórmula de 
Simpson simple para una función f en unintervalo [a,b]. 

Argumentos de entrada:
    f:  función integrando (función lambda).
    a:  extremo inferior del intervalo de integración (número real).
    b:  extremo superior del intervalo de integración (número real).
             
Argumentos de salida:
    I:  integral aproximada con la fórmula de Simpson de la función
        f en [a,b].
    
Ejemplos:
    f = lambda x : x**2
    I = simpson(f,0,2)
    print('Ejemplo de prueba con simpson simple =', I)
    Salida:
        Ejemplo de prueba con simpson simple = 2.6666666666666665
"""

# Función simpson
#--------------------------------------
def simpson(f,a,b):
    I = ((b-a)/6.0)*(f(a)+4*f((a+b)/2.0)+f(b)) 
    return I

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba
print('Ejemplo de prueba con simpson simple =', simpson(lambda x : x**2,0,2))

#--------------------------------------
# Ejercicio 1c
#--------------------------------------

# Cálculo de la integral aproximada
#---------------------------------------
Is = simpson(f,a,b)
print ('El valor aproximado con simpson simple es:', Is)