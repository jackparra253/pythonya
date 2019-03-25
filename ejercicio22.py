# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y
# a este resultado se lo multiplica por el tercero.

mensaje = "Ingrese un número: "
numero_uno = int(input(mensaje))
numero_dos = int(input(mensaje))
numero_tres = int(input(mensaje))

if numero_uno == numero_dos and numero_uno == numero_tres:
    suma = numero_uno + numero_dos
    print(suma)
    producto = suma * numero_tres
    print(producto)