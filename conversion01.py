def convertir(valor, categoria, unidad_origen, unidad_destino):
    conversiones = {
        "longitud": {
            "centimetro": {"metro": 0.01, "kilometro": 0.00001, "milla": 0.0000062137},
            "metro": {"centimetro": 100, "kilometro": 0.001, "milla": 0.000621371},
            "kilometro": {"centimetro": 100000, "metro": 1000, "milla": 0.621371},
            "milla": {"kilometro": 1.60934, "metro": 1609.34, "centimetro": 160934}
        },
        "masa": {
            "gramo": {"kilogramo": 0.001, "libra": 0.00220462},
            "kilogramo": {"gramo": 1000, "libra": 2.20462},
            "libra": {"gramo": 453.592, "kilogramo": 0.453592}
        },
        "temperatura": {
            "celsius": {
                "fahrenheit": lambda c: (c * 9/5) + 32,
                "kelvin": lambda c: c + 273.15
            },
            "fahrenheit": {
                "celsius": lambda f: (f - 32) * 5/9,
                "kelvin": lambda f: (f - 32) * 5/9 + 273.15
            },
            "kelvin": {
                "celsius": lambda k: k - 273.15,
                "fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
            }
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
