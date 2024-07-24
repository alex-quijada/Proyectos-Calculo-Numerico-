# Alexandra Quijada 27985694

import math as mt

def rieman(f, a, b, n):
    
    h = (b - a) / n
    sum = 0
    x = a
    for i in range(n):
        sum += f(x) * h
        x += h
    return sum

def trapecio(f, a, b, n):

    h = (b - a) / n
    sum = 0
    x = a
    for i in range(n):
        sum += (f(x) + f(x + h)) * h / 2
        x += h
    return sum

def calcular_integral(metodo, f, a, b, n):
  
    if metodo == 'rieman':
        return rieman(f, a, b, n)
    elif metodo == 'trapecio':
        return trapecio(f, a, b, n)
    else:
        raise ValueError("Método no reconocido. Use 'rieman' o 'trapecio'.")

if __name__ == "__main__":
    f = lambda x: x * (((x**2) + 1)**0.5)
    a, b = 1, 2
    n = 4

    metodo = 'rieman'
    riemann_result = calcular_integral(metodo, f, a, b, n)
    metodo = 'trapecio'
    trapecio_result = calcular_integral(metodo, f, a, b, n)

    print(f"\nIntegración usando la regla de Riemann:")
    print(f"Función: f(x) = x * sqrt(x^2 + 1)")
    print(f"Intervalo: [{a}, {b}] con {n} subdivisiones")
    print(f"Resultado: {riemann_result:.6f}\n")

    print(f"Integración usando la regla del trapecio:")
    print(f"Función: f(x) = x * sqrt(x^2 + 1)")
    print(f"Intervalo: [{a}, {b}] con {n} subdivisiones")
    print(f"Resultado: {trapecio_result:.6f}")
