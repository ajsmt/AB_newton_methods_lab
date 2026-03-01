import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

root_names = ['x = 3 (кратный)', 'x = -0.5 + 0.866i', 'x = -0.5 - 0.866i']
colors = ['blue', 'green', 'orange']

plt.figure(figsize=(12, 8))

for i in range(3):
    filename = f'first_root_{i}.txt'
    
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден, пропускаем.")
        continue

    df = pd.read_csv(filename, sep=',', header=0, names=['k', 'Error'], skipinitialspace=True)

    df = df[df['Error'] > 0]

    k_data = df['k'].values
    error_data = df['Error'].values

    log_error = np.log10(error_data)
    m, b = np.polyfit(k_data, log_error, 1)

    k_fit = np.linspace(k_data.min(), k_data.max(), 100)
    error_fit = 10**(m * k_fit + b)

    plt.scatter(k_data, error_data, color=colors[i], label=f'Данные: {root_names[i]}', s=40, zorder=5)
    
    plt.plot(k_fit, error_fit, color=colors[i], linestyle='--', alpha=0.6, 
             label=f'Аппроксимация {i} (наклон: {m:.2f})')

plt.yscale('log')
plt.title('Диаграмма сходимости метода Ньютона', fontsize=16)
plt.xlabel('Номер итерации (k)', fontsize=12)
plt.ylabel('Погрешность |xk - x*|', fontsize=12)

plt.grid(True, which="both", linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()