'''
13-Crea una función llamada calcular_descuento que tome dos parámetros:
precio y porcentaje_descuento. La función debe calcular y devolver el precio
después de aplicar el descuento.

'''

def calcular_descuento(precio,porcentaje):
    precio_final = precio -  (precio * porcentaje)/100
    return precio_final

#Main
precio = int(input("Ingrese el precio a calcular el descuento: "))
porcentaje = int(input("Ingrese el porcentae a descontar: "))
res = calcular_descuento(precio, porcentaje)
print(f"El precio con el descuetos es: {res}")