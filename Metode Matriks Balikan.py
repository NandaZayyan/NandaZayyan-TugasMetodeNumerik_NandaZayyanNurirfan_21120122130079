import numpy as np

# Fungsi untuk menyelesaikan problem menggunakan metode matriks balikan
def solve_using_inverse(A, b):
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    return x

# Contoh soal
A = np.array([[2, 1, -1], [4, 1, 1], [1, -1, 3]])
b = np.array([8, 12, 6])

# Solusi menggunakan metode matriks balikan
x_inv = solve_using_inverse(A, b)
print("Solusi menggunakan metode matriks balikan:")
print(x_inv)
