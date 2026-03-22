import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

root_names = ['x = 3 (кратный)', 'x = -0.5 + 0.866i', 'x = -0.5 - 0.866i']
colors = ['blue', 'green', 'orange']

plt.figure(figsize=(8, 6))

for i in range(3):
    filename = f'first_root_{i}.txt'
    if not os.path.exists(filename):
        continue

    df = pd.read_csv(filename, names=['k', 'Error'], skiprows=1)
    e = df['Error'].values
    e = e[e > 0]

    x = np.log10(e[:-1])
    y = np.log10(e[1:])

    m, b = np.polyfit(x, y, 1)

    plt.scatter(x, y, color=colors[i], label=f'{root_names[i]} (p≈{m:.2f})')
    plt.plot(x, m*x + b, color=colors[i], linestyle='--')

plt.xlabel('log(e_k)')
plt.ylabel('log(e_{k+1})')
plt.title('Оценка порядка сходимости')
plt.grid(True)
plt.legend()
plt.show()