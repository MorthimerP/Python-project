#Serie fibonacci 
numero = int(input("Introduce un numero: "))

def serie_f(numero):
    a,b = 0,1
    serie = []
    for i in range(numero):
        if b > numero: return serie
        else: 
            serie.append(b)
            a,b = b,a+b
           
lista = serie_f(numero)
print(lista)
        