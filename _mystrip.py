
def my_strip(strng):
    lista = []
    cadena_aux =""

#    if len(strng) < 1:
#        return lista
#    else:
#       for i in range(len(strng)):
#            if strng[i].isalpha():
#                cadena_aux += strng[i]
#               print(f"i-> {i}\tstring[i]-> {strng[i]} cadena_aux = {cadena_aux}")
#            elif cadena_aux != "":
#                print(f"Entramos al elif porque strng[{i}] = {strng[i]} y ahora cadena_aux = {cadena_aux}")
#                lista.append(cadena_aux)
#                print(f"La lista despues de añadir cadena_aux: {lista}")
#                cadena_aux = ""
#            else: continue
#    print(cadena_aux)
#   return lista

    if len(strng) < 1:
        return lista
    else:
        for char in strng:
            if char.isalpha():
                cadena_aux += char
                print(f"string[i]-> {char} cadena_aux = {cadena_aux}")
            elif cadena_aux != "":
                print(f"Entramos al elif porque el caracter es = {char} y ahora cadena_aux = {cadena_aux}")
                lista.append(cadena_aux)
                print(f"La lista despues de añadir cadena_aux: {lista}")
                cadena_aux = ""
            
    lista.append(cadena_aux)
    return lista


cadena = "Ser o no ser, esa es la cuestión"

print(my_strip(cadena))


