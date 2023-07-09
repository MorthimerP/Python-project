#Acceso al archivo txt con open y asignando a variable, incluyendo la condificacion utf-8
archivo_sin_leer = open("lectura_archivos/archivo.txt",encoding="utf-8")

#! Leer el archivo en su totalidad
#archivo = archivo_sin_leer.read()

#? Leer linea por linea
#? Devuelve una lista con las lineas del txt
#lineas = archivo_sin_leer.readlines()

#& Leer una sola linea
#& sin un numero como parametro, lee la primer linea completa
#& con un numero como parametro n, lee los n caracteres de la primer linea
linea = archivo_sin_leer.readline()

#+ Cerrar archivo
archivo_sin_leer.close()

#print(archivo)
print(linea)