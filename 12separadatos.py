# ============================================================
# 🟠🍋 Perceptrón Simple para Clasificar Naranjas y Limones
# Autor: Ing. Marcela Parra, Mg.
# ============================================================

import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from random import shuffle
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Función para generar puntos aleatorios dentro de un círculo.
# Cada punto tiene coordenadas x,y distribuidas uniformemente.
def points_within_circle(radius, center=(0, 0), number_of_points=100):
    cx, cy = center
    # Generar radios aleatorios con raíz cuadrada para distribución uniforme en área
    r = radius * np.sqrt(np.random.random(number_of_points))
    # Ángulo aleatorio entre 0 y 2π
    theta = np.random.random(number_of_points) * 2 * np.pi
    # Coordenadas x,y de los puntos generados
    x = cx + r * np.cos(theta)
    y = cy + r * np.sin(theta)
    return x, y

# Clase Perceptrón para clasificar puntos en dos categorías (naranjas y limones)
class Perceptron:
    # Inicializador con pesos iniciales y tasa de aprendizaje para ajustar pesos
    def __init__(self, weights, learning_rate=0.1):
        self.weights = np.array(weights)  # Pesos iniciales como array numpy
        self.learning_rate = learning_rate  # Factor para controlar velocidad de aprendizaje

    # Función escalón para decidir la salida final: 0 o 1 según el umbral cero
    @staticmethod
    def unit_step_function(x):
        return 0 if x < 0 else 1

    # Método que calcula la salida del perceptrón para un dato de entrada
    def __call__(self, in_data):
        # Producto elemento a elemento entre pesos y entradas
        weighted_sum = (self.weights * in_data).sum()  # Suma ponderada total
        return Perceptron.unit_step_function(weighted_sum)  # Salida binaria 0 o 1

    # Método para ajustar los pesos basado en el error entre salida esperada y calculada
    def adjust(self, target_result, calculated_result, in_data):
        # Convertir entrada a array si no lo es
        if not isinstance(in_data, np.ndarray):
            in_data = np.array(in_data)
        # Calcular error simple (target - calculado)
        error = target_result - calculated_result
        # Si hay error, corregir pesos
        if error != 0:
            correction = error * in_data * self.learning_rate  # Ajuste proporcional al error y entrada
            self.weights += correction  # Actualizar pesos sumando la corrección

    # Método para evaluar cuántos datos fueron clasificados correctamente
    def evaluate(self, data, labels):
        evaluation = Counter()
        for i in range(len(data)):
            label = int(round(self(data[i]), 0))  # Predecir etiqueta para cada dato
            if label == labels[i]:
                evaluation["correct"] += 1  # Contar aciertos
            else:
                evaluation["wrong"] += 1  # Contar errores
        total = evaluation["correct"] + evaluation["wrong"]
        accuracy = (evaluation["correct"] / total) * 100  # Calcular porcentaje de acierto
        print(f"Aciertos: {evaluation['correct']} de {total} ({accuracy:.2f}%)")
        return evaluation

# ------------------------------------------------------------
# Generar datos para naranjas y limones usando la función de puntos en círculo
oranges_x, oranges_y = points_within_circle(2.5, center=(8, 2), number_of_points=100)
lemons_x, lemons_y = points_within_circle(2.5, center=(2, 9), number_of_points=100)

# Combinar coordenadas en pares (x,y)
oranges = list(zip(oranges_x, oranges_y))
lemons = list(zip(lemons_x, lemons_y))

# Crear lista con datos etiquetados: 0 para naranja, 1 para limón
labelled_data = list(zip(oranges + lemons, [0] * len(oranges) + [1] * len(lemons)))
shuffle(labelled_data)  # Mezclar datos para aleatoriedad

# Separar datos y etiquetas en dos listas separadas
data, labels = zip(*labelled_data)

# Dividir datos en conjuntos de entrenamiento (80%) y prueba (20%)
train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, train_size=0.8, test_size=0.2, random_state=42)

# Crear instancia del perceptrón con pesos iniciales pequeños y tasa de aprendizaje
p = Perceptron(weights=[0.1, 0.1], learning_rate=0.3)

# Entrenamiento del perceptrón: ajustar pesos usando datos de entrenamiento
for i in range(len(train_data)):
    p.adjust(train_labels[i], p(train_data[i]), train_data[i])

# Evaluar el desempeño del modelo con datos de entrenamiento
print("Evaluación en datos de entrenamiento:")
p.evaluate(train_data, train_labels)

# Evaluar el desempeño con datos de prueba para validar generalización
print("\nEvaluación en datos de prueba:")
p.evaluate(test_data, test_labels)

# Mostrar los pesos finales luego del entrenamiento
print(f"\nPesos finales: {p.weights}")

# ------------------------------------------------------------
# Visualización de los datos y la frontera de decisión

X = np.arange(0, 10)  # Crear rango para eje X en gráfico

# Separar puntos de limones y naranjas para graficar con color distinto
lemons = [train_data[i] for i in range(len(train_data)) if train_labels[i] == 1]
lemons_x, lemons_y = zip(*lemons)
oranges = [train_data[i] for i in range(len(train_data)) if train_labels[i] == 0]
oranges_x, oranges_y = zip(*oranges)

fig, ax = plt.subplots()
# Graficar puntos de naranja en color naranja
ax.scatter(oranges_x, oranges_y, c="orange", label="Naranjas")
# Graficar puntos de limón en color amarillo
ax.scatter(lemons_x, lemons_y, c="yellow", label="Limones")

# Extraer pesos para calcular pendiente de la frontera de decisión
w1, w2 = p.weights
m = -w1 / w2  # Pendiente de la línea que separa clases

# Graficar línea de frontera de decisión
ax.plot(X, m * X, label="Frontera de decisión", linewidth=2)

# Añadir leyenda y etiquetas
ax.legend()
ax.set_title("Clasificación de Naranjas y Limones usando Perceptrón")
ax.set_xlabel("Característica 1")
ax.set_ylabel("Característica 2")
ax.grid(True)

# Mostrar gráfico
plt.show()