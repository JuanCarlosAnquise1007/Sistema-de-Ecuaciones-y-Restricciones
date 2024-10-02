import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

# Definir la función de ancho de banda disponible
def ancho_de_banda_disponible(n):
    if n <= 30:
        return 1000
    else:
        return 1000 * (0.95 ** (n - 30))

# Definir la función que busca el número máximo de archivos que se pueden transmitir
def maximizar_archivos(x):
    max_archivos = 0
    for n in range(1, 51):  # Máximo de 50 archivos
        if n * x <= ancho_de_banda_disponible(n):
            max_archivos = n
        else:
            break
    return max_archivos

# Función para graficar el ancho de banda y mostrar el resultado
def graficar():
    try:
        x = float(entry_bandwidth.get())  # Obtener el ancho de banda por archivo
    except ValueError:
        result_label.config(text="Por favor, ingrese un valor numérico válido.")
        return

    if x <= 0:
        result_label.config(text="El ancho de banda por archivo debe ser mayor que 0.")
        return

    # Calcular el número máximo de archivos
    max_archivos = maximizar_archivos(x)

    # Mostrar el resultado en la etiqueta
    result_label.config(text=f"El número máximo de archivos que se pueden transmitir es: {max_archivos}")

    # Graficar el ancho de banda disponible
    n_values = np.arange(1, 51)
    banda_values = [ancho_de_banda_disponible(n) for n in n_values]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, banda_values, label="Ancho de banda disponible", color='blue')
    plt.axvline(x=max_archivos, color='red', linestyle='--', label=f"Máximo archivos ({max_archivos})")
    plt.title('Ancho de Banda Disponible en Función del Número de Archivos Transmitidos')
    plt.xlabel('Número de Archivos')
    plt.ylabel('Ancho de Banda Disponible (Mbps)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Maximizar Archivos Transmitidos")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el ancho de banda por archivo
label_bandwidth = Label(frame, text="Ingrese el ancho de banda por archivo (Mbps):")
label_bandwidth.pack(pady=(0, 5))

# Campo de entrada para el ancho de banda por archivo
entry_bandwidth = Entry(frame)
entry_bandwidth.pack(pady=(0, 10))

# Botón para graficar
boton_graficar = Button(frame, text="Graficar y Calcular", command=graficar)
boton_graficar.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
