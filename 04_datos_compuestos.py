# Creando una lista que se puede modificar
lista = ["Carlos", "Morthimer", True, 21, 1.64]

#? Creando una tupla que no se puede modificar
#? Solo se puede redefinir 
tupla = ("Carlos", "Morthimer", True, 21, 1.64)

#* Esto es valido
print(lista)

lista[3] = "cambio"

print(lista)

#+ Creando un conjunto set
#+ Un set no se puede modificar solo redefinir (como una tupla)
#+ No deja acceder por indice
#+ No muestra valores repetidos (duplicados)
conjunto = {"Carlos", "Morthimer", True, 21, 1.64 }
print(conjunto) #* Imprime de forma desordenada

#! Creando un diccionario
#! Clave : valor <-> key : value
diccionario = {"nombre": "Carlos", "edad": 21, 3 : 1.64}

print(diccionario["edad"])
print(diccionario[3])

#~ Esto no es valido
#tupla[3] = "cambio"
#conjunto[3] = "cambio1"