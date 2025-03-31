import tkinter as tk
from tkinter import messagebox
from conversiones import convertir
from tabla import obtener_tabla

def actualizar_unidades(*args):
    categoria = categoria_var.get()
    unidades_disponibles = unidades_por_categoria.get(categoria, [])
    unidad_origen_var.set(unidades_disponibles[0] if unidades_disponibles else "")
    unidad_destino_var.set(unidades_disponibles[0] if unidades_disponibles else "")
    menu_origen['menu'].delete(0, 'end')
    menu_destino['menu'].delete(0, 'end')
    for unidad in unidades_disponibles:
        menu_origen['menu'].add_command(label=unidad, command=tk._setit(unidad_origen_var, unidad))
        menu_destino['menu'].add_command(label=unidad, command=tk._setit(unidad_destino_var, unidad))

def realizar_conversion():
    try:
        valor = float(entrada_valor.get())
        categoria = categoria_var.get().lower()
        unidad_origen = unidad_origen_var.get().lower()
        unidad_destino = unidad_destino_var.get().lower()
        resultado = convertir(valor, categoria, unidad_origen, unidad_destino)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def hacer_otra_conversion():
    entrada_valor.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado: ")

ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("650x500")

# Mostrar tabla de conversiones
etiqueta_tabla = tk.Label(ventana, text=obtener_tabla(), justify="left", font=("Courier", 10))
etiqueta_tabla.pack(pady=5)

# Datos de unidades por categoría
unidades_por_categoria = {
    "Distancia": ["metros", "pies", "kilometros", "millas"],
    "Temperatura": ["celsius", "fahrenheit", "kelvin"],
    "Masa": ["kilogramos", "libras", "gramos", "onzas"],
    "Velocidad": ["kilometros/h", "metros/s", "millas/h"]
}

# Categoría
categoria_var = tk.StringVar(value="Distancia")
categoria_var.trace("w", actualizar_unidades)
tk.Label(ventana, text="Categoría:").pack()
menu_categoria = tk.OptionMenu(ventana, categoria_var, *unidades_por_categoria.keys())
menu_categoria.pack()

# Valor
tk.Label(ventana, text="Valor:").pack()
entrada_valor = tk.Entry(ventana)
entrada_valor.pack()

# Unidad de origen
unidad_origen_var = tk.StringVar()
tk.Label(ventana, text="Unidad de origen:").pack()
menu_origen = tk.OptionMenu(ventana, unidad_origen_var, "")
menu_origen.pack()

# Unidad de destino
unidad_destino_var = tk.StringVar()
tk.Label(ventana, text="Unidad de destino:").pack()
menu_destino = tk.OptionMenu(ventana, unidad_destino_var, "")
menu_destino.pack()

# Inicializar unidades disponibles
tk.Frame(ventana).after(100, actualizar_unidades)

# Botón de conversión
boton_realizar_conversion = tk.Button(ventana, text="Realizar Conversión", command=realizar_conversion)
boton_realizar_conversion.pack(pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"))
etiqueta_resultado.pack()

# Botón para hacer otra conversión
boton_otra_conversion = tk.Button(ventana, text="Hacer otra conversión", command=hacer_otra_conversion)
boton_otra_conversion.pack(pady=10)

ventana.mainloop()
