#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número
# tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

mensaje = "Ingrese un número de uno o dos dígitos: "
numero = int(input(mensaje))
mensaje_un_digito = "El número tiene un dígito."

if numero > 0 and numero < 10:
    print(mensaje_un_digito)

mensaje_dos_digitos = "El número tiene dos dígitos."

if numero > 9 and numero < 100:
    print(mensaje_dos_digitos)