# ============================================================
# 🟠🍋 Clasificación Mejorada: Separación de Naranjas y Limones
# Autor: Ing. Marcela Parra, Mg.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from itertools import repeat
from random import shuffle

def points_within_circle(radius, center=(0, 0), number_of_points=100):
    """
    Genera puntos aleatorios distribuidos uniformemente dentro de un círculo.

    Parámetros:
    - radius: radio del círculo
    - center: tupla (x, y) con el centro del círculo
    - number_of_points: cantidad de puntos a generar

    Retorna:
    - x, y: arrays con las coordenadas de los puntos generados
    """
    cx, cy = center
    r = radius * np.sqrt(np.random.random(number_of_points))
    theta = np.random.random(number_of_points) * 2 * np.pi
    x = cx + r * np.cos(theta)
    y = cy + r * np.sin(theta)
    return x, y

# Aumentar la dispersión y separación para mejor clasificación visual
oranges_x, oranges_y = points_within_circle(2.5, center=(8, 2), number_of_points=100)  # Naranjas más a la derecha
lemons_x, lemons_y = points_within_circle(2.5, center=(2, 9), number_of_points=100)   # Limones más arriba

# Crear la figura y ajustar tamaño para mejor visibilidad
fig, ax = plt.subplots(figsize=(10, 7))

# Graficar los puntos con color y borde para mejor distinción
ax.scatter(oranges_x, oranges_y, c="orange", label="Naranjas", alpha=0.7, edgecolors='k')
ax.scatter(lemons_x, lemons_y, c="yellow", label="Limones", alpha=0.7, edgecolors='k')

# Crear lista de frutas con etiquetas (0: naranja, 1: limón)
fruits = list(zip(oranges_x, oranges_y, repeat(0, len(oranges_x))))
fruits += list(zip(lemons_x, lemons_y, repeat(1, len(lemons_x))))
shuffle(fruits)  # Mezclar puntos para evitar sesgo

def perceptron_line_fit(fruits, learning_rate=0.01, max_iter=1000):
    """
    Ajusta una línea divisoria usando el algoritmo perceptrón simple.

    Parámetros:
    - fruits: lista de tuplas (x, y, etiqueta)
    - learning_rate: tamaño del paso para actualización de parámetros
    - max_iter: máximo de iteraciones para entrenamiento

    Retorna:
    - slope: pendiente final de la línea
    - intercept: intercepto final de la línea
    """
    slope = 0.0
    intercept = 0.0

    for iteration in range(max_iter):
        errors = 0
        for x, y, label in fruits:
            y_pred = slope * x + intercept

            # Para naranjas (0), queremos que y_pred < y (punto debajo de línea)
            if label == 0 and y_pred >= y:
                slope -= learning_rate * x
                intercept -= learning_rate
                errors += 1

            # Para limones (1), queremos que y_pred > y (punto arriba de línea)
            elif label == 1 and y_pred <= y:
                slope += learning_rate * x
                intercept += learning_rate
                errors += 1

        if errors == 0:
            print(f"Entrenamiento completo en {iteration + 1} iteraciones.")
            break
    else:
        print(f"Máximo de iteraciones ({max_iter}) alcanzado con {errors} errores.")

    return slope, intercept

# Ejecutar ajuste del perceptrón
slope, intercept = perceptron_line_fit(fruits, learning_rate=0.01, max_iter=1000)

# Definir rango para dibujar la línea divisoria
X_range = np.linspace(0, 12, 200)
y_line = slope * X_range + intercept

# Graficar línea divisoria final en verde, con grosor destacado
ax.plot(X_range, y_line, color="green", linewidth=3, label="Línea divisoria final")

# Ajustes finales al gráfico para mejor presentación
ax.legend(fontsize=12)
ax.grid(True)
plt.xlabel("Dulzura (sweetness)", fontsize=14)
plt.ylabel("Acidez (sourness)", fontsize=14)
plt.title("Separación clara de Naranjas y Limones con Línea Divisoria Ajustada", fontsize=16)

plt.show()

# Mostrar pendiente e intercepto finales en consola
print(f"Pendiente final: {slope:.3f}")
print(f"Intercepto final: {intercept:.3f}")
