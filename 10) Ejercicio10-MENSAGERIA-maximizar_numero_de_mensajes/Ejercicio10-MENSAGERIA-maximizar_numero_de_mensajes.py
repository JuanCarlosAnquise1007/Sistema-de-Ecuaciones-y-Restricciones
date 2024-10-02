import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

# Función para calcular la latencia
def latencia(x):
    return 100 - 2 * x

# Función para actualizar los resultados y la gráfica
def actualizar_resultados():
    try:
        x = float(entry_num_mensajes.get())
        if x < 0:
            result_label.config(text="El número de mensajes debe ser mayor o igual a 0.")
            return
        if x > 40:
            result_label.config(text="El número de mensajes no puede ser mayor que 40.")
            return
    except ValueError:
        result_label.config(text="Por favor, ingrese un valor numérico válido.")
        return

    # Calcular la latencia
    lat = latencia(x)

    # Mostrar el resultado en la etiqueta
    result_label.config(text=f"Latencia para {x} mensajes/segundo: {lat:.2f} ms")

    # Crear la gráfica
    x_values = np.linspace(0, 50, 400)
    lat_values = latencia(x_values)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, lat_values, label='Latencia (L)', color='blue')
    
    # Graficar el valor ingresado
    plt.scatter([x], [lat], color='green', zorder=5, label=f'Ingresado: {x} mensajes/segundo, Latencia = {lat:.2f} ms')
    plt.axhline(y=20, color='orange', linestyle='--', label='Límite de Latencia = 20 ms')
    plt.axvline(x=40, color='red', linestyle='--', label='Máximo: 40 mensajes/segundo')

    # Personalizar la gráfica
    plt.title('Latencia en Función del Número de Mensajes por Segundo')
    plt.xlabel('Número de Mensajes por Segundo (x)')
    plt.ylabel('Latencia (ms)')
    plt.xlim(0, 50)
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Maximizar Mensajes en un Sistema de Mensajería")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el número de mensajes
label_num_mensajes = Label(frame, text="Ingrese el número de mensajes por segundo:")
label_num_mensajes.pack(pady=(0, 5))

# Campo de entrada para el número de mensajes
entry_num_mensajes = Entry(frame)
entry_num_mensajes.pack(pady=(0, 10))

# Botón para calcular y graficar
boton_calcular = Button(frame, text="Calcular y Graficar", command=actualizar_resultados)
boton_calcular.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
