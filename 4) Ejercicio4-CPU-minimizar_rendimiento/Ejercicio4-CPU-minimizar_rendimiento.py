import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Frame, Entry

def uso_cpu(x):
    return 2 * x**2 + 10 * x

def graficar():
    # Obtener el valor ingresado por el usuario
    try:
        peticiones = int(entry_peticiones.get())
        if peticiones < 10:
            result_label.config(text="El número de peticiones debe ser al menos 10.")
            return
    except ValueError:
        result_label.config(text="Por favor, ingrese un número válido.")
        return

    # Crear un rango de peticiones por segundo
    x_values = np.linspace(10, 30, 200)  # Rango desde 10 hasta 30
    y_values = uso_cpu(x_values)

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='Uso de CPU (U(x))', color='blue')

    # Área sombreada para el uso de CPU permitido
    plt.fill_between(x_values, y_values, 80, where=(y_values <= 80), color='lightgreen', alpha=0.5, label='Uso de CPU permitido')
    plt.fill_between(x_values, 80, 100, where=(y_values > 80), color='salmon', alpha=0.5, label='Uso de CPU > 80%')

    plt.axhline(y=80, color='red', linestyle='--', label='Límite de 80% CPU')
    plt.axvline(x=10, color='green', linestyle='--', label='Umbral de 10 peticiones/s')

    # Graficar el uso de CPU para las peticiones ingresadas
    u_peticiones = uso_cpu(peticiones)
    plt.scatter([peticiones], [u_peticiones], color='orange', zorder=5)
    plt.text(peticiones, u_peticiones, f'  ({peticiones}, {u_peticiones})', fontsize=10, color='orange')

    # Mensaje de resultados
    if u_peticiones <= 80:
        result_label.config(text="El uso de CPU está dentro del límite permitido.")
    else:
        result_label.config(text="El uso de CPU excede el 80%.")

    # Encontrar el rango óptimo de peticiones
    rango_optimo = x_values[(y_values <= 80)]
    if len(rango_optimo) > 0:
        rango_min = rango_optimo[0]
        rango_max = rango_optimo[-1]
        plt.axvspan(rango_min, rango_max, color='yellow', alpha=0.3, label='Rango óptimo (U(x) ≤ 80%)')
    
    # Personalizar la gráfica
    plt.title('Uso de CPU en función de las peticiones por segundo')
    plt.xlabel('Peticiones por segundo (x)')
    plt.ylabel('Uso de CPU (%)')
    plt.ylim(0, 100)
    plt.xlim(0, 30)
    plt.legend()
    plt.grid()
    plt.show()

# Crear la ventana principal
root = Tk()
root.title("Minimizar Uso de CPU")

# Crear un marco para contener los widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Etiqueta para ingresar el número de peticiones
label_peticiones = Label(frame, text="Ingrese el número de peticiones por segundo:")
label_peticiones.pack(pady=(0, 5))

# Campo de entrada para peticiones
entry_peticiones = Entry(frame)
entry_peticiones.pack(pady=(0, 10))

# Botón para graficar
boton_graficar = Button(frame, text="Graficar Uso de CPU", command=graficar)
boton_graficar.pack()

# Etiqueta para mostrar resultados o mensajes
result_label = Label(frame, text="")
result_label.pack(pady=(10, 0))

# Ejecutar el bucle principal
root.mainloop()
