#  Escribir un programa en el cual se ingresen cuatro numeros, 
# calcular e informar la suma de los dos primeros y el producto del tercero
#  y el cuarto.

primer_numero = input("Ingrese el primer numero: ")
primer_numero = int(primer_numero)
segundo_numero = input("Ingrese el segundo numero: ")
segundo_numero = int(segundo_numero)
tercer_numero = input("Ingrese el tercer numero: ")
tercer_numero = int(tercer_numero)
cuarto_numero = input("Ingrese el cuarto numero: ")
cuarto_numero = int(cuarto_numero)

suma = primer_numero + segundo_numero

producto = tercer_numero * cuarto_numero

print "La suma del primer numero y el segundo numero es: " + str(suma)
print "El producto del terce y cuarto numero es: " + str(producto)
