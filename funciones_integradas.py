#variables
numeros = [1,2,5,7,53,57,12,1234,8765,322,3455,1.1]

#! Encontrando el numero mas alto
num_max = max(numeros) 

#? Encontrando el numero menor 
num_min = min(numeros)

#* Redondeando a 6 decimales
num = round(3.141625,4)

#^ Obteniendo un resultado booleano
#^ False -> 0,vacion,False,None
res_bool = bool(-1)

#% Obteniendo un True con all()
#% True -> Si todos los valores son verdaderos
res_all = all([12,46,True,"fjkds",[54,67,3]])

#+ Sumando todos los valores de un iterable, solo numeros
total = sum(numeros)

print(total) 
