#Ejercicio 2

#! a) 1 segundo = 2 palabras, cuantos segundo se diran x palabras
texto = input("Introduce un texto: ") 
lista = texto.split(" ")
tam_texto = len(lista)
tiempo_segundos = tam_texto / 2
print(f"El usuario dijo {tam_texto} palabras en {tiempo_segundos} segundos")

#? b) si tarda mas de 1 min (60 seg) decir que pare
if tiempo_segundos>60 :
    print("Alto, estas hablando mucho")
    
#+ c) si un usuario habla 30% mas rapido, que tiempo tardaria en decirlo
#+ .7 seg = 2 palabras

tiempo_usuario = (tam_texto * .7) / 2
print(f"El usuario dijo {tam_texto} palabras en {tiempo_usuario} segundos")
