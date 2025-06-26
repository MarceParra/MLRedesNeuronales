# ============================================================
# 🟠🍋 Generación aleatoria de puntos para clases de frutas
# Autor: Ing. Marcela Parra, Mg.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

def points_within_circle(radius, center=(0, 0), number_of_points=100):
    """
    Genera puntos aleatorios dentro de un círculo definido por:
    - radius: radio del círculo
    - center: centro del círculo (x, y)
    - number_of_points: cantidad de puntos a generar
    
    Retorna dos arrays con las coordenadas x e y de los puntos.
    """
    center_x, center_y = center
    r = radius * np.sqrt(np.random.random((number_of_points,)))  # Distribución radial uniforme
    theta = np.random.random((number_of_points,)) * 2 * np.pi   # Ángulos aleatorios en [0, 2pi]
    x = center_x + r * np.cos(theta)
    y = center_y + r * np.sin(theta)
    return x, y

# Crear figura y ejes para graficar
fig, ax = plt.subplots()

# Generar 100 puntos para cada clase dentro de círculos con diferente centro y radio
oranges_x, oranges_y = points_within_circle(1.6, center=(5, 2), number_of_points=100)  # Clase naranjas
lemons_x, lemons_y = points_within_circle(1.9, center=(2, 5), number_of_points=100)    # Clase limones

# Graficar los puntos generados
ax.scatter(oranges_x, oranges_y, c="orange", label="Naranjas")
ax.scatter(lemons_x, lemons_y, c="yellow", label="Limones")

# Graficar línea divisoria (ejemplo)
X = np.arange(0, 8)
ax.plot(X, 0.9 * X, "g-", linewidth=2, label="Línea divisoria")

# Configuración adicional del gráfico
ax.legend()
ax.grid(True)
ax.set_xlabel("Dulzura (sweetness)")
ax.set_ylabel("Acidez (sourness)")
ax.set_title("Generación aleatoria de clases de frutas en un espacio de características")

plt.show()