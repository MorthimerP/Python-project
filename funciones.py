#Creando una funcion simple
def saludo():
    print("Hola usuario")
    
#+ Ejecutando la funcion simple
saludo()

#& Creando una funcion con parametros
def hola(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adj = "usuaria"
    elif sexo == "hombre":
        adj = "usuario"
    else:
        adj = "otro"
    print(f"Hola {adj}, tu nombre es: {nombre} como estas? ")
    
hola("carlos","HOMBRE")

#* Creando una funcion que retorne valores
def crear_contraseña(num):
    caracteres = "abcdef"
    num_int = str(num)
    num = int(num_int[0])
    c1 = num -2
    c2 = num +1  
    c3 = num -3
    contraseña = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num*2}"
    return (contraseña,num) #^ Opcional poner parentesis de tupla
 
#% Desempaquetando la funcion   
password,new_num = crear_contraseña(3)

print(f"Tu nueva contraseña es: {password}")
print(f"El numero utilizado fue: {new_num}")

#! Usando el parametro args
#! En caso de pasar otro parametro, el *args tiene que ser el ultimo
def suma(nombre,*numeros):
    return f"Hola {nombre} la suma total es: {sum(numeros)}"

resultado = suma("Carlos",1,2,3,4,5,6,7,8,9,10,)
print(resultado)

#? Forma 2 de hacer la suma anterior
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([1,2,3,4,5,6,7])

print(resultado2)

#+ Utilizando keyword arguments
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_res = frase(adjetivo="chistoso",nombre="carlos",apellido="perez")
print(frase_res)

#^ Creando la misma funcion con parametro opcional y un valor por defecto
def frase(nombre, apellido,adjetivo = "loco"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_res2 = frase("carlos", "perez", "chistoso")
print(frase_res2)