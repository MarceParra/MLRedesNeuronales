# ============================================================
# 🟠🍋 Visualización de la Línea Divisoria entre Naranjas y Limones usando Perceptrón
# Autor: Ing. Marcela Parra, Mg.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

def points_within_circle(radius, center=(0, 0), number_of_points=100):
    """
    Genera puntos aleatorios distribuidos dentro de un círculo.
    
    Parámetros:
    - radius: radio del círculo
    - center: (x, y) coordenadas del centro del círculo
    - number_of_points: cantidad de puntos a generar
    
    Retorna:
    - x, y: arrays con las coordenadas de los puntos generados
    """
    cx, cy = center
    # Generar radios aleatorios con distribución uniforme dentro del círculo
    r = radius * np.sqrt(np.random.random(number_of_points))
    # Generar ángulos aleatorios entre 0 y 2π
    theta = np.random.random(number_of_points) * 2 * np.pi
    # Calcular coordenadas x e y
    x = cx + r * np.cos(theta)
    y = cy + r * np.sin(theta)
    return x, y

# Generar puntos para naranjas y limones con centros y radios diferentes para separarlos mejor
oranges_x, oranges_y = points_within_circle(2.5, center=(8, 2), number_of_points=100)
lemons_x, lemons_y = points_within_circle(2.5, center=(2, 9), number_of_points=100)

# Crear figura y eje para graficar
fig, ax = plt.subplots()

# Graficar los puntos de las naranjas en color naranja
ax.scatter(oranges_x, oranges_y, c="orange", label="Naranjas")

# Graficar los puntos de los limones en color amarillo
ax.scatter(lemons_x, lemons_y, c="yellow", label="Limones")

# Definir rango para la línea divisoria en el eje x
X = np.arange(0, 12)

# Calcular la pendiente (m) usando los pesos del perceptrón (w1=0.45, w2=0.5)
# La pendiente es m = w1 / w2
slope = 0.45 / 0.5

# Graficar la línea divisoria que separa ambas clases
ax.plot(X, slope * X, color="green", linewidth=2, label="Línea divisoria")

# Configurar leyenda, etiquetas y cuadrícula
ax.legend()
ax.set_xlabel("Dulzura (x1)")
ax.set_ylabel("Acidez (x2)")
ax.set_title("Línea Divisoria entre Naranjas y Limones usando Perceptrón")
ax.grid(True)

# Mostrar el gráfico
plt.show()

# Imprimir la pendiente calculada para referencia
print(f"Pendiente calculada (slope): {slope:.3f}")
