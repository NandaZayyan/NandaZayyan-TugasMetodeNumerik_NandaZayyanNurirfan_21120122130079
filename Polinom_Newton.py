import numpy as np
import matplotlib.pyplot as plt

# Data tegangan (x) dan waktu patah (y)
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def divided_differences(xi, yi):
    n = len(yi)
    coef = np.zeros([n, n])
    coef[:,0] = yi

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (xi[i+j] - xi[i])
    
    return coef[0, :] 

def newton_interpolation(xi, yi, x):
    coef = divided_differences(xi, yi)
    n = len(coef)
    result = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - xi[j])
        result += term
    return result

x_plot = np.linspace(5, 40, 500)
y_plot_newton = [newton_interpolation(x, y, xi) for xi in x_plot]

plt.plot(x_plot, y_plot_newton, label="Newton Interpolation")
plt.scatter(x, y, color='red', label="Data Points")
plt.xlabel("Tegangan (kg/mm^2)")
plt.ylabel("Waktu Patah (jam)")
plt.title("Interpolasi Polinom Newton")
plt.legend()
plt.show()
