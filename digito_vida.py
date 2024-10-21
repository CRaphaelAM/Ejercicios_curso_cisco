"""
Programa que calcula el digito de la vida.
Este digito se calcula sumando los digitos de la fecha de nacimiento de cada persona
La fecha debe estar en formato yyyy/mm/dd


25 % 10 = 2,5   10%10

"""

def calcular_digito(cadena):
    suma = 0
    str_suma = cadena[:]
    while(len(str_suma)>1):
        for char in str_suma:
            suma+= int(char)
        str_suma = str(suma)
        suma = 0

    return str_suma

def validar_entrada(cadena):
    error  = True
    
    if len(cadena)>8 or len(cadena)<6:
        print("El formato de la fecha no es valido: ")
        return error
    else:
        for char in cadena:
            if not char.isdigit():
                print("Ingreso caracter no numericos")
                return error
    return False

cadena=input("Ingrese la fecha de nacimiento: ")
while validar_entrada(cadena):
    cadena=input("Ingrese la fecha de nacimiento: ")
    
print(f"El número de la vida correspondiente a la fecha *{cadena}* es {calcular_digito(cadena)}")
