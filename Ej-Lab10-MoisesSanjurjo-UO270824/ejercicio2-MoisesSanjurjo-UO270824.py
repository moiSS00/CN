# -*- coding: utf-8 -*-
"""
Ejercicio 2: Resolución de un sistema lineal con sustitución regresiva.

Función sust_regre: Calcula utilizando sustitución regresiva la solución 
del sistema lineal U*x = b, con U cuadrada triangular superior no singular.

Argumentos de entrada:
         U: matriz cuadrada triangular superior no singular del sistema lineal 
            L*x = b (array numpy de dos dimensiones).
         b: vector de términos independientes (array numpy de una dimensión).
         
Argumentos de salida:
         x: solución del sistema U*x = b (array numpy de una dimensión).

Ejemplos: 
          U = np.array([[2., 1, 1], [0, 2, 1]])
          b = np.array([9., 4, 4])
          x = sus_regre(U,b)
          print('Solución =', x)
          Salida:
              Error: La matriz U no es cuadrada
              Solución = None
          
          U = np.array([[2., 1, 1], [0, 0, 1], [0, 0, 2]])
          b = np.array([9., 4, 4])
          x = sus_regre(U,b)
          print('Solución =', x)
          Salida: 
              Error: La matriz U es singular
              Solución = None
    
          U = np.array([[2., 1, 1], [0, 2, 1], [0, 0, 2]])
          b = np.array([9., 4, 4])
          x = sus_regre(U,b)
          print('Solución =', x)
          # Comprobamos que U*x = b
          print('Comprobación: U*x =', np.dot(U,x), 'b = ',b)
          Salida: 
              Solución = [3. 1. 2.]
              Comprobación: U*x = [9. 4. 4.] b =  [9. 4. 4.]    
          
"""

import numpy as np

np.set_printoptions(precision = 2)   # sólo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

# Función sus_regre
#-----------------------------------------------------------------------------
def sus_regre(U,b):
    m,n = U.shape   # dimensiones de la matriz U
    # Comprobamos que la matriz U es cuadrada
    if m != n:
        print('La matriz U no es cuadrada')
        return
    # Comprobamos que las dimensiones de U y b son adecuadas
    if n != len(b):
        print('Las dimensiones no son correctas')
        return
    # Comprobamos que la matriz U es no singular
    d = np.diag(U)
    for i in range(0,len(d)):
        if d[i] == 0:
            print("La matriz U es singular")
            return
    # Resolvemos el sistema 
    x = np.zeros(len(b))          # definimos el vector solución x
    x[-1] = b[-1]/U[len(b)-1][len(b)-1]   # última coordenada de x
    for i in range(n-1,-1,-1): 
        sumatorio = 0
        for j in range(i+1,n):
            sumatorio += (U[i,j]*x[j])
        x[i] = (1/U[i,i])*(b[i] - sumatorio) # restantes coordenadas de x
    return x    


#--------------------------------------
# Ejemplos
#--------------------------------------
    
# Ejemplos de prueba   
#--------------------------------------
    
#PRIMER EJERMPLO DE PRUEBA
U = np.array([[2., 1, 1], [0, 2, 1]])
b = np.array([9., 4, 4])
x = sus_regre(U,b)
print('Solución =', x)

#SEGUNDO EJEMPLO DE PRUEBA 
U = np.array([[2., 1, 1], [0, 0, 1], [0, 0, 2]])
b = np.array([9., 4, 4])
x = sus_regre(U,b)
print('Solución =', x)

#TERCER EJEMPLO DE PRUEBA 
U = np.array([[2., 1, 1], [0, 2, 1], [0, 0, 2]])
b = np.array([9., 4, 4])
x = sus_regre(U,b)
print('Solucion del sistema 1 =', x)
# Comprobamos que U*x = b
print('Comprobacion: U*x =', np.dot(U,x), 'b = ',b)

# Ejemplo
#--------------------------------------
n = 5
np.random.seed(2)           
U = np.random.random((n,n)) 
U = np.triu(U)              # Haz cero los elementos bajo la diagonal
b = np.random.random(n)  
x = sus_regre(U,b)

print('U')
print(U)
print('b')
print(b)
print('Solucion del sistema 2 =', x)
