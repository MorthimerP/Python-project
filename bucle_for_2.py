frutas = ["manzana", "pera", "naranja", "uva","mango"]
cadena = "Hola Carlos"
numeros = [1,3,7,3,8,5]

#^ Evitando una iteracion con continue
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"Me voy a comer una {fruta}")

#* Evitando que el bucle siga ejecutandose con break (else no se ejecuta)
for fruta in frutas:
    if fruta == "naranja":
        break
    print(f"Me voy a comer una {fruta}")
else:
    print(f"for terminado")
    
print(f"Bucle terminado")

#% Recorrer una cadena
for letra in cadena:
    print(letra)
    
#! for en una sola linea
numeros_duplicados = [a*2 for a in numeros]
print(numeros_duplicados)