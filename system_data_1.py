import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Файл для случая касания (один корень)
filename = 'system_6.363961_1.txt'

if not os.path.exists(filename):
    raise FileNotFoundError(f'Файл {filename} не найден')

# Загружаем данные
df = pd.read_csv(filename, sep=',', skipinitialspace=True)
df.columns = ['k', 'error'] # Нормализуем имена колонок

# Ошибка (невязка ||f(xk)||)
e = df['error'].values
e = e[e > 1e-15] # Убираем машинный ноль

plt.figure(figsize=(8, 6))

# Формируем пары (ошибка на текущем шаге, ошибка на следующем)
x = np.log10(e[:-1])
y = np.log10(e[1:])

# Вычисляем порядок сходимости p через линейную регрессию
p, b = np.polyfit(x, y, 1)

# Отрисовка точек и линии регрессии
plt.scatter(x, y, color='blue', label=f'Данные для c ≈ 6.36 (p ≈ {p:.2f})')
plt.plot(x, p*x + b, color='blue', linestyle='--', alpha=0.7)

plt.xlabel('log(||f(x_k)||)')
plt.ylabel('log(||f(x_{k+1})||)')
plt.title('Диаграмма сходимости метода Ньютона')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()