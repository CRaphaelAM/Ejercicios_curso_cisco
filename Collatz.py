
y = "y"

while y == "y":
    correcto = False

    while not correcto:
        c0 = int(input("Ingrese un numero: "))
        if c0 <= 1:
            print("Ingrese un numero correcto.")
        else: correcto = True

    pasos = 0
    while c0 > 1:
        c0 = c0 // 2 if c0%2 == 0 else 3 * c0 + 1
        print("c0: ",c0)
        pasos+=1
    print("Pasos: ",pasos)
    y = input("Repetir?: ")
