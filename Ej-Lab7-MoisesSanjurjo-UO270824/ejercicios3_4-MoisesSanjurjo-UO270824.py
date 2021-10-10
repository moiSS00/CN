# -*- coding: utf-8 -*-
"""
Ejercicios 3 y 4: Cálculo del polinomio de aproximación (caso continuo).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

#-----------------------------------------------------------------------------
# Ejercicio 3
#-----------------------------------------------------------------------------
f = lambda x : np.cos(x)

# Construimos la matriz A del sistema y el vector b de términos independientes
g = 2                               # grado del polinomio
A = np.zeros((g + 1,g + 1)) # matriz de coeficientes
b = np.zeros(g + 1)             # término independiente
for i in range(g + 1):          # recorremos las filas de A
    for j in range(g + 1):      # recorremos las columnas de A
        integrando_A = lambda x : x**(i+j) # tenemos que integrar x**(i+j)
        # integrate.quad devuelve la integral y una cota del error (dos coordenadas)  
        A[i,j] = integrate.quad(integrando_A,-1,1)[0] # tomamos sólo el valor de la integral (coordenada 0)
    # Para el término independiente b    
    integrando_b = lambda x : (x**i)*f(x) # tenemos que integrar x*i * f(x)
    b[i] = integrate.quad(integrando_b,-1,1)[0]  # tomamos sólo el valor de la integral (coordenada 0)
    
print('Matriz del sistema =\n', A)    # mostramos la matriz A
print('Término independiente =', b)   # mostramos el vector b

# Resolvemos el sistema
p = np.linalg.solve(A, b)
# Reordenamos los coeficientes del polinomio p 
# para que parezcan de mayor a menor potencia de x
p = p[::-1]
print('Coeficientes del polinomio p =', p)

# Para hacer la representación gráfica del polinomio
plt.close('all')

xx = np.linspace(-1,1)   # para hacer la gráfica del polinomio p en [-1,1]
yy = np.polyval(p,xx)   # evaluamos p en xx

plt.figure()
plt.plot(xx,f(xx),'red',label = 'exacta')  # dibujamos la función cos x (en rojo)
plt.plot(xx,yy, label = 'aproximada')  # dibujamos el polinomio
plt.grid()
plt.legend()
plt.show() 

# Calculamos el error relativo
error_rel = np.linalg.norm(f(xx) - yy)/np.linalg.norm(f(xx))
print('Error relativo = ', error_rel)


#-------------------------------------------------------------------------------------
# Ejercicio 4 (se resuelve como en el caso anterior pero con los datos del ejercicio 4)
#-------------------------------------------------------------------------------------

f = lambda x : np.cos(np.arctan(x)) - np.exp(x**2)*np.log(x+2)

# Construimos la matriz A del sistema y el vector b de términos independientes
g = 4             # grado del polinomio
A = np.zeros((g + 1,g + 1))             # matriz de coeficientes
b = np.zeros(g + 1)            # término independiente

for i in range(g + 1):          # recorremos las filas de A
    for j in range(g + 1):      # recorremos las columnas de A
        integrando_A = lambda x : x**(i+j) # tenemos que integrar x**(i+j)
        # integrate.quad devuelve la integral y una cota del error (dos coordenadas)  
        A[i,j] = integrate.quad(integrando_A,-1,1)[0] # tomamos sólo el valor de la integral (coordenada 0)
    # Para el término independiente b    
    integrando_b = lambda x : (x**i)*f(x) # tenemos que integrar x*i * f(x)
    b[i] = integrate.quad(integrando_b,-1,1)[0]  # tomamos sólo el valor de la integral (coordenada 0)
    
print('Matriz del sistema =\n', A)    # mostramos la matriz A
print('Término independiente =', b)   # mostramos el vector b

# Resolvemos el sistema
p = np.linalg.solve(A, b)
# Reordenamos los coeficientes del polinomio p 
# para que parezcan de mayor a menor potencia de x
p = p[::-1]
print('Coeficientes del polinomio p =', p)

# Para hacer la representación gráfica del polinomio
plt.close('all')

xx = np.linspace(-1,1)   # para hacer la gráfica del polinomio p en [-1,1]
yy = np.polyval(p,xx)   # evaluamos p en xx

plt.figure()
plt.plot(xx,f(xx),'red',label = 'exacta')  # dibujamos la función cos x (en rojo)
plt.plot(xx,yy, label = 'aproximada')  # dibujamos el polinomio
plt.grid()
plt.legend()
plt.show() 

# Calculamos el error relativo
error_rel = np.linalg.norm(f(xx) - yy)/np.linalg.norm(f(xx))
print('Error relativo = ', error_rel)

