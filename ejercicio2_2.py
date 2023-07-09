# Crear funcion que al pasarle un numero muestre los numeros primos anteriores a él 
numero = int(input("Introduce un numero: "))

#! Creando una funcion booleana que verifique si un numero es primo 
def es_primo(numero):
    #? Verificamos que el numero sea mayor a 1
    if numero > 1:
        #* Verificamos que el numero no pueda dividirse entre 2 y el mismo -1
        for i in range(2,numero-1):
            #^ Si retorna false el numero es compuesto
            if numero % i == 0: return False
        #+ Si retorna true el numero es primo
        return True
    else:
        print("Error: Numero menor o igual a cero")
        return False
    
#% Funcion para imprimir los numeros primos
def num_primos(numero):
    #& Lista donde guardar los numero primos
    primos = []	
    #, Ciclo para verificar si un numero es primo desde el cero hasta el numero
    for n in range(2,numero+1):
        if es_primo(n):
            #! Si es primo lo agrega a la lista
            primos.append(n)
    #? Imprime la lista
    print(primos)
    
num_primos(numero)

#+ En una linea
primos = lambda num : list(filter(lambda x: all(x % i != 0 for i in range(2,int(x ** .5)+1)), range(2,num)))
print(primos(numero))