# Realizar la carga del precio de un producto y la cantidad a llevar. 
# Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del 
# producto)

precio_producto = input("Ingrese el precio de un producto ")
precio_producto = int(precio_producto)
cantidad = input("Cantidad a llevar ")
cantidad = int(cantidad)

valor_total = precio_producto * cantidad

print "Se debe pagar: " + str(valor_total)