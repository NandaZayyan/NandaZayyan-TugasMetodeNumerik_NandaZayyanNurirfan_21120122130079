import numpy as np

# Fungsi untuk mendekomposisi matriks A menjadi LU menggunakan metode Crout
def lu_decomposition_crout(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            sum_ = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum_
        for j in range(i+1, n):
            sum_ = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - sum_) / U[i][i]

    return L, U

# Fungsi untuk menyelesaikan problem menggunakan dekomposisi LU Crout
def solve_using_lu_crout(A, b):
    L, U = lu_decomposition_crout(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

# Contoh soal
A = np.array([[2, 1, -1], [4, 1, 1], [1, -1, 3]])
b = np.array([8, 12, 6])

# Solusi menggunakan dekomposisi LU Crout
x_lu_crout = solve_using_lu_crout(A, b)
print("Solusi menggunakan metode dekomposisi Crout:")
print(x_lu_crout)
