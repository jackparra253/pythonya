# Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10,
# imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

diez = 10

mensaje = "Ingrese un número: "
numero_uno = int(input(mensaje))
numero_dos = int(input(mensaje))
numero_tres = int(input(mensaje))

if numero_uno < diez or numero_dos < diez or numero_tres < diez:
    mensaje_salida = "Alguno de los números es menor a diez"
    print(mensaje_salida)