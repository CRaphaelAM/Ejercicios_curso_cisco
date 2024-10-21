"""
Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:


###
# #
###
# #
###

"""
combinaciones = [["###","# #","# #","# #","###"],["  #","  #","  #","  #","  #"],["###","  #","###","#  ","###"],["###","  #","###","  #","###"],
                ["# #","# #","###","  #","  #"],["###","#  ","###","  #","###"],["###","#  ","###","# #","###"],["###","  #","###","  #","  #"],
                ["###","# #","###","# #","###"],["###","# #","###","  #","  #"]]

def leds(cadena):
    final = []
    for elemento in cadena:
        mostrar = "\n".join(combinaciones[int(elemento)])
        final.append(mostrar)
    print(" ".join(final))

cadena = input("Ingrese el numero: ")
leds(cadena)
