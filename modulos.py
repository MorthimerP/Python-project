# Un modulo es cualquier archivo con punto py

#! Importando un modulo y nombrandolo de otra forma con "as"
#import modulo_saludar as m_saludar

#* Importando todo
#* Mala practica -> programa se sobrecarga
#from modulo_saludar import *  

#? importar solo una o varias funciones
#? para importar mas de dos, se usa una coma " , "
#? se le cambia el nombre solo a un funcion con "as" 
from modulo_saludar import saludar,saludar2 as saludando
saludo = saludar("morthi")
saludo2 = saludando("carlos")

#saludo = m_saludar.saludar("morthi")
print(saludo2)
print(saludo)