# Realizar un programa que lea cuatro valores numericos e informar su suma 
# y promedio. 

primer_numero = input("Ingrese el primer numero: ")
primer_numero = int(primer_numero)
segundo_numero = input("Ingrese el segundo numero: ")
segundo_numero = int(segundo_numero)
tercer_numero = input("Ingrese el tercer numero: ")
tercer_numero = int(tercer_numero)
cuatro_numero = input("Ingrese el cuarto numero: ")
cuatro_numero = int(cuatro_numero)

suma = primer_numero + segundo_numero + tercer_numero + cuatro_numero

promedio = suma / 4

print "La suma es: " + str(suma)

print "El promedio es: " + str(promedio)