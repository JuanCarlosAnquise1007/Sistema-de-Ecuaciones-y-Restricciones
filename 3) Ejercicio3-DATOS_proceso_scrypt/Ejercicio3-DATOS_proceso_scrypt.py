import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y entradas para el número de datos
        self.data_label = tk.Label(self, text="Ingrese el número de datos (máx. 10):")
        self.data_label.pack(side="top")

        self.data_entry = tk.Entry(self)
        self.data_entry.pack(side="top")

        # Botón para calcular
        self.calculate_button = tk.Button(self)
        self.calculate_button["text"] = "Calcular y Graficar"
        self.calculate_button["command"] = self.calculate
        self.calculate_button.pack(side="top")

        # Etiqueta para mostrar resultados
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(side="top")

        # Frame para el gráfico
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Número de Datos (x)')
        self.ax.set_ylabel('Tiempo de Ejecución (segundos)')
        self.ax.set_title('Tiempo de Ejecución vs Número de Datos')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="bottom")

    def calculate(self):
        try:
            # Leer el número de datos ingresados por el usuario
            x = int(self.data_entry.get())
            
            # Verificar si x está dentro del límite (máximo 10)
            if x < 0:
                messagebox.showerror("Error", "El número de datos no puede ser negativo.")
                return
            elif x > 10:
                messagebox.showerror("Error", "El número máximo de datos es 10.")
                return
            
            # Calcular el tiempo de ejecución
            tiempo_ejecucion = 5 * x + 2
            
            # Verificar el tiempo de ejecución
            if tiempo_ejecucion > 50:
                max_datos = (50 - 2) // 5
                self.result_label["text"] = f"Excede el tiempo de ejecución. Máximo datos procesables: {max_datos}"
            else:
                self.result_label["text"] = f"Tiempo de ejecución: {tiempo_ejecucion:.2f} segundos."

            # Actualizar gráfico
            self.ax.clear()  # Limpiar el gráfico

            # Redibujar el gráfico
            x_values = np.arange(0, 11)  # Valores de 0 a 10
            y_values = 5 * x_values + 2  # Tiempo de ejecución
            self.ax.plot(x_values, y_values, label='T(x) = 5x + 2', color='blue')
            self.ax.axhline(y=50, color='red', linestyle='--', label='Límite de 50 segundos')

            # Restablecer etiquetas y título
            self.ax.set_xlabel('Número de Datos (x)')
            self.ax.set_ylabel('Tiempo de Ejecución (segundos)')
            self.ax.set_title('Tiempo de Ejecución vs Número de Datos')
            self.ax.set_ylim(0, 60)
            self.ax.legend()  # Mostrar leyenda
            self.canvas.draw()  # Redibujar el canvas

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Maximización de Datos Procesados")
root.geometry("600x700")

app = Application(master=root)
app.mainloop()
