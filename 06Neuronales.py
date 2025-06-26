# ============================================================
# 🟠🍋 Verificar posición de frutas respecto a una línea recta
# Autor: Ing. Marce Parra
# ============================================================

# Coordenadas de las frutas
lemon = (1.1, 3.9)     # limón (más ácido)
orange = (3.5, 1.8)    # naranja (más dulce)

# Definir un punto sobre la línea para calcular la pendiente
punto_sobre_linea = (4, 4.5)

# Calcular la pendiente de la línea (m = y / x)
m = punto_sobre_linea[1] / punto_sobre_linea[0]  # m = 4.5 / 4 = 1.125

print(f"Pendiente m = {m:.3f}")

# Evaluar si la naranja está debajo de la línea
resultado_naranja = orange[0] * m - orange[1]
print(f"\nResultado para naranja: {resultado_naranja:.3f}")
if resultado_naranja > 0:
    print("🟠 La naranja está DEBAJO de la línea.")
else:
    print("🟠 La naranja está ENCIMA de la línea.")

# Evaluar si el limón está arriba de la línea
resultado_limon = lemon[0] * m - lemon[1]
print(f"\nResultado para limón: {resultado_limon:.3f}")
if resultado_limon > 0:
    print("🍋 El limón está DEBAJO de la línea.")
else:
    print("🍋 El limón está ENCIMA de la línea.")
