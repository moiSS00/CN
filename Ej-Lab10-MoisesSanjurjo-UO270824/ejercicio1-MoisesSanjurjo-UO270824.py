# -*- coding: utf-8 -*-
"""
Ejercicio 1: Resolución de un sistema lineal con sustitución progresiva.

Función sust_prog: Calcula utilizando sustitución progresiva la solución 
del sistema lineal L*x = b, con L cuadrada triangular inferior no singular.

Argumentos de entrada:
         L: matriz cuadrada triangular inferior no singular del sistema lineal 
            L*x = b (array numpy de dos dimensiones).
         b: vector de términos independientes (array numpy de una dimensión).
         
Argumentos de salida:
         x: solución del sistema L*x = b (array numpy de una dimensión).

Ejemplos: 
          L = np.array([[2., 0, 0], [1, 2, 0]])
          b = np.array([2., -1, 0])
          x = sus_prog(L,b)
          print('Solución =', x)
          Salida:
              Error: La matriz L no es cuadrada
              Solución = None
          
          L = np.array([[2., 0, 0], [1, 2, 0], [1, 1, 0]])
          b = np.array([2., -1, 0])
          x = sus_prog(L,b)
          print('Solución =', x)
          Salida: 
              Error: La matriz L es singular
              Solución = None
    
          L = np.array([[2., 0, 0], [1, 2, 0], [1, 1, 2]])
          b = np.array([2., -1, 0])
          x = sus_prog(L,b)
          print('Solución =', x)
          # Comprobamos que L*x = b
          print('Comprobación: L*x =', np.dot(L,x), 'b = ', b)
          Salida: 
              Solución = [ 1. -1.  0.]
              Comprobación: L*x = [ 2. -1.  0.] b =  [ 2. -1.  0.]
              
          
"""

import numpy as np

np.set_printoptions(precision = 2)   # sólo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

# Función sus_prog 
#-----------------------------------------------------------------------------
def sus_prog(L,b):
    m,n = L.shape   # dimensiones de la matriz L
    # Comprobamos que la matriz L es cuadrada
    if m != n:
        print('La matriz L no es cuadrada')
        return
    # Comprobamos que las dimensiones de L y b son adecuadas
    if n != len(b):
        print('Las dimensiones no son correctas')
        return
    # Comprobamos que la matriz L es no singular
    d = np.diag(L)
    for i in range(0,len(d)):
        if d[i] == 0:
            print("La matriz L es singular")
            return
        
    # Resolvemos el sistema 
    x = np.zeros(len(b))              # definimos el vector solución x
    x[0] = b[0]/L[0,0]   # primera coordenada de x
    for i in range(0,len(b)):
        sumatorio = 0
        for j in range(0,i):
            sumatorio += (L[i,j]*x[j])
        x[i] = (1/L[i,i])*(b[i] - sumatorio)       # restantes coordenadas de x
    return x    


#--------------------------------------
# Ejemplos
#--------------------------------------
    
# Ejemplos de prueba
#--------------------------------------    

#PRIMER EJERMPLO DE PRUEBA
L = np.array([[2., 0, 0], [1, 2, 0]])
b = np.array([2., -1, 0])
x = sus_prog(L,b)
print('Solucion =', x)

#SEGUNDO EJEMPLO DE PRUEBA
L = np.array([[2., 0, 0], [1, 2, 0], [1, 1, 0]])
b = np.array([2., -1, 0])
x = sus_prog(L,b)
print('Solucion =', x)
          
#TERCER EJEMPLO DE PRUEBA 
L = np.array([[2., 0, 0], [1, 2, 0], [1, 1, 2]])
b = np.array([2., -1, 0])
x = sus_prog(L,b)
print('Solucion del sistema 1=', x)
# Comprobamos que L*x = b
print('Comprobacion: L*x =', np.dot(L,x), 'b = ', b)

# Ejemplo
#--------------------------------------
n = 5
np.random.seed(1)           # para que los números aleatorios se repitan
L = np.random.random((n,n)) # genera una matriz aleatoria nxn
L = np.tril(L)              # hacer cero los elementos por encima de la diagonal
b = np.random.random(n)  # genera un vector aleatorio de dimensión n
x = sus_prog(L,b)

print('L')
print(L)
print('b')
print(b)
print('Solucion del sistema 2 =', x)



   