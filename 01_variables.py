var_str = "Variable tipo string"
var_int = 3
var_bool = False

print(var_str)
print(var_int)
print(var_bool)

var_int_to_str = str(var_int)
print(type(var_int_to_str))

#^ Concatenacion de variables en print
print(var_int_to_str,var_bool,var_str)

#! Funcion len
print(len (var_int_to_str))
#+ print("\n")
print(len(var_str))
#& len solo funciona con variables string

# Variables en una sola linea, de cualquier tipo
name,username,age,yesorno = "Morthi","Primehunter",20,False
print("Nombre:",name,username,"\nEdad:",age,"\nPermiso:",yesorno)

# Si funciona el salto de linea "\n"

#? Introducir valores en variables
nombre = input("Nombre: ")
edad = input("Edad: ")

print(nombre)
print(edad)