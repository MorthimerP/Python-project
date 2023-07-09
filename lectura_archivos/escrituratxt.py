with open ("lectura_archivos/archivo.txt", "w",encoding="utf-8") as f:
    #^ Sobreescribiendo el archivo
    #f.write("Texto agregado sobreescribiendolo")
    
    #+ La funcion writelines debe tener como parametro un iterable
    f.writelines(["Texto sobre escrito \n","Linea agregada"])