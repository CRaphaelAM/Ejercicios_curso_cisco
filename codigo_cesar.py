"""Ya estás familiarizado con el cifrado César, y es por eso que queremos que mejores el código que te mostramos recientemente.

El cifrado César original cambia cada carácter por otro a se convierte en b, z se convierte en a, y así sucesivamente. Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga del rango 1..25.

Además, dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas) y todos los caracteres no alfabéticos deben permanecer intactos.

Tu tarea es escribir un programa el cual:

    Le pida al usuario una línea de texto para encriptar.
    Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
    Imprime el texto codificado. 

Prueba tu código utilizando los datos que te proporcionamos.

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
    
"""

def cifrado():
    mensaje_cifrado = ""

    for char in mensaje:
        if not char.isalpha():
            mensaje_cifrado += char
        elif char.isupper() :
            if ord(char) + int(desplazamiento) > ord("Z"):
                resto = ord(char) + int(desplazamiento) - ord("Z")
                code = ord("A")-1 + resto
            else: code = ord(char) + int(desplazamiento)
            mensaje_cifrado += chr(code)
        else:
            if ord(char) + int(desplazamiento) > ord("z"):
                resto = ord(char) + int(desplazamiento) - ord("z")
                code = ord("a")-1 + resto
            else: code = ord(char) + int(desplazamiento)
            mensaje_cifrado += chr(code)
    
    return mensaje_cifrado

def descifrado():
    mensaje_descifrado = ""
    
    for char in mensaje:
        if not char.isalpha():
            mensaje_descifrado += char
        elif char.isupper() :
            if ord(char) - int(desplazamiento) < ord("A"):
                resto = ord("A") - (ord(char) - int(desplazamiento))
                code = ord("Z")+1 - resto
            else: code = ord(char) - int(desplazamiento)
            mensaje_descifrado += chr(code)
        else:
            if ord(char) - int(desplazamiento) < ord("a"):
                resto = ord("a")- ord(char) + int(desplazamiento) 
                code = ord("z")+1 - resto
            else: code = ord(char) - int(desplazamiento)
            mensaje_descifrado += chr(code)
    
    return mensaje_descifrado

    pass


continuar = True
while continuar:
    opcion = input("Presione 1 para cifrar un mensaje. \nPresione 2 para descifrar un mensaje.\nPresione 3 para salir.\n\tOpcion: ")
    match opcion:
        case "1":
            error = True
            while error:
                try:
                    desplazamiento = input("Cuánto desea desplazar el codigo: ")
                    if  25 >= int(desplazamiento) >= 1:
                        error = False
                    else: print("El número ingresado está fuera de rango.")
                except:
                    print("Ha ocurrido un error con el numero ingresado.")
                    error = True
            
            mensaje = input("Ingrese el mensaje: ")
            mensaje_cifrado = cifrado()
            print(f"Aquí está su mensaje: {mensaje_cifrado}")
        case "2":
            error = True
            while error:
                try:
                    desplazamiento = input("Cuánto se ha desplazado el codigo: ")
                    if  25 >= int(desplazamiento) >= 1:
                        error = False
                    else: print("El número ingresado está fuera de rango.")
                except:
                    print("Ha ocurrido un error con el numero ingresado.")
                    error = True
            
            mensaje = input("Ingrese el mensaje cifrado: ")
            mensaje_descifrado = descifrado()
            print(f"Aquí está su mensaje: {mensaje_descifrado}")
        case "3": 
            print("Hasta Luego") 
            continuar = False
        case _: print(f"{opcion}: No es una opcion valida.")
