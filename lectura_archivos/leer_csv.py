import csv

with open("lectura_archivos/datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)