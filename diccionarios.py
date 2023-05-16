# Creando diccionarios con dict()
diccionario = dict(nombre = "carlos", apellido = "perez", edad = 21)

#? Las listas no pueden ser claves y en caso de querer meter conjuntos usamos frozenset
diccionario1 = {frozenset(["carlos","perez"]):"alumno"}

#* Creando diccionario con todos los valores None, usando fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","edad","estatura","promedio"])

#* fromkeys("Dato_a_iterar","Dato_a_igualar")
diccionario = dict.fromkeys("nombre","valor")


print(diccionario)
