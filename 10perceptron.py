# ============================================================
# 🟠🍋 Perceptrón Simple para Clasificar Naranjas y Limones
# Autor: Ing. Marcela Parra, Mg.
# ============================================================

import numpy as np  # Importa la librería NumPy para cálculos numéricos
from collections import Counter  # Importa Counter para contar clasificaciones

def points_within_circle(radius, center=(0, 0), number_of_points=100):
    # Genera puntos aleatorios dentro de un círculo
    cx, cy = center  # Coordenadas del centro
    r = radius * np.sqrt(np.random.random(number_of_points))  # Distancias radiales aleatorias
    theta = np.random.random(number_of_points) * 2 * np.pi  # Ángulos aleatorios
    x = cx + r * np.cos(theta)  # Coordenadas x
    y = cy + r * np.sin(theta)  # Coordenadas y
    return x, y  # Devuelve los puntos

# Genera 100 naranjas cerca del punto (8, 2)
oranges_x, oranges_y = points_within_circle(2.5, center=(8, 2), number_of_points=100)

# Genera 100 limones cerca del punto (2, 9)
lemons_x, lemons_y = points_within_circle(2.5, center=(2, 9), number_of_points=100)

class Perceptron:
    def __init__(self, weights):
        # Inicializa el perceptrón con una lista de pesos
        self.weights = np.array(weights)  # Guarda los pesos como array NumPy

    def __call__(self, in_data):
        # Permite usar el perceptrón como función
        weighted_input = self.weights * in_data  # Multiplica entradas por pesos
        weighted_sum = weighted_input.sum()  # Suma los valores ponderados
        return weighted_sum  # Devuelve el resultado

# Crea un perceptrón con pesos manuales: dulzura -0.45, acidez 0.5
p = Perceptron(weights=[-0.45, 0.5])

# Imprime resultados para las primeras 10 naranjas
print("🟠 Salidas para las primeras 10 naranjas:")
for point in zip(oranges_x[:10], oranges_y[:10]):  # Combina pares (x, y)
    res = p(point)  # Evalúa con el perceptrón
    print(f"{res:.3f}", end=", ")  # Muestra el resultado

print("\n\n🍋 Salidas para las primeras 10 limones:")
for point in zip(lemons_x[:10], lemons_y[:10]):  # Lo mismo para limones
    res = p(point)
    print(f"{res:.3f}", end=", ")

# Crea un contador para clasificaciones correctas e incorrectas
evaluation = Counter()

# Clasifica todas las naranjas (esperamos que res < 0)
for point in zip(oranges_x, oranges_y):
    res = p(point)
    if res < 0:
        evaluation['correctas'] += 1  # Clasificación correcta
    else:
        evaluation['incorrectas'] += 1  # Clasificación incorrecta

# Clasifica todos los limones (esperamos que res >= 0)
for point in zip(lemons_x, lemons_y):
    res = p(point)
    if res >= 0:
        evaluation['correctas'] += 1
    else:
        evaluation['incorrectas'] += 1

# Imprime el resumen de resultados
print("\n\n📊 Evaluación de clasificación:")
print(f"Frutas correctamente clasificadas: {evaluation['correctas']}")
print(f"Frutas incorrectamente clasificadas: {evaluation['incorrectas']}")
