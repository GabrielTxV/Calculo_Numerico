import numpy as np

def gauss_pivot(A, b):
    n = len(b)
    # Concatena A e b em uma matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)])

    # Passo de eliminação com pivoteamento parcial
    for i in range(n):
        # Encontra a linha com o maior valor absoluto na coluna i
        max_row = np.argmax(abs(Ab[i:, i])) + i
        # Troca a linha atual com a linha max_row
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Realiza a eliminação Gaussiana
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Substituição para trás para resolver o sistema
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    
    return x

# Exemplo de uso
A = np.array([[5, 7, 7], [2.5, 3.5, 5.5], [10, 4, 6]], dtype=np.float64)
b = np.array([12, 12, 20], dtype=np.float64)

x = gauss_pivot(A, b)
print("Solução do sistema Ax = b:")
print(x)
