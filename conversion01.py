from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def convertir(valor, categoria, unidad_origen, unidad_destino):
    conversiones = {
        "distancia": {
            "metros": {"pies": 3.28084, "kilometros": 0.001, "millas": 0.000621371},
            "pies": {"metros": 0.3048, "kilometros": 0.0003048, "millas": 0.000189394},
            "kilometros": {"metros": 1000, "pies": 3280.84, "millas": 0.621371},
            "millas": {"metros": 1609.34, "pies": 5280, "kilometros": 1.60934}
        },
        "temperatura": {
            "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
            "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9, "kelvin": lambda f: (f - 32) * 5/9 + 273.15},
            "kelvin": {"celsius": lambda k: k - 273.15, "fahrenheit": lambda k: (k - 273.15) * 9/5 + 32}
        },
        "masa": {
            "kilogramos": {"libras": 2.20462, "gramos": 1000, "onzas": 35.274},
            "libras": {"kilogramos": 0.453592, "gramos": 453.592, "onzas": 16},
            "gramos": {"kilogramos": 0.001, "libras": 0.00220462, "onzas": 0.035274},
            "onzas": {"kilogramos": 0.0283495, "libras": 0.0625, "gramos": 28.3495}
        },
        "velocidad": {
            "kmh": {"mps": 0.277778, "mph": 0.621371},
            "mps": {"kmh": 3.6, "mph": 2.23694},
            "mph": {"kmh": 1.60934, "mps": 0.44704}
        }
    }

    if categoria not in conversiones:
        return "Categoría no válida."

    if unidad_origen not in conversiones[categoria]:
        return f"La unidad de origen '{unidad_origen}' no es válida en la categoría '{categoria}'."
    
    if unidad_destino not in conversiones[categoria][unidad_origen]:
        return f"La unidad de destino '{unidad_destino}' no es válida para la unidad de origen '{unidad_origen}'."
    
    conversion = conversiones[categoria][unidad_origen][unidad_destino]
    if callable(conversion):
        return conversion(valor)
    else:
        return valor * conversion

def main():
    print(Fore.CYAN + Style.BRIGHT + "Bienvenido al conversor de unidades.")
    print(Fore.YELLOW + "Categorias disponibles: distancia, temperatura, masa, velocidad.")
    categoria = input(Fore.GREEN + "¿Qué quieres convertir? ").lower()

    if categoria not in ["distancia", "temperatura", "masa", "velocidad"]:
        print(Fore.RED + "Categoría no válida. Intenta de nuevo.")
        return

    try:
        valor = float(input(Fore.GREEN + "Introduce el valor a convertir: "))
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un número válido.")
        return

    unidad_origen = input(Fore.GREEN + "Introduce la unidad de origen: ").lower()
    unidad_destino = input(Fore.GREEN + "Introduce la unidad de destino: ").lower()

    resultado = convertir(valor, categoria, unidad_origen, unidad_destino)
    
    print(Fore.CYAN + f"El resultado es: {resultado}")

print("Ejecutando script...")  

if _name_ == "_main_":
    main()
