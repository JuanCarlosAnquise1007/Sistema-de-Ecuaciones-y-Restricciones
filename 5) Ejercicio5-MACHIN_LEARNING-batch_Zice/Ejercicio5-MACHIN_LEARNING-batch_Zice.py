import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

# Definir la función del tiempo de entrenamiento
def tiempo_entrenamiento(x):
    return 1000 * x + 0.1 * x

def graficar():
    # Obtener el batch size ingresado
    try:
        batch_size = int(entry_batch_size.get())
        if batch_size < 16 or batch_size > 128:
            result_label.config(text="El tamaño del batch debe estar entre 16 y 128.")
            return
    except ValueError:
        result_label.config(text="Por favor, ingrese un número válido.")
        return

    # Crear un rango de batch sizes
    x_values = np.linspace(16, 128, 100)
    y_values = tiempo_entrenamiento(x_values)

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='T(x) = 1000x + 0.1x', color='blue')

    # Encontrar y graficar el tiempo de entrenamiento para el batch size ingresado
    tiempo_minimo = tiempo_entrenamiento(batch_size)
    plt.scatter([batch_size], [tiempo_minimo], color='red', zorder=5)
    
    # Agregar el texto del resultado en la gráfica
    plt.text(batch_size, tiempo_minimo, f'T({batch_size}) = {tiempo_minimo:.2f}', fontsize=10, color='red', 
             verticalalignment='bottom', horizontalalignment='right')

    # Personalizar la gráfica
    plt.title('Tiempo de Entrenamiento en Función del Batch Size')
    plt.xlabel('Batch Size (x)')
    plt.ylabel('Tiempo de Entrenamiento T(x)')
    plt.ylim(0, 200000)  # Ajustar el límite superior según el rango esperado
    plt.xlim(10, 130)  # Ajustar el límite para incluir el rango
    plt.axhline(y=tiempo_entrenamiento(16), color='green', linestyle='--', label='T(16) (Mínimo)')
    plt.axvline(x=16, color='green', linestyle='--', label='Batch size mínimo (16)')
    plt.axvline(x=128, color='orange', linestyle='--', label='Batch size máximo (128)')
    plt.legend()
    plt.grid()
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Minimizar Tiempo de Entrenamiento")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el tamaño del batch
label_batch_size = Label(frame, text="Ingrese el tamaño del batch (16 a 128):")
label_batch_size.pack(pady=(0, 5))

# Campo de entrada para el tamaño del batch
entry_batch_size = Entry(frame)
entry_batch_size.pack(pady=(0, 10))

# Botón para graficar
boton_graficar = Button(frame, text="Graficar Tiempo de Entrenamiento", command=graficar)
boton_graficar.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
