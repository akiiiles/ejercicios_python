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

# Nueva función para ver clientes y pedidos
def ver_clientes_y_pedidos():
    cursor.execute("SELECT cliente.id, cliente.nombre, pedido.tela, pedido.color, pedido.cantidad FROM cliente LEFT JOIN pedido ON cliente.id = pedido.cliente_id")
    datos = cursor.fetchall()
    
    ventana = tk.Toplevel(root)
    ventana.title("Clientes y Pedidos")
    
    text = tk.Text(ventana, width=60, height=20)
    text.pack()
    
    if not datos:
        text.insert(tk.END, "No hay clientes ni pedidos registrados.\n")
    else:
        text.insert(tk.END, "ID Cliente | Nombre | Tela | Color | Cantidad\n")
        text.insert(tk.END, "-----------------------------------------------------\n")
        for dato in datos:
            text.insert(tk.END, f"{dato[0]} | {dato[1]} | {dato[2] or '-'} | {dato[3] or '-'} | {dato[4] or '-'}\n")

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

# Interfaz gráfica
conexion, cursor = conectar_db()
root = tk.Tk()
root.title("Tintorería")

# Botón para ver clientes y pedidos
tk.Button(root, text="Ver Clientes y Pedidos", command=ver_clientes_y_pedidos).pack(pady=10)

root.mainloop()
