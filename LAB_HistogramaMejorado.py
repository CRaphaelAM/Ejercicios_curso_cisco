"""
El código anterior necesita ser mejorado. Está bien, pero tiene que ser mejor.

Tu tarea es hacer algunas enmiendas, que generen los siguientes resultados:

    El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero).
    El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión '.hist' (debe concatenarse con el nombre original).

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