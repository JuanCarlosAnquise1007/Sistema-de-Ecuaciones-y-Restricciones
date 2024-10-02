import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

# Función para calcular el costo de almacenamiento
def costo_almacenamiento(x):
    return 50 + 5 * x

# Función para actualizar los resultados y la gráfica
def actualizar_resultados():
    try:
        x = float(entry_tamaño_almacenamiento.get())
        if x < 0:
            result_label.config(text="La cantidad de TB debe ser mayor o igual a 0.")
            return
    except ValueError:
        result_label.config(text="Por favor, ingrese un valor numérico válido.")
        return

    # Calcular el costo de almacenamiento
    costo = costo_almacenamiento(x)

    # Mostrar el resultado en la etiqueta
    if costo > 500:
        result_label.config(text=f"El costo excede el presupuesto de 500 dólares.")
    else:
        result_label.config(text=f"Costo de almacenamiento para {x} TB: {costo:.2f} dólares.")

    # Crear la gráfica
    x_values = np.linspace(0, 100, 400)
    costo_values = costo_almacenamiento(x_values)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, costo_values, label='Costo de Almacenamiento', color='blue')
    
    # Graficar el valor ingresado
    plt.scatter([x], [costo], color='green', zorder=5, label=f'Ingresado: {x} TB, Costo = {costo:.2f}')
    plt.axhline(y=500, color='orange', linestyle='--', label='Presupuesto = 500 dólares')
    plt.axvline(x=90, color='red', linestyle='--', label='Máximo: 90 TB')

    # Personalizar la gráfica
    plt.title('Costo de Almacenamiento vs. Cantidad de TB')
    plt.xlabel('Cantidad de TB Almacenados (x)')
    plt.ylabel('Costo de Almacenamiento ($)')
    plt.xlim(0, 100)
    plt.ylim(0, 600)
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Maximizar Almacenamiento en la Nube")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el tamaño del almacenamiento
label_tamaño_almacenamiento = Label(frame, text="Ingrese la cantidad de TB de almacenamiento:")
label_tamaño_almacenamiento.pack(pady=(0, 5))

# Campo de entrada para el tamaño del almacenamiento
entry_tamaño_almacenamiento = Entry(frame)
entry_tamaño_almacenamiento.pack(pady=(0, 10))

# Botón para calcular y graficar
boton_calcular = Button(frame, text="Calcular y Graficar", command=actualizar_resultados)
boton_calcular.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
