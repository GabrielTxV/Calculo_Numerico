import numpy as np

def newton_interpolation(x_points, y_points):
    """
    Função para calcular o polinômio de interpolação usando o método de Newton.

    Parâmetros:
    x_points: Lista de pontos x conhecidos.
    y_points: Lista de pontos y correspondentes aos pontos x.

    Retorna:
    polinomio: Polinômio que interpola os pontos fornecidos.
    """
    n = len(x_points)
    coef = np.zeros([n, n])
    coef[:,0] = y_points

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_points[i+j] - x_points[i])

    def newton_poly(x):
        result = coef[0, 0]
        for i in range(1, n):
            term = coef[0, i]
            for j in range(i):
                term *= (x - x_points[j])
            result += term
        return result

    return newton_poly

# Parâmetros dos pontos
x_points = [3, 2, 1]
y_points = [20, 12, 6]

polinomio_interpolador = newton_interpolation(x_points, y_points)

# Imprimir o polinômio interpolador em forma simbólica
import sympy as sp
x = sp.symbols('x')
polinomio_simb = polinomio_interpolador(x)
print(f"O polinômio interpolador é: {sp.expand(polinomio_simb)}")