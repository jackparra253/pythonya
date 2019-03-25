#Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo)
# Cargar por teclado el valor numérico del día, mes y año. Ejemplo: dia:10 mes:2 año:2018

mensaje_entrada = "Ingrese los datos correspondientes al primer trimestre del año (enero, febrero o marzo). "
mensaje_dia = "Ingrese el día. "
mensaje_mes = "Ingrese el mes."
mensaje_anio = "Ingrese el año. "

print(mensaje_entrada)

dia = int(input(mensaje_dia))
mes = int(input(mensaje_mes))
anio = int(input(mensaje_anio))

mensaje_salida = "corresponde al primer trimestre del año (enero, febrero o marzo)"

if dia >= 1 and dia <= 30 and mes == 1 or mes == 3:
    print(mensaje_salida)
else:
    if dia >= 1 and dia <= 28 and mes == 2:
        print(mensaje_salida)
    else:
        mensaje_error = "Fechas fuera de rango."
        print(mensaje_error)
