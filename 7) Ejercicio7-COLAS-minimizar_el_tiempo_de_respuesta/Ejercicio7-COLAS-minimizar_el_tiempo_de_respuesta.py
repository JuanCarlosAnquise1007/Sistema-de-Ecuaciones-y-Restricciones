import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

# Función de tiempo de respuesta
def tiempo_respuesta(x):
    return 100 / x + 2 * x

# Función para minimizar el tiempo de respuesta y encontrar el valor óptimo de x
def minimizar_tiempo_respuesta():
    # Obtener el valor mínimo de trabajos por segundo (x)
    try:
        trabajos_por_segundo = float(entry_trabajos_por_segundo.get())
        if trabajos_por_segundo < 5:
            result_label.config(text="El valor mínimo de trabajos por segundo es 5.")
            return
    except ValueError:
        result_label.config(text="Por favor, ingrese un valor numérico válido.")
        return

    # Calcular el tiempo de respuesta para el valor ingresado
    tiempo_minimo = tiempo_respuesta(trabajos_por_segundo)

    # Crear un rango de valores de x desde el mínimo permitido hasta 20 (para la gráfica)
    x_values = np.linspace(5, 20, 100)
    y_values = tiempo_respuesta(x_values)

    # Encontrar el valor de x que minimiza la función
    x_optimo = np.sqrt(50)  # Derivada analítica de la función T(x) para encontrar el mínimo
    tiempo_optimo = tiempo_respuesta(x_optimo)

    # Mostrar el resultado en la etiqueta
    result_label.config(text=f"El número óptimo de trabajos es {x_optimo:.2f} con un tiempo de respuesta de {tiempo_optimo:.2f} segundos.")

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='T(x) = 100/x + 2x', color='blue')
    
    # Graficar el valor óptimo de x
    plt.scatter([x_optimo], [tiempo_optimo], color='red', zorder=5, label=f'Óptimo: T({x_optimo:.2f}) = {tiempo_optimo:.2f}')
    plt.axvline(x=x_optimo, color='red', linestyle='--', label=f'Valor óptimo de x = {x_optimo:.2f}')
    
    # Graficar el valor de trabajos por segundo ingresado por el usuario
    plt.scatter([trabajos_por_segundo], [tiempo_minimo], color='green', zorder=5, label=f'Ingresado: T({trabajos_por_segundo}) = {tiempo_minimo:.2f}')
    plt.axvline(x=trabajos_por_segundo, color='green', linestyle='--', label=f'Trabajos por segundo = {trabajos_por_segundo}')

    # Graficar la línea límite de 5 trabajos por segundo
    plt.axvline(x=5, color='orange', linestyle='--', label='Límite mínimo de 5 trabajos')

    # Personalizar la gráfica
    plt.title('Minimización del Tiempo de Respuesta')
    plt.xlabel('Trabajos por Segundo (x)')
    plt.ylabel('Tiempo de Respuesta T(x)')
    plt.xlim(4, 21)
    plt.ylim(0, 50)
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Minimizar Tiempo de Respuesta")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el número de trabajos por segundo
label_trabajos_por_segundo = Label(frame, text="Ingrese el número de trabajos por segundo (mínimo 5):")
label_trabajos_por_segundo.pack(pady=(0, 5))

# Campo de entrada para el número de trabajos por segundo
entry_trabajos_por_segundo = Entry(frame)
entry_trabajos_por_segundo.pack(pady=(0, 10))

# Botón para graficar
boton_graficar = Button(frame, text="Calcular y Graficar", command=minimizar_tiempo_respuesta)
boton_graficar.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
