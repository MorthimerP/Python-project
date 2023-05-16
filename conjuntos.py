# Creando un conjunto con set
conjunto = set(["dato1",21,1.64])

#+ Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2",2023])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#* Teoria de conjuntos
conjunto1 = {1,2,3,4,5,6,7,8,9}
conjunto2 = {1,3,5,7,9}

#% Validando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#& Validando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#^ Verificando si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)