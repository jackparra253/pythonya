# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información:
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente.
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según
# el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
#
# Nivel máximo:	Porcentaje>=90%.
# Nivel medio:	Porcentaje>=75% y <90%.
# Nivel regular:	Porcentaje>=50% y <75%.
# Fuera de nivel:	Porcentaje<50%.

cantidad_preguntas_realizadas = int(input("Ingrese la cantidad de preguntas. "))
cantidad_respuestas_correctas = int(input("Ingrese la cantidad de respuestas correctas. "))

porcentaje = (cantidad_respuestas_correctas * 100) / cantidad_preguntas_realizadas

if porcentaje < 50:
    print("Fuera de nivel")
else:
    if porcentaje >= 50 and porcentaje < 75:
        print("Nivel regular")
    else:
        if porcentaje >= 75 and porcentaje < 90:
            print("Nivel medio")
        else:
            if porcentaje >= 90:
                print("Nivel máximo")