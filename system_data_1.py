import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

filename = 'system_6.363961_1.txt'

if not os.path.exists(filename):
    raise FileNotFoundError(f'Файл {filename} не найден')

df = pd.read_csv(filename, sep=',', skipinitialspace=True)

# FIX: нормализуем имена столбцов
df.columns = ['k', 'error']

# убираем нули и отрицательные значения
df = df[df['error'] > 0]

k = df['k'].values
error = df['error'].values

plt.figure(figsize=(8, 6))
plt.semilogy(k, error, marker='o', linewidth=2)

plt.xlabel('Номер итерации k')
plt.ylabel(r'$\|f(x_k)\|$')
plt.title('Диаграмма сходимости метода Ньютона')

plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()