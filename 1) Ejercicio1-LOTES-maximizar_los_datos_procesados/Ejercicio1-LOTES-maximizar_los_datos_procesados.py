import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definimos la variable global para el canvas
canvas = None

def maximizar_datos(x, num_lotes):
    # Parámetros del problema
    memoria_total = 1024  # MB
    max_lotes = num_lotes  # Número máximo de lotes definidos por el usuario
    eficiencia_reducida = 0.8  # 20% de reducción de eficiencia a partir del 6º lote
    
    # Inicialización de variables
    memoria_utilizada = 0
    datos_procesados = 0
    
    # Almacenamos los datos por lote para visualización y eficiencia
    lotes_procesados = 0
    datos_por_lote = []
    eficiencia_por_lote = []
    
    # Procesamos los lotes hasta el número máximo indicado
    for lote in range(1, max_lotes + 1):
        if memoria_utilizada + x <= memoria_total:
            if lote <= 5:
                # Los primeros 5 lotes no tienen reducción de eficiencia
                datos_procesados += x
                datos_por_lote.append(x)
                eficiencia_por_lote.append(1.0)  # 100% de eficiencia
            else:
                # A partir del 6º lote, hay reducción del 20%
                datos_procesados += x * eficiencia_reducida
                datos_por_lote.append(x * eficiencia_reducida)
                eficiencia_por_lote.append(eficiencia_reducida)  # 80% de eficiencia
            
            memoria_utilizada += x
            lotes_procesados += 1
        else:
            # Si no se puede procesar el lote debido a la limitación de memoria
            datos_por_lote.append(0)
            eficiencia_por_lote.append(0)  # 0% de eficiencia, no se procesa el lote
    
    # Asegurar que el número de lotes está en la lista
    while len(datos_por_lote) < max_lotes:
        datos_por_lote.append(0)  # No se procesan más lotes
        eficiencia_por_lote.append(0)  # 0% de eficiencia
    
    # Devolver resultados y datos por lote
    return lotes_procesados, memoria_utilizada, datos_procesados, datos_por_lote, eficiencia_por_lote

def actualizar_grafico(datos_por_lote, num_lotes):
    global canvas
    
    # Limpiar el canvas anterior si existe
    if canvas:
        canvas.get_tk_widget().pack_forget()
    
    # Crear la figura para graficar
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(range(1, num_lotes + 1), datos_por_lote[:num_lotes], color='skyblue')  # Graficar los lotes seleccionados
    ax.set_xlabel("Número de lote")
    ax.set_ylabel("Datos procesados por lote (MB)")
    ax.set_title("Maximización de los datos procesados por lote")
    
    # Mostrar el gráfico en la interfaz Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

def graficar():
    try:
        # Obtener los valores de entrada del usuario
        x = float(entry_lote.get())
        num_lotes = int(entry_num_lotes.get())
        
        # Validación del tamaño de lote y número de lotes
        if x <= 0:
            messagebox.showerror("Error", "El tamaño del lote debe ser mayor que 0.")
            return
        if not (1 <= num_lotes <= 8):
            messagebox.showerror("Error", "El número de lotes debe estar entre 1 y 8.")
            return
        
        # Llamar a la función maximizar_datos
        lotes_procesados, memoria_utilizada, datos_procesados, datos_por_lote, eficiencia_por_lote = maximizar_datos(x, num_lotes)
        
        # Mostrar los resultados en etiquetas
        label_resultado.config(text=f"Lotes procesados: {lotes_procesados}\n"
                                    f"Memoria utilizada: {memoria_utilizada} MB\n"
                                    f"Datos procesados: {datos_procesados:.2f} MB")
        
        # Actualizar el gráfico con los nuevos datos
        actualizar_grafico(datos_por_lote, num_lotes)
        
        # Mostrar las iteraciones y la eficiencia en cada lote
        iteraciones_texto = "Iteraciones y eficiencia:\n"
        for i in range(num_lotes):  # Mostrar solo los lotes seleccionados
            eficiencia = eficiencia_por_lote[i] * 100  # Convertir a porcentaje
            iteraciones_texto += f"Lote {i + 1}: Eficiencia del {eficiencia:.0f}%\n"
        
        label_iteraciones.config(text=iteraciones_texto)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para el tamaño del lote y el número de lotes.")

# Crear la ventana principal
root = tk.Tk()
root.title("Maximización de Datos Procesados")
#root.geometry("600x700")

# Frame para la entrada y el botón
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=20)

# Etiqueta y campo de entrada para el tamaño del lote
label_lote = tk.Label(frame_entrada, text="Tamaño del lote (MB):")
label_lote.grid(row=0, column=0, padx=10)

entry_lote = tk.Entry(frame_entrada)
entry_lote.grid(row=0, column=1, padx=10)

# Etiqueta y campo de entrada para el número de lotes a procesar
label_num_lotes = tk.Label(frame_entrada, text="Número de lotes (máx 8):")
label_num_lotes.grid(row=1, column=0, padx=10)

entry_num_lotes = tk.Entry(frame_entrada)
entry_num_lotes.grid(row=1, column=1, padx=10)

# Botón para calcular y graficar
btn_graficar = tk.Button(frame_entrada, text="Calcular y Graficar", command=graficar)
btn_graficar.grid(row=2, columnspan=2, pady=10)

# Etiqueta para mostrar los resultados
label_resultado = tk.Label(root, text="", justify="left")
label_resultado.pack(pady=10)

# Frame para el gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20)

# Etiqueta para mostrar las iteraciones y la eficiencia
label_iteraciones = tk.Label(root, text="", justify="left")
label_iteraciones.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
