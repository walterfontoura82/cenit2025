'''
12-Crea una función llamada convertir_temperatura que tome una temperatura
en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
es: Fahrenheit = (Celsius * 9/5) + 32.
'''

def convertir_temperatura(grados):
    fahren = grados * (9/5) + 32
    return fahren
# Main

grados = int(input("Ingrese la temperatura a convertir: "))
res = convertir_temperatura(grados)
print(f"La temperatura en Grados Fahrenheit es: {res}")
    