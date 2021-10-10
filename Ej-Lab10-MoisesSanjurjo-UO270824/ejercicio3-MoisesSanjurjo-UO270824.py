# -*- coding: utf-8 -*-
"""
Ejercicio 3: Descomposición LU de una matriz para resolver un sistema lineal
de ecuaciones.

Función LU: Para una matriz cuadrada A calcula las matirces L y tales que A = L*U, con
U triangular superior y L triangular inferior.

Argumentos de entrada:
         A: matriz cuadrada (array numpy de dos dimensiones)
         
Argumentos de salida:
         L: matriz triangular inferior (array numpy de dos dimensiones).
         U: matriz triangular superior (array numpy de dos dimensiones).

Ejemplos: 
         A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]]) 
         b = np.array([2.,4,6])
         L,U = LU(A)
         print('L=')
         print(L)
         print('U=') 
         print(U) 
          Salida:
              L = 
               [[1.   0.   0.  ]
               [0.5  1.   0.  ]
               [0.5  0.33 1.  ]]
              U =
               [[2.   1.   1.  ]
               [0.   1.5  0.5 ]
               [0.   0.   1.33]
          
"""
import numpy as np

# Función LU 
#-----------------------------------------------------------------------------
def LU(A):
    m,n = A.shape   # dimensiones de la matriz A
    # Comprobamos que la matriz A es cuadrada
    if m != n:
        print('La matriz A no es cuadrada')
        return
    U = np.copy(A)  # hacemos una copia de A
    L = np.eye(n)  
    for k in range(0,n):               # bucle para recorrer las columnas
        for i in range(k+1,m): # bucle para recorrer las filas
            f = U[i,k]/U[k,k]                # coeficiente f
            U[i,:] -= f*U[k]              # Fila i - f veces la Fila k
            L[i,k] = f               # el elemento (i,k) de L es el correspondiente coeficiente f
    return L,U 

#--------------------------------------
# Ejemplos
#--------------------------------------
    
# Ejemplo de prueba   
#-------------------------
A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]]) 
b = np.array([2.,4,6])
L,U = LU(A)
print('L=')
print(L)
print('U=') 
print(U)     


# Función sus_prog (ver ejercicio1.py)
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


# Función sus_regre (ver ejercicio2.py)   
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
# Ejercicios
#--------------------------------------
   
# Ejercicio 1 
#--------------------------------------
y = sus_prog(L,b)
x = sus_regre(U,y)
print('Solucion del sistema 1 =', x)


# Ejercicio 2 
#--------------------------------------
n = 5
np.random.seed(4)           
A = np.random.random((n,n)) 
b = np.random.random(n) 
L,U = LU(A)
y = sus_prog(L,b)
x = sus_regre(U,y) 

print('\n A')
print(A)
print('\n b') 
print(b)
print('Solucion del sistema 2 =',x)

