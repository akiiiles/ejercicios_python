import tkinter as tk
from tkinter import messagebox
import sqlite3

# Definir tipos de tela y colores con tiempos asociados
telas = {
    "Algodón": {"Rojo": 2, "Azul": 3, "Verde": 1, "Negro": 4, "Blanco": 2, "Gris": 3, "Amarillo": 2, "Rosa": 2, "Marrón": 3, "Violeta": 4},
    "Lino": {"Rojo": 3, "Azul": 4, "Verde": 2, "Negro": 5, "Blanco": 3, "Gris": 4, "Amarillo": 3, "Rosa": 3, "Marrón": 4, "Violeta": 5},
    "Seda": {"Rojo": 4, "Azul": 5, "Verde": 3, "Negro": 6, "Blanco": 4, "Gris": 5, "Amarillo": 4, "Rosa": 4, "Marrón": 5, "Violeta": 6}
}

# Configuración de base de datos
def conectar_db():
    conexion = sqlite3.connect("tintoreria.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS pedido (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, tela TEXT, color TEXT, cantidad INTEGER, FOREIGN KEY(cliente_id) REFERENCES cliente(id))")
    conexion.commit()
    return conexion, cursor

# Funciones del sistema
def ingresar_cliente():
    nombre = entry_cliente.get()
    if nombre:
        cursor.execute("INSERT INTO cliente (nombre) VALUES (?)", (nombre,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente ingresado correctamente")
        entry_cliente.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Ingrese un nombre")

def ingresar_pedido():
    cliente_id = entry_cliente_id.get()
    tela = var_tela.get()
    color = var_color.get()
    cantidad = entry_cantidad.get()
    
    if cliente_id and tela and color and cantidad:
        cursor.execute("INSERT INTO pedido (cliente_id, tela, color, cantidad) VALUES (?, ?, ?, ?)", (cliente_id, tela, color, cantidad))
        conexion.commit()
        messagebox.showinfo("Éxito", "Pedido ingresado correctamente")
    else:
        messagebox.showwarning("Error", "Complete todos los campos")

def calcular_tiempo():
    cliente_id = entry_cliente_id.get()
    if not cliente_id:
        messagebox.showwarning("Error", "Ingrese un ID de cliente")
        return
    
    cursor.execute("SELECT tela, color, cantidad FROM pedido WHERE cliente_id=?", (cliente_id,))
    pedidos = cursor.fetchall()
    
    if not pedidos:
        messagebox.showwarning("Error", "No hay pedidos para este cliente")
        return
    
    tiempo_total = sum(telas[tela][color] * cantidad for tela, color, cantidad in pedidos)
    messagebox.showinfo("Tiempo estimado", f"El tiempo total estimado es {tiempo_total} horas")

# Interfaz gráfica
conexion, cursor = conectar_db()
root = tk.Tk()
root.title("Tintorería")

# Sección Ingreso de Cliente
frame_cliente = tk.Frame(root)
frame_cliente.pack(pady=10)
tk.Label(frame_cliente, text="Nombre Cliente:").pack(side=tk.LEFT)
entry_cliente = tk.Entry(frame_cliente)
entry_cliente.pack(side=tk.LEFT)
tk.Button(frame_cliente, text="Ingresar Cliente", command=ingresar_cliente).pack(side=tk.LEFT)

# Sección Ingreso de Pedido
frame_pedido = tk.Frame(root)
frame_pedido.pack(pady=10)
tk.Label(frame_pedido, text="ID Cliente:").pack(side=tk.LEFT)
entry_cliente_id = tk.Entry(frame_pedido)
entry_cliente_id.pack(side=tk.LEFT)
tk.Label(frame_pedido, text="Cantidad:").pack(side=tk.LEFT)
entry_cantidad = tk.Entry(frame_pedido)
entry_cantidad.pack(side=tk.LEFT)

# Menús desplegables para tela y color
var_tela = tk.StringVar()
var_tela.set("Algodón")
tk.Label(frame_pedido, text="Tela:").pack(side=tk.LEFT)
tela_menu = tk.OptionMenu(frame_pedido, var_tela, *telas.keys())
tela_menu.pack(side=tk.LEFT)

def actualizar_colores(*args):
    menu = color_menu['menu']
    menu.delete(0, 'end')
    for color in telas[var_tela.get()].keys():
        menu.add_command(label=color, command=tk._setit(var_color, color))
    var_color.set(list(telas[var_tela.get()].keys())[0])

var_tela.trace('w', actualizar_colores)
var_color = tk.StringVar()
var_color.set("Rojo")
tk.Label(frame_pedido, text="Color:").pack(side=tk.LEFT)
color_menu = tk.OptionMenu(frame_pedido, var_color, *telas["Algodón"].keys())
color_menu.pack(side=tk.LEFT)

# Botón para ingresar pedido
tk.Button(frame_pedido, text="Ingresar Pedido", command=ingresar_pedido).pack(side=tk.LEFT)

# Botón para calcular tiempo
frame_calculo = tk.Frame(root)
frame_calculo.pack(pady=10)
tk.Button(frame_calculo, text="Calcular Tiempo", command=calcular_tiempo).pack()

# Botón para salir
tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

root.mainloop()