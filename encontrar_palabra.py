"""
Cadena que revisa una secuencia de caracteres y determina si la palabra escogida se encuentra
dentro de esa secuencia de caracteres
"""

def encontrar_palabra(cadena,palabra):
    ocurrencia = 0
    cadena = cadena.lower()
    palabra = palabra.lower()
    for char in palabra:
        ocurrencia = cadena.find(char,ocurrencia)
        if ocurrencia == -1: return False
    return True


cadena = input("Ingrese la cadena de texto: ")
palabra = input("Ingrese la palabra que desea buscar en el texto: ")

if encontrar_palabra(cadena,palabra):
    print(f"\"{palabra}\" Si esta en el texto")
else: print(f"No se pudo encontrar \"{palabra}\" en el texto")


