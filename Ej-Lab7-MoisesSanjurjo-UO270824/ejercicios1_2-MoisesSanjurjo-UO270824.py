# -*- coding: utf-8 -*-
"""
Ejercicios 1 y 2: Cálculo del polinomio de aproximación (caso discreto). 
Utilizamos la matriz de Vandermonde (ver ejercicio1.py del Interpolación).

-----------------------------------------------------------------------------
Función Vandermonde_g: Halla la matriz de Vandermonde a partir 
de un vector x (nodos) para construir un polinomio de aproximación de grado g. 

Argumentos de entrada:
    x:  vector que contiene los nodos (array numpy).
    g:  grado del polinomio de aproximación (número entero).
             
Argumentos de salida:
    V:  matriz de Vandermonde con g+1 columnas (array numpy).
    
Ejemplos:
    x = np.array([1,2,3,4,5.])
    print('Matriz de Vandermonde con 4 columnas =\n', Vandermonde_g(x,3))
    Salida:
        Matriz de Vandermonde con 4 columnas =
        [[  1.   1.   1.   1.]
        [  1.   2.   4.   8.]
        [  1.   3.   9.  27.]
        [  1.   4.  16.  64.]
        [  1.   5.  25. 125.]]
"""

import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

# Función Vandermonde_g
#--------------------------------------------------------
def Vandermonde_g(x,g):
    n = len(x)        # dimensión de x   
    V = np.ones((n, g+1)) # la matriz de Vandermonde tiene g+1 columnas
    for i in range(1, g+1):
        V[:,i] = V[:,i-1]*x # multiplicamos cada colunma por el vector x para
                            # generar la siguiente columna                                    
    return V

#--------------------------------------
# Ejemplos
#--------------------------------------

# Ejemplo de prueba 
x = np.array([1,2,3,4,5.]) 
print('Matriz de Vandermonde con 4 columnas =\n', Vandermonde_g(x,3))    

#------------------------------------------------------------------------------
# Ejercicio1 
#------------------------------------------------------------------------------
# Datos
f = lambda x : np.cos(x)         # función
x = np.array([-1,-0.5,0,0.5,1])  # nodos
y = f(x)  # valores en los nodos

# Calculamos el polinomio de aproximación de grado 2

# Calculamos la matriz de Vandermonde
V = Vandermonde_g(x,2)
# La traspuesta de V es V.T
A = np.dot(V.transpose(),V)       # multiplicamos V traspuesa por V (matriz del sistema)      
b = np.dot(V.transpose(),y.transpose())       # multiplicamos V traspuesa por y traspuesto (vector de términos independientes)
print('Matriz del sistema =\n', A)    # mostramos la matriz A
print('Término independiente =', b)   # mostramos el vector b

# Resolvemos el sistema
p = np.linalg.solve(A, b)
print('Solución del sistema =',p) # p es el polinomio de aproximación

# Reordenamos los coeficientes del polinomio p 
# para que parezcan de mayor a menor potencia de x
p = p[::-1]


# Para hacer la representación gráfica del polinomio
plt.close('all')

xx = np.linspace(-1,1)   # para hacer la gráfica del polinomio p  en [-1,1]
yy = np.polyval(p,xx) # evaluamos p en xx

plt.figure(1)
plt.plot(x,y,'ro')      # dibujamos los puntos (en rojo con o)
plt.plot(xx,yy, label = 'p')      # dibujamos el polinomio
plt.grid()
plt.legend() 
plt.show()
   
#------------------------------------------------------------------------------
# Ejercicio 2 (se resuelve como el caso anterior pero con los datos del ejercicio 2)
#------------------------------------------------------------------------------
# Datos
f = lambda x : np.cos(np.arctan(x)) - np.exp(x**2)*np.log(x+2)
x = np.linspace(-1,1,10)
y = f(x)

# Calculamos el polinomio de aproximación de grado 4

# Calculamos la matriz de Vandermonde
V = Vandermonde_g(x,4)
# La traspuesta de V es V.T
A = np.dot(V.transpose(),V)       # multiplicamos V traspuesa por V (matriz del sistema)      
b = np.dot(V.transpose(),y.transpose())       # multiplicamos V traspuesa por y traspuesto (vector de términos independientes)
print('Matriz del sistema =\n', A)    # mostramos la matriz A
print('Término independiente =', b)   # mostramos el vector b

# Resolvemos el sistema
p = np.linalg.solve(A, b)
print('Solución del sistema =',p) # p es el polinomio de aproximación

# Reordenamos los coeficientes del polinomio p 
# para que parezcan de mayor a menor potencia de x
p = p[::-1]


# Para hacer la representación gráfica del polinomio
plt.close('all')

xx = np.linspace(-1,1)   # para hacer la gráfica del polinomio p  en [-1,1]
yy = np.polyval(p,xx) # evaluamos p en xx

plt.figure(1)
plt.plot(x,y,'ro')      # dibujamos los puntos (en rojo con o)
plt.plot(xx,yy, label = 'p')      # dibujamos el polinomio
plt.grid()
plt.legend() 
plt.show()



