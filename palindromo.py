"""
Programa que determina si una cadena de texto ingresada por teclado es un palindromo
"""


#def es_palindromo(cadena):
#    cadena_sin_espacios = cadena.replace(" ","")
#    cadena_inversa = cadena_sin_espacios[::-1]
#    print(cadena_sin_espacios,"  ",cadena_inversa)
#    return cadena_sin_espacios == cadena_inversa


def es_palindromo(cadena):
    cadena_aux = cadena.replace(" ","")
    for i,char in enumerate(cadena_aux):
        cadenita = cadena_aux[-(i+1)]
        if char != cadena_aux[-(i + 1)]:
            return False
    return True


cadena = input("Ingresa la cadena de texto: ")

if es_palindromo(cadena.lower()):
    print("La cadena ingresada es un palindromo.")
else: print("La cadena ingresada no es un palindromo.")