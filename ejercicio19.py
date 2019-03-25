#Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor

mensaje = "Ingrese un número "

numero_uno = int(input(mensaje))
numero_dos = int(input(mensaje))
numero_tres = int(input(mensaje))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print(numero_uno)
else:
    if numero_dos > numero_uno and numero_dos > numero_tres:
        print(numero_dos)
    else:
        if numero_tres > numero_dos and numero_tres > numero_uno:
            print(numero_tres)
