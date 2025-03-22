import tkinter as tk
from tkinter import messagebox
from conversiones import convertir
from tabla import obtener_tabla

def realizar_conversion():
    valor = entrada_valor.get()
    categoria = entrada_categoria.get().lower()
    unidad_origen = entrada_origen.get().lower()
    unidad_destino = entrada_destino.get().lower()
    
    try:
        valor = float(valor)
        resultado = convertir(valor, categoria, unidad_origen, unidad_destino)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("500x400")

# Mostrar tabla de conversiones
etiqueta_tabla = tk.Label(ventana, text=obtener_tabla(), justify="left", font=("Courier", 10))
etiqueta_tabla.pack(pady=5)

# Entradas de usuario
tk.Label(ventana, text="Categoría:").pack()
entrada_categoria = tk.Entry(ventana)
entrada_categoria.pack()

tk.Label(ventana, text="Valor:").pack()
entrada_valor = tk.Entry(ventana)
entrada_valor.pack()

tk.Label(ventana, text="Unidad de origen:").pack()
entrada_origen = tk.Entry(ventana)
entrada_origen.pack()

tk.Label(ventana, text="Unidad de destino:").pack()
entrada_destino = tk.Entry(ventana)
entrada_destino.pack()

# Botón de conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=realizar_conversion)
boton_convertir.pack(pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"))
etiqueta_resultado.pack()

ventana.mainloop()
