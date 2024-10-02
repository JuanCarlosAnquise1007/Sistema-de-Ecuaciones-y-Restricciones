import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

# Función para calcular el rendimiento total
def calcular_rendimiento(x):
    if x <= 0:
        return 0, 0  # Evitar división por cero
    n = 200 / x  # Calcular el número de lotes
    if n <= 10:
        rendimiento = n  # Sin reducción de rendimiento
    else:
        rendimiento = 10 * (1 - 0.1 * (n - 10))  # Aplicar reducción
    return n, rendimiento

# Función para actualizar los resultados y la gráfica
def actualizar_resultados():
    try:
        x = float(entry_tamaño_lote.get())
        if x <= 0:
            result_label.config(text="El tamaño del lote debe ser mayor que 0.")
            return
    except ValueError:
        result_label.config(text="Por favor, ingrese un valor numérico válido.")
        return

    # Calcular el número de lotes y rendimiento
    n, rendimiento = calcular_rendimiento(x)

    # Mostrar el resultado en la etiqueta
    result_label.config(text=f"Número de lotes: {n:.2f}, Rendimiento total: {rendimiento:.2f}")

    # Crear la gráfica
    x_values = np.linspace(1, 40, 400)
    rendimiento_values = [calcular_rendimiento(val)[1] for val in x_values]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, rendimiento_values, label='Rendimiento Total', color='blue')
    
    # Graficar el valor ingresado
    plt.scatter([x], [rendimiento], color='green', zorder=5, label=f'Ingresado: x = {x}, Rendimiento = {rendimiento:.2f}')
    plt.axvline(x=x, color='green', linestyle='--', label=f'Tamaño del lote = {x}')

    # Graficar la línea límite de 10 lotes
    plt.axvline(x=200 / 10, color='orange', linestyle='--', label='Límite de rendimiento sin reducción')

    # Personalizar la gráfica
    plt.title('Rendimiento Total en Función del Tamaño del Lote')
    plt.xlabel('Tamaño del Lote (x)')
    plt.ylabel('Rendimiento Total')
    plt.xlim(0, 40)
    plt.ylim(-5, 20)
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Maximizar Tamaño del Lote")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el tamaño del lote
label_tamaño_lote = Label(frame, text="Ingrese el tamaño del lote (x) en unidades de energía:")
label_tamaño_lote.pack(pady=(0, 5))

# Campo de entrada para el tamaño del lote
entry_tamaño_lote = Entry(frame)
entry_tamaño_lote.pack(pady=(0, 10))

# Botón para calcular y graficar
boton_calcular = Button(frame, text="Calcular y Graficar", command=actualizar_resultados)
boton_calcular.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
