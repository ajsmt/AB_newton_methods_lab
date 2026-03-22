import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

root_names = ['x = 3 (кратный)', 'x = -0.5 + 0.866i', 'x = -0.5 - 0.866i']
colors = ['blue', 'green', 'orange']

plt.figure(figsize=(8, 6))

for i in range(3):
    # Используем файлы модифицированного метода
    filename = f'mod_first_root_{i}.txt'
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден, пропускаем.")
        continue

    # Загрузка данных (пропускаем заголовок)
    df = pd.read_csv(filename, names=['k', 'Error'], skiprows=1)
    e = df['Error'].values
    e = e[e > 0] # Исключаем нулевые значения для логарифмирования

    # Формируем пары (ошибка на текущем шаге, ошибка на следующем)
    x = np.log10(e[:-1])
    y = np.log10(e[1:])

    # Линейная регрессия: наклон прямой m и есть искомый порядок p
    m, b = np.polyfit(x, y, 1)

    # Отрисовка точек и аппроксимирующей прямой
    plt.scatter(x, y, color=colors[i], label=f'{root_names[i]} (p≈{m:.2f})')
    plt.plot(x, m*x + b, color=colors[i], linestyle='--')

plt.xlabel('log(e_k)')
plt.ylabel('log(e_{k+1})')
plt.title('Оценка порядка сходимости (Модифицированный метод)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()