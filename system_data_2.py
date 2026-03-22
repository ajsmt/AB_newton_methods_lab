import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Файлы для случая пересечения (два корня)
files = [
    'system_7.000000_1.txt',
    'system_7.000000_2.txt'
]
colors = ['blue', 'green']

plt.figure(figsize=(8, 6))

for i, filename in enumerate(files, start=1):
    if not os.path.exists(filename):
        print(f'Файл {filename} не найден, пропускаем.')
        continue

    # Чтение данных
    df = pd.read_csv(filename, sep=',', skipinitialspace=True)
    df.columns = ['k', 'error']
    
    # Невязка системы
    e = df['error'].values
    e = e[e > 1e-15] # Отсекаем шум

    if len(e) < 2:
        continue

    # Подготовка данных для оценки порядка p
    x = np.log10(e[:-1])
    y = np.log10(e[1:])

    # Регрессия для вычисления наклона (порядка p)
    p, b = np.polyfit(x, y, 1)

    # Отрисовка
    plt.scatter(x, y, color=colors[i-1], label=f'Корень {i} (p ≈ {p:.2f})')
    plt.plot(x, p*x + b, color=colors[i-1], linestyle='--')

plt.xlabel('log(||f(x_k)||)')
plt.ylabel('log(||f(x_{k+1})||)')
plt.title('Диаграммы сходимости метода Ньютона (c = 7)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()