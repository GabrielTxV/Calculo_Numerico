import numpy as np

def lu_decomposition(A):
    n = A.shape[0]
    L = np.eye(n, dtype=np.float64)
    U = A.copy()
    P = np.eye(n, dtype=np.float64)

    for i in range(n):
        # Pivoteamento parcial
        max_row = np.argmax(abs(U[i:, i])) + i
        if i != max_row:
            # Troca as linhas em U, L e P
            U[[i, max_row]] = U[[max_row, i]]
            P[[i, max_row]] = P[[max_row, i]]
            if i > 0:
                L[[i, max_row], :i] = L[[max_row, i], :i]
        
        # Eliminação para construir L e U
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    
    return P, L, U

def lu_solve(A, b):
    # Decomposição LU com pivoteamento parcial
    P, L, U = lu_decomposition(A)
    
    # Exibe as matrizes P, L e U
    print("Matriz P (permutação):")
    print(P)
    print("\nMatriz L (triangular inferior):")
    print(L)
    print("\nMatriz U (triangular superior):")
    print(U)
    
    # Calcula Pb (b ajustado pela permutação P)
    Pb = np.dot(P, b)
    
    # Resolve Ly = Pb usando substituição para frente
    y = np.zeros_like(b, dtype=np.float64)
    for i in range(len(b)):
        y[i] = Pb[i] - np.dot(L[i, :i], y[:i])

    # Resolve Ux = y usando substituição para trás
    x = np.zeros_like(b, dtype=np.float64)
    for i in range(len(b) - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    
    return x

# Matrizes A e b do sistema
A = np.array([[5, 7, 7], [2.5, 3.5, 5.5], [10, 4, 6]], dtype=np.float64)
b = np.array([12, 12, 20], dtype=np.float64)

# Resolve o sistema usando fatoração LU com pivoteamento manual
x = lu_solve(A, b)

# Exibe a solução encontrada
print("\nSolução do sistema Ax = b:")
print(x)

# Validação do resultado
Ax = np.dot(A, x)
print("\nProduto Ax:")
print(Ax)
print("\nVetor b:")
print(b)

# Verifica se Ax é aproximadamente igual a b
if np.allclose(Ax, b):
    print("\nA solução está correta dentro da tolerância numérica.")
else:
    print("\nA solução não está correta. Pode haver instabilidade numérica.")
