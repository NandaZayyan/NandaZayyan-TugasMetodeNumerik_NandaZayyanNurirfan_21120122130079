import numpy as np
import matplotlib.pyplot as plt

# Data tegangan (x) dan waktu patah (y)
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(xi, yi, x):
    def L(k, x):
        Lk = 1
        for i in range(len(xi)):
            if i != k:
                Lk *= (x - xi[i]) / (xi[k] - xi[i])
        return Lk

    return sum(yi[k] * L(k, x) for k in range(len(xi)))

# Range untuk plotting
x_plot = np.linspace(5, 40, 500)
y_plot_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_plot]

plt.plot(x_plot, y_plot_lagrange, label="Langrange Interpolation")
plt.scatter(x, y, color='red', label="Data Points")
plt.xlabel("Tegangan (kg/mm^2)")
plt.ylabel("Waktu Patah (jam)")
plt.title("Interpolasi Polinom Langrange")
plt.legend()
plt.show()

