# ============================================================
# 🟠🍋 Visualización de líneas separadoras para frutas
# Autor: Ing. Marcela Parra, Mg.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

def create_distance_function(a, b, c):
    """
    Crea una función para calcular la distancia y posición relativa
    de un punto respecto a la línea definida por: 0 = a*x + b*y + c
    
    Retorna una función que recibe coordenadas (x, y) y devuelve:
    - distancia absoluta al línea
    - posición relativa:
        -1 si el punto está debajo de la línea
         0 si el punto está sobre la línea
        +1 si el punto está encima de la línea
    """
    def distance(x, y):
        nom = a * x + b * y + c
        if nom == 0:
            pos = 0
        elif (nom < 0 and b < 0) or (nom > 0 and b > 0):
            pos = -1
        else:
            pos = 1
        dist = np.abs(nom) / np.sqrt(a**2 + b**2)
        return dist, pos
    return distance

# Coordenadas de las frutas: (dulzura, acidez)
orange = (4.5, 1.8)  # naranja
lemon = (1.1, 3.9)   # limón
fruits_coords = [orange, lemon]

# Configuración del gráfico
fig, ax = plt.subplots()
ax.set_xlabel("Dulzura (sweetness)")
ax.set_ylabel("Acidez (sourness)")
x_min, x_max = -1, 7
y_min, y_max = -1, 8
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])

X = np.arange(x_min, x_max, 0.1)

# Dibujar varias líneas que pasan por el origen con diferentes pendientes
step = 0.05
for x in np.arange(0, 1 + step, step):
    slope = np.tan(np.arccos(x))  # Calcula la pendiente de la línea
    dist4line = create_distance_function(slope, -1, 0)  # Línea: y = slope * x -> ax + by + c = 0 => a=slope, b=-1, c=0
    Y = slope * X

    # Evaluar en qué lado de la línea están las frutas
    results = []
    for point in fruits_coords:
        results.append(dist4line(*point))

    # Si están en lados opuestos, línea verde, sino roja
    if results[0][1] != results[1][1]:
        ax.plot(X, Y, "g-", linewidth=0.8, alpha=0.9)  # Línea verde separadora
    else:
        ax.plot(X, Y, "r-", linewidth=0.8, alpha=0.9)  # Línea roja no separadora

# Graficar frutas
size = 10
for (index, (x, y)) in enumerate(fruits_coords):
    if index == 0:
        ax.plot(x, y, "o", color="darkorange", markersize=size, label="Naranja")
    else:
        ax.plot(x, y, "oy", markersize=size, label="Limón")

ax.legend()
plt.title("Líneas separadoras entre frutas por posición relativa")
plt.show()
