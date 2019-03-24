#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje
# indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.

mensaje = "Ingrese un número entero positivo de hasta tres cifras."
numero = int(input(mensaje))

if numero > 0 and numero <= 9:
    print("El número tine una cifra.")
else:
    if numero >= 10 and numero <= 99:
        print("El número tine dos cifras.")
    else:
        if numero >= 100 and numero <= 999:
            print("El número tine tres cifras.")
        else:
            if numero> 999:
                print("el número de cifras es mayor")
            else:
                print("el número debe ser positivo")