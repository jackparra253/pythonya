# Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda
# "Todos los números son menores a diez".
diez = 10

mensaje = "Ingrese un número: "
numero_uno = int(input(mensaje))
numero_dos = int(input(mensaje))
numero_tres = int(input(mensaje))

if numero_uno < diez and numero_dos < diez and numero_tres < diez:
    mensajde_salida = "Todos los números son menores a diez"
    print(mensajde_salida)