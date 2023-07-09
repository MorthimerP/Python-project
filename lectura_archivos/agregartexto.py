with open("lectura_archivos/agregartexto.txt", "a", encoding="utf-8") as f:
    f.write("\n")
    #* Usando un bucle para agregar lineas
    for i in range(5):
        f.write(f"Linea {i} agregada \n")