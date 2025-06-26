# ============================================================
# Separación de clases con línea recta - Ejemplo simple
# Autor: Ing. Marce Parra
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

# Valores para el eje X (de 0 a 6)
X = np.arange(0, 7)

# Crear figura y ejes para graficar
fig, ax = plt.subplots()

# Punto 1: naranja (dulzura=3.5, acidez=1.8)
ax.plot(3.5, 1.8, "o", color="darkorange", markersize=15, label="Naranja")

# Punto 2: limón (dulzura=1.1, acidez=3.9)
ax.plot(1.1, 3.9, "o", color="yellow", markersize=15, label="Limón")

# Punto que define la pendiente (ejemplo: (4, 4.5))
point_on_line = (4, 4.5)

# Calcular pendiente m = y / x usando el punto sobre la línea
m = point_on_line[1] / point_on_line[0]

# Graficar línea verde: y = m * x
ax.plot(X, m * X, "g-", linewidth=3, label=f"Línea: y = {m:.2f}x")

# Añadir etiquetas y leyenda
ax.set_xlabel("Dulzura")
ax.set_ylabel("Acidez")
ax.legend()

# Título del gráfico
ax.set_title("Separación de clases con línea recta")

# Mostrar gráfico
plt.show()
