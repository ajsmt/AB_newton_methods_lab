import pandas as pd
import matplotlib.pyplot as plt
import os

files = [
    'system_7.000000_1.txt',
    'system_7.000000_2.txt'
]

plt.figure(figsize=(8, 6))

for i, filename in enumerate(files, start=1):
    if not os.path.exists(filename):
        print(f'Файл {filename} не найден, пропускаем.')
        continue

    df = pd.read_csv(filename, sep=',', skipinitialspace=True)

    df.columns = ['k', 'error']

    df = df[df['error'] > 0]

    plt.semilogy(
        df['k'],
        df['error'],
        marker='o',
        linewidth=2,
        label=f'Корень {i}'
    )

plt.xlabel('Номер итерации k', fontsize=12)
plt.ylabel(r'$\|f(x_k)\|$', fontsize=12)
plt.title('Диаграммы сходимости метода Ньютона (c = 7)', fontsize=14)

plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()