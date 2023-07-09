numeros = [1,2,3,4,5,6,7]

# Lambda crea funcniones anonimas
mul_x2 = lambda x : x*2

#* Creando funcion comun para decir si es par o no
def espar(num):
    if num % 2 == 0:
        return True

#^ Usando filter con una funcion comun
num_pares = filter(espar,numeros)

#+ Creando lo mismo que antes pero con lambda
num_pares2 = filter(lambda numero: numero % 2 == 0,numeros)

print(list(num_pares2))