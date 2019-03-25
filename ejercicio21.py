# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

mensaje_inicial = "Ingrese una fecha"
print(mensaje_inicial)

mensaje_dia = "Ingrese el día: "
mensaje_mes = "Ingrese el mes: "
anio = "Ingrese el año: "

dia = int(input(mensaje_dia))
mes = int(input(mensaje_mes))
anio = int(input(anio))

mensaje_salida = "La fecha corresponde a navidad. "

if dia == 25 and mes == 12:
    print(mensaje_salida)
else:
    mensaje_validacion = "La fecha no corresponde a navidad. "
    print(mensaje_validacion)