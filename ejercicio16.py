#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

mensaje = "Ingrese un número: "

numero = int(input(mensaje))

if numero < 0:
    print("El numero es negativo.")
else:
    if  numero == 0:
        print("El número es cero.")
    else:
        print("El numero es positivo.")