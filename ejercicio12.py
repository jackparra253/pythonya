#Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

mensaje_ingresar_nota = "Ingrese la nota del alumno: "

primera_nota = int(input(mensaje_ingresar_nota))
segunda_nota = int(input(mensaje_ingresar_nota))
tercera_nota = int(input(mensaje_ingresar_nota))

total_notas = primera_nota + segunda_nota + tercera_nota
cantidad_notas = 3
promedio = total_notas/3

mensaje_promocionado = "Promocionado"


if promedio >= 7:
    print(mensaje_promocionado)
