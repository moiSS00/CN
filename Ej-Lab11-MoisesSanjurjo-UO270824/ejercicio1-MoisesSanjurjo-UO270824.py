# -*- coding: utf-8 -*-

"""
Ejercicio 1: Resolución de un sistema lineal con el método de Jacobi.

Función jacobi: Calcula utilizando el método de Jacobi la solución aproximada
del sistema lineal A*x = b, con A cuadrada no singular.

Argumentos de entrada:
         A:       matriz cuadrada no singular del sistema lineal 
                  A*x = b (array numpy de dos dimensiones).
         b:       vector de términos independientes (array numpy de una dimensión).
         tol:     cota superior del error: ||x_{k}-x_{k-1}||< tol (número 
                  real). 
         maxiter: máximo número de iteraciones (número entero positivo). Por 
                  defecto se toma maxiter = 1000
         
Argumentos de salida:
         x: aproximación k-ésima de la solución del sistema A*x = b (array numpy de una dimensión).
         k: número de iteraciones realizado (número entero)

Ejemplos: 
        tol = 1.e-6
        A = np.array([[5.,1,-1,-1],[1,4,-1,1],[1,1,-5,-1],[1,1,1,-4]])
        b = np.array([1.,1,1,1])
        x, k = jacobi(A,b,tol)
        print('x =',x)        
        print('Iteraciones =', k)
        Salida:
            x = [ 0.0937499  0.2499999 -0.0937499 -0.1874999]
            Iteraciones = 18
                          
"""
import numpy as np

np.set_printoptions(precision = 7)   # sólo 7 decimales
np.set_printoptions(suppress = True)   # no usar notación exponencial

def jacobi(A,b,tol,maxiter=1000):
    m,n = A.shape   # dimensiones de la matriz A
    # Comprobamos que la matriz A es cuadrada
    if m != n:
        print('La matriz A no es cuadrada')
        return
    # Comprobamos que las dimensiones de A y b son adecuadas
    if n != len(b):
        print('Las dimensiones no son correctas')
        return 
    # Comprobamos que la matriz A es no singular
    d = np.diag(A)
    for i in range(0,len(d)):
        if d[i] == 0:
            print("La matriz A es singular")
            return
    x = np.zeros(len(b)) # inicializamos el vector x donde guardaremos las iteraciones
    test_parada = False  # inicializamos el test de parada como False 
    k = 0        # inicializamos el contador de iteraciones
    sumatorio = 0
    while test_parada == False and k < maxiter:       
        xant = np.copy(x)
        for i in range(0,len(x)):
            for j in range(0,len(x)):
                if j!= i: 
                    sumatorio += (A[i,j]*xant[j])
            x[i] = (1/A[i,i])*(b[i] - sumatorio) # fórmula de Jacobi
            sumatorio = 0
        test_parada = np.linalg.norm(x-xant) < tol   # test de parada
        k += 1                      # actualizamos el contador de operaciones 
    return x,k    

#--------------------------------------
# Ejemplos
#--------------------------------------
    
# Ejemplo de prueba 
#--------------------------------------
tol = 1.e-6
A = np.array([[5.,1,-1,-1],[1,4,-1,1],[1,1,-5,-1],[1,1,1,-4]])
b = np.array([1.,1,1,1])
x, k = jacobi(A,b,tol)
print('x =',x)        
print('Iteraciones =', k)  


# Ejemplo 2
#-------------------------------
n = 9 

A1 = np.diag(np.ones(n))*2 
A2 = np.diag(np.ones(n-1),1)
A = A1 + A2 + A2.T 

b = np.concatenate((np.arange(1,6),np.arange(4,0,-1)))*1.

print('A')
print(A)
print('b') 
print(b)
x, k = jacobi(A,b,tol)
print('x =',x)        
print('Iteraciones =', k)  

