# No asistio el profesor, los alumnos daran la clase
def obtener_compañeros(cantidad_compañeros):
    #^ Creamos lista de los compañeros
    compañeros = []
    
    #* Pedimos la informacion en un for
    for i in range(cantidad_compañeros):
        nombre = input("Introduce tu nombre: ")
        edad = int(input("Introduce tu edad: "))
        compañero = nombre,edad
        
        #% Agregando la informacion a la lista
        compañeros.append(compañero)
        
    #& Ordenando de menor a mayor segun la edad  
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(5)

print(f"El profesor es: {profesor}")
print(f"El asistente es: {asistente}")
