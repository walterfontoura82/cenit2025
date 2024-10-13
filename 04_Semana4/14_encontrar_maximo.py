'''
14-Crea una función llamada encontrar_maximo que tome una lista de números
como parámetro y devuelva el número máximo de la lista.

'''
def crear_maximo(List_num):
    max = List_num[0]
    for num in List_num:
       if num > max:
           max = num
    print(f'El max es: {max}')
        
        
#Main
List_num = [1,2,3,4,5,156,7,8,9,10,11,12,13]
crear_maximo(List_num)
    