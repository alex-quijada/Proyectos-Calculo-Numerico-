# Alexandra Quijada 27985694

from sympy import *
from math import * 

def bisec(fun,xa,xb):
  xr = (xa + xb) / 2                            
  fxr = fun(xr)                                   
  fxa = fun(xa)                                   
  tvi = fxa * fxr                               

  if tvi > 0:                                  
    xa = xr
  else:
    xb = xr

  return [xa,xb,xr]

def biseccion(fun,xa,xb,p):
  print("-------------------------------------------------")
  print("Algoritmo de biseccion")
  print("Acotaciones [", xa, ",", xb,"]")
  print("Margen de error del ", p, "%")
  print("------------------------------------------------- \n")
  i = 1
  print("Iteracion ", i, ":")
  print("xa =", xa)
  print("xb =", xb)
  erp = 100       
  auxiliar = bisec(fun,xa,xb)
  xa = auxiliar[0]
  xb = auxiliar[1]
  xr = auxiliar[2]
  print("xr (actual) =", xr)
  print()

  while erp > p:
    i = i + 1
    print("Iteracion ", i, ":")
    xra = xr
    auxiliar = bisec(fun,xa,xb)
    xa = auxiliar[0]
    xb = auxiliar[1]
    xr = auxiliar[2]
    print("Valor actual =", xr)

    erp = abs(200 - abs((xr + xra) / xr * 100))    
    print("error en porcentaje =", "{:.2f}".format(erp),"%")
    print()
  
  print("-------------------------------------------------")
  print("El valor ", xr, "es favorable con un margen de error de", erp, "% lo que es un porcentaje del", p, "%")
  print("-------------------------------------------------")

#Ejemplo de Uso 
fun = lambda x : (x**2) + (9*(x**3)) - 6
biseccion(fun,0,4,1)