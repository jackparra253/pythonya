#  De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

sueldo = int(input("Ingrese el sueldo del empleado: "))
antiguedad = int(input("Ingrese la cantidad de años de antiguedad del empleado: "))

if sueldo < 500 and antiguedad >= 10:
    aumento_antiguedad_mayor_igual_diez_anios = sueldo * 0.20
    print(sueldo + aumento_antiguedad_mayor_igual_diez_anios)
else:
    if sueldo < 500 and antiguedad < 10:
        aumento_antiguedad_menor_diez_anios = sueldo * 0.5
        print(sueldo + aumento_antiguedad_menor_diez_anios)
    else:
        if sueldo >= 500:
            print(sueldo)
