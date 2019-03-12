# Calcular el sueldo mensual de un operario conociendo la cantidad de horas 
# trabajadas y el valor por hora. 

cantidad_horas = input("Ingrese la cantidad de horas del empleado: ")
cantidad_horas = int(cantidad_horas)

valor_hora = input("Ingrese el valor de la hora: ")
valor_hora = int(valor_hora)

sueldo_diario = cantidad_horas * valor_hora
cantidad_dias = 30
sueldo_mensual  = sueldo_diario * cantidad_dias

print("El salario mensual es:" )
print(sueldo_mensual)