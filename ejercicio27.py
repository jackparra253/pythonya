#Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación
# (debe mostrar el mayor y el menor de ellos)

mensaje = "Ingrese un número: "
numero_uno = int(input(mensaje))
numero_dos = int(input(mensaje))
numero_tres = int(input(mensaje))

if  numero_uno > numero_dos and numero_uno > numero_tres and numero_dos > numero_tres:
    print("mayor")
    print(numero_uno)
    print(" menor ")
    print(numero_tres)
else:
    if numero_uno > numero_dos and numero_uno > numero_tres and numero_tres > numero_dos:
        print("mayor")
        print(numero_uno)
        print(" menor ")
        print(numero_dos)
    else:
        if numero_dos > numero_uno and numero_dos > numero_tres and numero_uno > numero_tres:
            print("mayor")
            print(numero_dos)
            print(" menor ")
            print(numero_tres)
        else:
            if numero_dos > numero_uno and numero_dos > numero_tres and numero_tres > numero_uno:
                print("mayor")
                print(numero_dos)
                print(" menor ")
                print(numero_uno)
            else:
                if numero_tres > numero_uno and numero_tres > numero_dos and numero_uno > numero_dos:
                    print("mayor")
                    print(numero_tres)
                    print(" menor ")
                    print(numero_dos)
                else:
                    print("mayor")
                    print(numero_tres)
                    print(" menor ")
                    print(numero_uno)

