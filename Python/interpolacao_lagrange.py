import sympy as sp

def lagrange_polynomial(x_points, y_points):
    """
    Função para calcular o polinômio de interpolação usando o método de Lagrange.

    Parâmetros:
    x_points: Lista de pontos x conhecidos.
    y_points: Lista de pontos y correspondentes aos pontos x.

    Retorna:
    polinomio: Polinômio simbólico que interpola os pontos fornecidos.
    """
    x = sp.symbols('x')  # Define o símbolo x para o polinômio
    n = len(x_points)    # Número de pontos
    polinomio = 0        # Inicializa o polinômio interpolador

    for i in range(n):
        # Calcula o termo L_i(x) para o polinômio de Lagrange
        termo = y_points[i]
        for j in range(n):
            if i != j:
                termo *= (x - x_points[j]) / (x_points[i] - x_points[j])
        polinomio += termo

    # Simplifica o polinômio para obter uma forma expandida
    polinomio = sp.expand(polinomio)
    return polinomio

# Parâmetros dos pontos
x_points = [3, 2, 1]
y_points = [20, 12, 6]

polinomio_interpolador = lagrange_polynomial(x_points, y_points)
print(f"O polinômio interpolador é: {polinomio_interpolador}")