import pandas as pd
df = pd.read_csv("lectura_archivos/datos.csv")

#! Cambiar el tipo de dato de una columna
df['edad'] = df["edad"].astype(str)

#? Reemplazar un dato de alguna columna por otro
df["nombre"].replace("carlos", "morthi",inplace=True)

#* Eliminar filas con datos faltantes 
#* Para eliminar columnas -> (axis=1)
df = df.dropna()

#^ Eliminando filas repetidas
df = df.drop_duplicates()

#% Creando un csv con el dataframe resultante
df.to_csv("lectura_archivos/datos_nuevos.csv")

print(df)