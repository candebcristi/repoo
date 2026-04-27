#tareita numérica

#librerías
import numpy as np
import matplotlib.pyplot as plt

#constantes
n= 15 #Cantidad peces
r= 0.25 #Tasa crecimiento
Eo = 0.1 #Esfuerzo pesquero
k= 30 #Capacidad límite
q= 0.001 #Capturabilidad
dt= 1. #paso temporal
dias = 5
horas = 24*dias
pobl_init = 2
c1 = 1-((pobl_init*r)/(k*(r-q*Eo)))

N = int(horas/dt)


t1 = np.linspace(0, horas, N+1)

#modelo explotación pesquera
def n(t):
  numerador = k*(r-q*Eo)
  expon = (np.exp((-1)*(r-q*Eo)*t))
  #print(expon)
  denominador = (r)+(k*(r-q*Eo)*c1*expon)
  #print(denominador)
  #print(expon)
  n_evaluado = ((numerador))/((denominador))
  #print(n_evaluado)
  return n_evaluado

#Gráfico
plt.figure(figsize=(7,5))
plt.plot(t1, n(t1))
plt.xlabel("Tiempo (horas)")
plt.ylabel("Cantidad de peces (cantidad de individuos)")
plt.title("Cantidad de peces en el tiempo")
plt.show()