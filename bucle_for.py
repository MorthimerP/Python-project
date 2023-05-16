# Crear una lista
animales = ["gato", "perro", "loro", "cocodrilo","pez"]
numeros = [12,54,23,87,46]

#^ Recorriendo la lista animales
for animal in animales:
    print(f"La variable animal equivale a: {animal}")
    
#+ Recorriendo la lista numeros y realizando operaciones con ellos
for numero in numeros:
    res = numero * 10
    print(res)
    
#% Recorriendo dos for al mismo tiempo, ambas listas deben tener el mismo tamaño
for numero,animal in zip(numeros,animales):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")    
    
#! Usando range() en for
#! 1 parametro -> empieza de 0 hasta el parametro
#! 2 parametros -> empieza del parametro1 al parametro2
for num in range(1,50):
    print(num)
    
#* Forma de recorrer una lista con su indice con enumerate() -> devuelve una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"Indice: {indice}, valor: {valor}")

#? Usando for-else 
for numero in numeros:
    print(f"Valor actual: {numero}")
#& El else se muestra una vez y al final del bucle
else:
    print("Bucle terminado")
    
#+ TODO LO ANTERIOR FUNCNIONA IGUAL TANTO PARA LISTAS COMO PARA TUPLAS Y CONJUNTOS