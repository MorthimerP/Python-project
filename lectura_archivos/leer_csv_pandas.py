import pandas as pd
#? usamos la funcion read_csv para leer el archivo csv
df = pd.read_csv("lectura_archivos/datos.csv") 

#* Obteniendo los datos de la columna nombre
#print(df["nombre"])

cadena = "0123456789"
#^ Usando slicing ":" para recorrer una cadena en un rango especificado
#^ Posicion inicio si se incluye, final no
#print(cadena[3:7])

#! Ordenamos el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#+ Ordenando de forma descendente
df_orden_descendete = df.sort_values("edad",ascending=False)

#% Accediendo a la primeras filas con head()
fila1 = df.head(1)

#& Accediendo a las ultimas filas con tails()
fila2 = df.tail(1)

#, Accediendo a la cantidad de filas y columnas con shape
filas,columnas = df.shape

#? Obteniendo datos estadisticos del dataframe
df_info = df.describe()

#* Accediendo a un elemento especifico con loc[fila,columna]
elem_esp = df.loc[2,"edad"]

#^ Accediendo a un elemento especifico con iloc (usando indices)
elem_esp_iloc = df.iloc[2,2]

#!Accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#+ Accediendo a fila X con loc o  iloc
fila = df.loc[2,:]

#% Accediendo a filas con edad mayor a 30
fila_30 = df.loc[df["edad"]>30,:]

print(fila_30)