#Accesando al archivo con with open
with open("lectura_archivos/archivo.txt") as archivo:
    #% Leemos el archivo
    contenido = archivo.read()
    
    #* Mostramos el contenido del archivo
    print(contenido)
    
#! Con with open no es necesario cerrar el archivo 