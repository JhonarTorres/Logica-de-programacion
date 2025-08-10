import tkinter as tk
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



###########################3funciones
def insertar_numero(valor):
    contenido_actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, contenido_actual + str(valor))

def insertar_operador(op):
    contenido_actual = entrada.get()
    if contenido_actual and contenido_actual[-1] not in '+-*/':
        entrada.delete(0, tk.END)
        entrada.insert(0, contenido_actual + op)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def toggle_distancia_section():
    if frame_distancia.winfo_ismapped():
        frame_distancia.place_forget()
    else:
        frame_distancia.place(x=10, y=100, width=400, height=140)

def calcular_distancia():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

        ventana_grafico = tk.Toplevel(ventana)
        ventana_grafico.title("Gráfico Distancia Euclidiana")
        ventana_grafico.geometry("500x500")

        fig, ax = plt.subplots(figsize=(5,5))
        ax.plot([x1, x2], [y1, y2], marker='o', color='blue')
        ax.annotate("P1", (x1, y1), textcoords="offset points", xytext=(5,-10))
        ax.annotate("P2", (x2, y2), textcoords="offset points", xytext=(5,-10))
        ax.set_title(f"Distancia Euclidiana: {distancia:.3f}")
        ax.grid(True)

        min_x = min(x1, x2) - 1
        max_x = max(x1, x2) + 1
        min_y = min(y1, y2) - 1
        max_y = max(y1, y2) + 1
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)

        canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        ventana_error = tk.Toplevel(ventana)
        ventana_error.title("Error")
        tk.Label(ventana_error, text="Por favor, ingresa números válidos").pack()

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("430x620")
ventana.resizable(False,False)
ventana.config(bg='light coral')

entrada = tk.Entry(ventana, font=("Arial", 20), bd=5, relief="sunken", justify='right')
entrada.place(x=10, y=10, width=400, height=50)

frame_distancia = tk.Frame(ventana, bd=2, relief='groove', bg='lightgray')


tk.Label(frame_distancia, text="Punto 1 :", bg='lightgray').place(x=10, y=10)
entry_x1 = tk.Entry(frame_distancia, width=8)
entry_x1.place(x=120, y=10)
entry_y1 = tk.Entry(frame_distancia, width=8)
entry_y1.place(x=190, y=10)

tk.Label(frame_distancia, text="Punto 2 :", bg='lightgray').place(x=10, y=50)
entry_x2 = tk.Entry(frame_distancia, width=8)
entry_x2.place(x=120, y=50)
entry_y2 = tk.Entry(frame_distancia, width=8)
entry_y2.place(x=190, y=50)

#############################################3 Etiquetas debajo para coordenadas x, y
tk.Label(frame_distancia, text="x", bg='lightgray').place(x=140, y=29)
tk.Label(frame_distancia, text="y", bg='lightgray').place(x=210, y=29)
tk.Label(frame_distancia, text="x", bg='lightgray').place(x=140, y=70)
tk.Label(frame_distancia, text="y", bg='lightgray').place(x=210, y=70)

btn_calcular_distancia = tk.Button(frame_distancia, text="Calcular", command=calcular_distancia)
btn_calcular_distancia.place(x=290, y=20, width=100, height=40)

#######################################33 Botones números
bt0 = tk.Button(ventana, text='0', command=lambda: insertar_numero(0), width=34, height=5)
bt0.place(x=6, y=530)

bt1 = tk.Button(ventana, text='1', command=lambda: insertar_numero(1), width=10, height=5)
bt1.place(x=6, y=440)

bt2 = tk.Button(ventana, text='2', command=lambda: insertar_numero(2), width=10, height=5)
bt2.place(x=90, y=440)

bt3 = tk.Button(ventana, text='3', command=lambda: insertar_numero(3), width=10, height=5)
bt3.place(x=174, y=440)

bt4 = tk.Button(ventana, text='4', command=lambda: insertar_numero(4), width=10, height=5)
bt4.place(x=6, y=350)

bt5 = tk.Button(ventana, text='5', command=lambda: insertar_numero(5), width=10, height=5)
bt5.place(x=90, y=350)

bt6 = tk.Button(ventana, text='6', command=lambda: insertar_numero(6), width=10, height=5)
bt6.place(x=174, y=350)

bt7 = tk.Button(ventana, text='7', command=lambda: insertar_numero(7), width=10, height=5)
bt7.place(x=6, y=260)

bt8 = tk.Button(ventana, text='8', command=lambda: insertar_numero(8), width=10, height=5)
bt8.place(x=90, y=260)

bt9 = tk.Button(ventana, text='9', command=lambda: insertar_numero(9), width=10, height=5)
bt9.place(x=174, y=260)

# Botones operaciones
btC = tk.Button(ventana, text='C', command=borrar, width=10, height=5)
btC.place(x=257, y=530)

btX = tk.Button(ventana, text='X', command=lambda: insertar_operador('*'), width=10, height=5)
btX.place(x=257, y=440)

btr = tk.Button(ventana, text='-', command=lambda: insertar_operador('-'), width=10, height=5)
btr.place(x=257, y=350)

bts = tk.Button(ventana, text='+', command=lambda: insertar_operador('+'), width=10, height=5)
bts.place(x=257, y=260)

btr2 = tk.Button(ventana, text='/', command=lambda: insertar_operador('/'), width=10, height=5)
btr2.place(x=342, y=530)

btIgual = tk.Button(ventana, text='=', command=calcular, width=10, height=5)
btIgual.place(x=342, y=440)

btn_distancia = tk.Button(ventana, text="Distancia E", command=toggle_distancia_section, width=10, height=11)
btn_distancia.place(x=342, y=260)

ventana.mainloop()

