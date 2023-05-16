diccionario = {
    "nombre": "carlos",
    "apellido":"perez",
    "edad":21,
    "estatura":1.64
}

#+ Recorriendo un diccionario para obtener las claves
for key in diccionario:
    print(f"La key es: {key}")

#* Usando for para iterar en un diccionario, usando items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"La key es: {key} y el valor es: {valor}")