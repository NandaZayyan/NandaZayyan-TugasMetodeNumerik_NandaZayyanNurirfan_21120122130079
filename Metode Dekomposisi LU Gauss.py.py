import numpy as np

# Fungsi untuk mendekomposisi matriks A menjadi LU menggunakan metode Gauss
def lu_decomposition_gauss(A):
    n = len(A)
    A = A.astype(float)  # Konversi tipe data matriks A menjadi float64
    L = np.eye(n)
    U = A.copy()

    for i in range(n):
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            U[j] -= factor * U[i]

    return L, U

# Fungsi untuk mencari solusi menggunakan dekomposisi LU
def solve_using_lu(A, b):
    L, U = lu_decomposition_gauss(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

# Contoh soal
A = np.array([[2, 1, -1], [4, 1, 1], [1, -1, 3]], dtype=np.int32)  # Definisikan tipe data int32
b = np.array([8, 12, 6], dtype=np.int32)  # Definisikan tipe data int32

# Solusi menggunakan dekomposisi LU Gauss
x_lu = solve_using_lu(A, b)
print("Solusi menggunakan metode dekomposisi LU Gauss:")
print(x_lu)
