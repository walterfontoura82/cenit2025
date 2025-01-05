'''
11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.
12-Crea una función llamada convertir_temperatura que tome



'''
def contar_vocales(text):
    cant_vocales = 0
    l_vocales = "aeiou"
    for x in text:
        if x in l_vocales:
            cant_vocales += 1
    return cant_vocales


# Main
texto = input("Ingrese un texto para contar vocales: ")
texto = texto.lower()
res = contar_vocales(texto)
print(f"La cantidad de vocales que tiene el texto es: {res}")