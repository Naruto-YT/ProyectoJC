def convertir(valor, categoria, unidad_origen, unidad_destino):
    conversiones = {  # Asegúrate de que esta estructura está bien definida
        "distancia": {
            "metros": {"pies": 3.28084, "kilometros": 0.001, "millas": 0.000621371},
            "pies": {"metros": 0.3048, "kilometros": 0.0003048, "millas": 0.000189394},
            "kilometros": {"metros": 1000, "pies": 3280.84, "millas": 0.621371},
            "millas": {"metros": 1609.34, "pies": 5280, "kilometros": 1.60934}
        }
    }
    
    if categoria not in conversiones:
        return "Categoría no válida."
    
    if unidad_origen not in conversiones[categoria]:
        return f"La unidad de origen '{unidad_origen}' no es válida."
    
    if unidad_destino not in conversiones[categoria][unidad_origen]:
        return f"La unidad de destino '{unidad_destino}' no es válida."
    
    conversion = conversiones[categoria][unidad_origen][unidad_destino]
    return conversion(valor) if callable(conversion) else valor * conversion
