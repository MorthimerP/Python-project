# Datos dados
minimo = 2.5
promedio = 4
maximo = 7

#! Dato actual
actual = 1.5

#? a) diferencia en porcentaje entre actual y dados

#? porcentajes datos dados
d_min = (minimo*100)/maximo
d_prom = (promedio*100)/maximo

d_actual = (actual*100)/maximo

#* diferencias de porcentajes
dif_act_min = d_min - d_actual
dif_act_prom = d_prom - d_actual
dif_act_max = 100 - d_actual  

print("Diferencia en porcentaje del actual al maximo: {:.2f}%".format(dif_act_max))
print("Diferencia en porcentaje del actual al promedio: {:.2f}%".format(dif_act_prom))
print("Diferencia en porcentaje del actual al min: {:.2f}%".format(dif_act_min))