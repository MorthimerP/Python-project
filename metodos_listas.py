# Creando una lista con list
lista = list(["hola","carlos",21,1.64,True])
lista1 = list([23,63,220,987,True,False,2.5])

#! len -> cuenta la cantidad de elementos de una lista
cant_elementos = len (lista)

#? append -> agrega un elemento a la lista
#? solo agrega un elemento 
agregando_con_append = lista.append(123)

#* insert -> agrega un elemento a la lista en un indice especifico
#* insert(posicion, elemento)
lista.insert(2,"elemento insertado")

#^ extend -> agrega varios elementos a una lista
#^ los elementos a agregar deben ser dados en forma de lista
lista.extend([False,1,2,3,"abcd","texto agregado"])

#% pop -> elimina un elemnto de la lista
#% se especifica el elemento mediante el indice
#% para eliminar el ultimo elemento se pone el indice -1
lista.pop(-1)

#& remove -> remueve un elemento por su valor
#& busca en la lista el parametro dado y los elimina
lista.remove("abcd")

#! sort -> ordena los elementos de una lista de forma ascendente
#! no puede ordenar con cadenas de texto
#! parametro (reverse=True) ordena en reversa
lista1.sort()

#? reverse -> invierte los elementos de una lista
lista.reverse()

#* index -> busca una cadena en una lista
#* devuelve la posicion de la coincidencia
elemento_encontrado = lista.index("carlos")

#+ clear -> elimina todos los elementos de una lista
lista.clear()  

print(lista)