import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def max_peticiones_por_nodo(num_nodos, capacidad_red):
    # Calculamos el número máximo de peticiones que puede procesar cada nodo
    x = capacidad_red / num_nodos
    
    # Redondeamos hacia abajo para asegurarnos de no exceder la capacidad de la red
    x = int(x)
    
    return x

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.num_nodos_label = tk.Label(self, text="Número de nodos:")
        self.num_nodos_label.pack(side="top")

        self.num_nodos_entry = tk.Entry(self)
        self.num_nodos_entry.pack(side="top")

        self.capacidad_red_label = tk.Label(self, text="Capacidad de la red:")
        self.capacidad_red_label.pack(side="top")

        self.capacidad_red_entry = tk.Entry(self)
        self.capacidad_red_entry.pack(side="top")

        self.calculate_button = tk.Button(self)
        self.calculate_button["text"] = "Calcular"
        self.calculate_button["command"] = self.calculate
        self.calculate_button.pack(side="top")

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(side="top")

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Componentes del sistema')
        self.ax.set_ylabel('Peticiones por segundo')
        self.ax.set_title('Peticiones procesadas por el sistema')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="bottom")

    def calculate(self):
        num_nodos = int(self.num_nodos_entry.get())
        capacidad_red = int(self.capacidad_red_entry.get())

        x = max_peticiones_por_nodo(num_nodos, capacidad_red)

        self.result_label["text"] = f"Para maximizar el número de peticiones procesadas, cada nodo debe procesar {x} peticiones por segundo.\nEl sistema en su conjunto puede procesar {x * num_nodos} peticiones por segundo."

        self.ax.clear()
        self.ax.bar(['Nodos', 'Red'], [num_nodos * x, capacidad_red])
        self.canvas.draw()

root = tk.Tk()
app = Application(master=root)
app.mainloop()