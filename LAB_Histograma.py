"""
Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos saber con qué frecuencia aparece cada letra en el texto. Tal análisis puede ser útil en criptografía, por lo que queremos poder hacerlo en referencia al alfabeto latino.

Tu tarea es escribir un programa que:

    Pida al usuario el nombre del archivo de entrada.
    Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan como iguales).
    Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).

Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.



Programa que calcula la cantidad de ocurrencias de las letras de un archivo de texto.
"""

def contador_letras(line: list[str]) -> None:
    """
    Cuenta las apariciones de las letras e incrementa el contador asociado a cada letra en el diccionario

    Argumentos: Una cadena de caracteres
    Devuelve: None
    """
    
    for char in line.lower():
        if char in letras.keys():
            letras[char] += 1


def main() ->None:
    try:
        with open ("./ejemplo.txt","r") as in_file:
            for line in in_file:
                contador_letras(line)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    for k,d in letras.items():
        if d != 0:
            print(f"{k} -> {d}")

letras: dict[str] = {
    "a": 0,    "b": 0,    "c": 0,    "d": 0,    "e": 0,    "f": 0,    "g": 0,
    "h": 0,    "i": 0,    "j": 0,    "k": 0,    "l": 0,    "m": 0,    "n": 0,
    "o": 0,    "p": 0,    "q": 0,    "r": 0,    "s": 0,    "t": 0,    "u": 0,
    "v": 0,    "w": 0,    "x": 0,    "y": 0,    "z": 0     
    }

if __name__ == "__main__":
    main()