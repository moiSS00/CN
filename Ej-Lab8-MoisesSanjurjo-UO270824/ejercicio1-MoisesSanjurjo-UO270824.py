# -*- coding: utf-8 -*-
"""
Ejercicio 1: Aproximación numérica de la derivada de la función f(x) = exp(x).

"""

import numpy as np
import matplotlib.pyplot as plt

# Función exponencial y su derivada f'
f =  lambda x:np.exp(x)            # función f
df = lambda x:np.exp(x)          # derivada exacta f'

#---------------------------------------------------------------
# h = 0.1
#--------------------------------------------------------------- 
h = 0.1     # paso

# Gráfica de la derivada
plt.close('all') # cerramos todas las ventanas

plt.figure(1)               
xx = np.linspace(0,1)             # definimos un vector x para dibujar la derivada en [0,1]
plt.plot(xx,df(xx),'--')   # dibujamos la derivada
plt.grid()

# Diferencias progresivas, regresivas y centradas
a = 0               # extremo inferior del intervalo
b = 1               # extremo superior del intervalo
x = np.arange(a,b+h,h)    # vector con 1º coordenada a, última coordenanda b y diferencia entre coordenadas h
df_p = np.diff(f(x))/h   # vector que contiene los valores de las diferencias progresivas
df_r = df_p                     # vector que contiene los valores de las diferencias regresivas
df_c = (df_p[1:] + df_r[0:-1])/2 # vector que contiene los valores de las diferencias centradas

# Gráfica de f' y de las diferencia progresivas, regresivas y centradas
xp = x[0:-1]    # vector con las coordenadas x para las diferencias progresivas
xr = x[1:]    # vector con las coordenadas x para las diferencias regresivas
xc = x[1:-1]    # vector con las coordenadas x para las diferencias centradas
plt.plot(xp,df_p,xr,df_r,xc,df_c)  # dibujamos las diferencias progresivas, regresivas y centradas
plt.legend(["df","df_p","df_r","df_c"]) # leyenda
plt.title("Derivada de f(x) = e^x y sus aproximaciones (h=0.1)") # título de la gráfica
plt.show()

## Gráfica de los errores en cada punto
plt.figure(2)  # abrimos una nueva figura
plt.plot(xp,abs(df(xp)-df_p),'o',xr,abs(df(xr)-df_r),'o',xc,abs(df(xc)-df_c),'o')    # dibujamos los valores |f'(x_i)-df_aprox(x_i)| para las 
# diferentes aproximaciones (progresiva, regresiva y centrada)
plt.grid() 
plt.legend(["df_p","df_r","df_c"]) # leyenda
plt.title("Errores (h=0.1)")    # título
plt.show()

## Errores globales relativos
ErrorG_p = np.linalg.norm((df(xp)-df_p))/np.linalg.norm(df(xp)) # error global relativo para aprox. progresiva
ErrorG_r = np.linalg.norm((df(xr)-df_r))/np.linalg.norm(df(xr)) # error global relativo para aprox. regresiva
ErrorG_c = np.linalg.norm((df(xc)-df_c))/np.linalg.norm(df(xc)) # error global relativo para aprox. centrada
print("h = ",h)   # escribimos en pantalla los errores 
print("ErrorG_p = ",ErrorG_p) 
print("ErrorG_r = ",ErrorG_r)
print("ErrorG_c = ",ErrorG_c)

#---------------------------------------------------------------
# h = 0.01
#---------------------------------------------------------------

h = 0.01     # paso

# Gráfica de la derivada
plt.close('all') # cerramos todas las ventanas

plt.figure(1)               
xx = np.linspace(0,1)             # definimos un vector x para dibujar la derivada en [0,1]
plt.plot(xx,df(xx),'--')   # dibujamos la derivada
plt.grid()

# Diferencias progresivas, regresivas y centradas
a = 0               # extremo inferior del intervalo
b = 1               # extremo superior del intervalo
x = np.arange(a,b+h,h)    # vector con 1º coordenada a, última coordenanda b y diferencia entre coordenadas h
df_p = np.diff(f(x))/h   # vector que contiene los valores de las diferencias progresivas
df_r = df_p                     # vector que contiene los valores de las diferencias regresivas
df_c = (df_p[1:] + df_r[0:-1])/2 # vector que contiene los valores de las diferencias centradas

# Gráfica de f' y de las diferencia progresivas, regresivas y centradas
xp = x[0:-1]    # vector con las coordenadas x para las diferencias progresivas
xr = x[1:]    # vector con las coordenadas x para las diferencias regresivas
xc = x[1:-1]    # vector con las coordenadas x para las diferencias centradas
plt.plot(xp,df_p,xr,df_r,xc,df_c)  # dibujamos las diferencias progresivas, regresivas y centradas
plt.legend(["df","df_p","df_r","df_c"]) # leyenda
plt.title("Derivada de f(x) = e^x y sus aproximaciones (h=0.1)") # título de la gráfica
plt.show()

## Gráfica de los errores en cada punto
plt.figure(2)  # abrimos una nueva figura
plt.plot(xp,abs(df(xp)-df_p),'o',xr,abs(df(xr)-df_r),'o',xc,abs(df(xc)-df_c),'o')    # dibujamos los valores |f'(x_i)-df_aprox(x_i)| para las 
# diferentes aproximaciones (progresiva, regresiva y centrada)
plt.grid() 
plt.legend(["df_p","df_r","df_c"]) # leyenda
plt.title("Errores (h=0.1)")    # título
plt.show()

## Errores globales relativos
ErrorG_p = np.linalg.norm((df(xp)-df_p))/np.linalg.norm(df(xp)) # error global relativo para aprox. progresiva
ErrorG_r = np.linalg.norm((df(xr)-df_r))/np.linalg.norm(df(xr)) # error global relativo para aprox. regresiva
ErrorG_c = np.linalg.norm((df(xc)-df_c))/np.linalg.norm(df(xc)) # error global relativo para aprox. centrada
print("h = ",h)   # escribimos en pantalla los errores 
print("ErrorG_p = ",ErrorG_p) 
print("ErrorG_r = ",ErrorG_r)
print("ErrorG_c = ",ErrorG_c)
 

