#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

mensaje = "Ingrese un número: "

primer_numero = int(input(mensaje))
segundo_numero = int(input(mensaje))
tercer_numero = int(input(mensaje))

if(primer_numero > segundo_numero and primer_numero > tercer_numero):
    print(primer_numero)
else :
    if segundo_numero > primer_numero and segundo_numero > tercer_numero:
        print(segundo_numero)
    else:
        if(tercer_numero> primer_numero and tercer_numero> segundo_numero):
            print(tercer_numero)
