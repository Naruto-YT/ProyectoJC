import tkinter as tk
from tkinter import ttk, messagebox
from conversiones import convertir
from tabla import obtener_tabla

# Diccionario de categorías y sus unidades (ajustado a conversiones.py)
categorias = {
    "masa": ["gramo", "kilogramo", "libra"],
    "longitud": ["centimetro", "metro", "kilometro", "milla"],
    "temperatura": ["celsius", "fahrenheit", "kelvin"]
}

def actualizar_unidades(event):
    categoria = combo_categoria.get().lower()
    unidades = categorias.get(categoria, [])
    combo_origen['values'] = unidades
    combo_destino['values'] = unidades
    combo_origen.set('')
    combo_destino.set('')

def realizar_conversion():
    try:
        valor = float(entrada_valor.get())
        categoria = combo_categoria.get().lower()
        unidad_origen = combo_origen.get().lower()
        unidad_destino = combo_destino.get().lower()

        if not categoria or not unidad_origen or not unidad_destino:
            raise ValueError("Debe seleccionar todas las opciones.")

        if unidad_origen == unidad_destino:
            etiqueta_resultado.config(text=f"Resultado: {valor} (mismo tipo de unidad)")
            return

        resultado = convertir(valor, categoria, unidad_origen, unidad_destino)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Verifica que todos los campos estén completos y correctos.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def hacer_otra_conversion():
    entrada_valor.delete(0, tk.END)
    combo_categoria.set('')
    combo_origen.set('')
    combo_destino.set('')
    etiqueta_resultado.config(text="Resultado: ")

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("700x600")

# --- Tabla de conversiones (parte superior) ---
tk.Label(ventana, text="Tabla de conversiones (guía):", font=("Arial", 12, "bold")).pack(pady=5)
etiqueta_tabla = tk.Label(ventana, text=obtener_tabla(), justify="left", font=("Courier", 10), bg="#f0f0f0")
etiqueta_tabla.pack(padx=10, pady=5, fill="x")

# --- Área de conversión ---
frame_conversion = tk.Frame(ventana)
frame_conversion.pack(pady=20)

tk.Label(frame_conversion, text="Categoría:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
combo_categoria = ttk.Combobox(frame_conversion, values=list(categorias.keys()), state="readonly")
combo_categoria.grid(row=0, column=1, padx=5)
combo_categoria.bind("<<ComboboxSelected>>", actualizar_unidades)

tk.Label(frame_conversion, text="Unidad de origen:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
combo_origen = ttk.Combobox(frame_conversion, state="readonly")
combo_origen.grid(row=1, column=1, padx=5)

tk.Label(frame_conversion, text="Unidad de destino:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
combo_destino = ttk.Combobox(frame_conversion, state="readonly")
combo_destino.grid(row=2, column=1, padx=5)

tk.Label(frame_conversion, text="Valor:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entrada_valor = tk.Entry(frame_conversion)
entrada_valor.grid(row=3, column=1, padx=5)

boton_realizar = tk.Button(frame_conversion, text="Convertir", command=realizar_conversion)
boton_realizar.grid(row=4, column=0, columnspan=2, pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=5)

# --- Botones de acción ---
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Otra conversión", command=hacer_otra_conversion).pack(side="left", padx=10)

ventana.mainloop()
