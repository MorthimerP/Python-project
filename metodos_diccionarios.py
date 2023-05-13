# creando un diccionario
diccionario = {
    "nombre": "carlos",
    "apellido": "perez",
    "edad": 21,
    "estatura": 1.64 ,
    "eliminar": 0 
}

#! keys -> devuelve las claves en un objeto dict_item
#! tambien sirve para iterar
claves = diccionario.keys()

#? get -> pasar por parametro la clave y devuelve el valor
#? si no encuentra el parametro, devuelve "none"
valor_de = diccionario.get('apellido')

#^ pop -> elemina un elemento del diccionario
diccionario.pop("eliminar")

#% items -> obtiene el elemento dict_items iterable
diccionario_iterable = diccionario.items()

#* clear -> elimina todos los elementos del diccionario
diccionario.clear()

print(diccionario)