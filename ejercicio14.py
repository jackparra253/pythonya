#Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
#Si el promedio es >=7 mostrar "Promocionado".
#Si el promedio es >=4 y <7 mostrar "Regular".
#Si el promedio es <4 mostrar "Reprobado".

mensaje = "Ingrese la nota del alumno: "

primera_nota = int(input(mensaje))
segunda_nota = int(input(mensaje))
tercera_nota = int(input(mensaje))

total_notas = primera_nota + segunda_nota + tercera_nota
cantida_notas = 3
promedio = total_notas/cantida_notas

if promedio < 4:
    print("Reprobado")
else :
    if promedio >= 4 and promedio < 7:
        print("Regular")
    else:
        if promedio >= 7:
            print("Promocionado")


