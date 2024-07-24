# Alexandra Quijada 27985694

import math as m
import numpy as np

def newton_raphson(x0, tolerancia, fx, dfx):
    
    tabla = []
    tramo = abs(2 * tolerancia)
    xi = x0
    
    while tramo >= tolerancia:
        xnuevo = xi - fx(xi) / dfx(xi)
        tramo = abs(xnuevo - xi)
        tabla.append([xi, xnuevo, tramo])
        xi = xnuevo

    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    # Retorno una tupla con toda la información necesaria
    return (xi, tramo, tabla)

# SALIDA
def salida_newton_raphson(tupla):

    # Tupla Parametros: Tupla con la raíz encontrada, el error y una tabla de iteraciones.
    
    print(f"{'Iter':<5}{'xi':<12}{'xnuevo':<12}{'tramo':<12}")
    np.set_printoptions(precision=4)
    
    for i, row in enumerate(tupla[2]):
        print(f"{i+1:<5}{row[0]:<12.6f}{row[1]:<12.6f}{row[2]:<12.6f}")
    
    print(f"\n La Raíz encontrada es: {tupla[0]:.10f}")
    print(f"Con error del margen: {tupla[1]:.10f}")

if __name__ == "__main__":
    # Definición de las funciones
    dfx = lambda x: -2 * x * (m.e ** (-x ** 2)) - 2
    fx = lambda x: (m.e ** (-x ** 2)) - 2 * x + 1
   
    # Ejecución del método de Newton-Raphson
    Z = newton_raphson(0.80, 0.02, fx, dfx)
    salida_newton_raphson(Z)
   
    Y = newton_raphson(2, 0.001, fx, dfx)
    salida_newton_raphson(Y)
