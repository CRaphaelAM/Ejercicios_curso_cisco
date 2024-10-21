"""
Este programa determina si dos frases ingresadas por teclado son anagramas
"""

def es_anagrama(cadena1,cadena2):
    cadena1_aux = cadena1.replace(" ","")
    cadena2_aux = cadena2.replace(" ","")
    if len(cadena1_aux) != len(cadena2_aux):
        return False
    for char in cadena1_aux:
        if not char.isalpha():
            return False
        
        if char in cadena2_aux:
            if cadena2_aux.count(char) != cadena1_aux.count(char):
                return False
    return True

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if es_anagrama(cadena1.lower(),cadena2.lower()):
    print(f"{cadena1} y {cadena2} son anagramas.")
else: print(f"{cadena1} y {cadena2} no son anagramas.")
        