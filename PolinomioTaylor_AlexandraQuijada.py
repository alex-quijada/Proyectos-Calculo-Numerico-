# Alexandra Quijada 27985694

from sympy import symbols, diff, lambdify, factorial

def taylor(f, g, X0):
    x = symbols('x')
    f_sym = f(x)
    pol = f_sym.subs(x, X0)  # Evaluamos la función en X0 para el término independiente
    deriv = f_sym  # Inicializamos la derivada como la función original

    # Calculos para el polinomio de Taylor 
    for i in range(1, g + 1):
        deriv = diff(deriv, x)  # para sacar la i-ésima derivada
        deriv_at_X0 = deriv.subs(x, X0)  # Evaluamos la derivada en X0
        pol += (deriv_at_X0 / factorial(i)) * (x - X0)**i  # Añadimos el término al polinomio

    poly_func = lambdify(x, pol)
    return pol, poly_func

# Ejemplo de Uso
if __name__ == "__main__":
    f = lambda x: x**2 + 3*x**3 - 2
    X0 = 0 
    g = 4 

    pol, poly_func = taylor(f, g, X0)

    # Impresión del polinomio y valores
    print(f"\nEl polinomio de Taylor de orden {g} para la función dada en x = {X0} es:")
    print(f"P(x) = {pol}\n")
    print("Valores del polinomio de Taylor en algunos puntos:")
    print(f"{'x':>6} | {'P(x)':>10}")
    print("-" * 20)
    for x_val in [0, 0.5, 1]:
        print(f"{x_val:>6.2f} | {poly_func(x_val):>10.4f}")

