# 2 listas con nombres y apellidos
nombres = ["Carlos", "Luis", "Ailton", "Marifer","Jimena"]
apellidos = ["Perez", "Bernal", "Diaz","Pada","Salas"]

#* Registramos la informacion en un archivo txt
with open("ej_xt.txt", "w") as f:
    f.writelines("Los datos son: \n\n")
    [f.writelines(f"Nombre: {n} \nApellido: {a} \n -------- \n") for n,a in zip(nombres,apellidos)]