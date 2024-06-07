import numpy as np
import time
import matplotlib.pyplot as plt

def riemann_integral(f, a, b, N):
    width = (b - a) / N
    total_area = 0
    for i in range(N):
        total_area += f(a + i * width) * width
    return total_area

def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Hasil perhitungan, galat RMS, dan waktu eksekusi
results = []
errors = []
execution_times = []

for N in N_values:
    start_time = time.time()
    pi_estimate = riemann_integral(f, 0, 1, N)
    end_time = time.time()
    
    execution_time = end_time - start_time
    error = np.sqrt((pi_estimate - pi_reference)**2)
    
    results.append(pi_estimate)
    errors.append(error)
    execution_times.append(execution_time)

# Output hasil
print("N\t\tπ estimate\t\tError (RMS)\t\tExecution Time (s)")
for i, N in enumerate(N_values):
    print(f"{N}\t\t{results[i]:.15f}\t{errors[i]:.15f}\t{execution_times[i]:.8f}")

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(N_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Error (RMS, log scale)')
plt.title('Error vs N')

plt.subplot(1, 2, 2)
plt.plot(N_values, execution_times, marker='o')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs N')

plt.tight_layout()
plt.show()
