# Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

coordenada_x = int(input("Ingrese un valor para la coordenada x. "))
coordenada_y = int(input("Ingrese un valor para la coordenada y. "))

if coordenada_x > 0 and coordenada_y > 0:
    print("1º Cuadrante. ")
else:
    if coordenada_x < 0 and coordenada_y > 0:
        print("2° Cuadrante. ")
    else:
        if coordenada_x < 0 and coordenada_y < 0:
            print("3° Cuadrante. ")
        else:
            if coordenada_x > 0 and coordenada_y < 0:
                print("4° Cuadrante. ")