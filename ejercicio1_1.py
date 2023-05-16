# Datos dados
minimo = 2.5
promedio = 4
maximo = 7

#! Dato actual
actual = 1.5

#? a) diferencia en porcentaje entre actual y dados

#? porcentajes datos dados
d_min = (actual*100)/minimo
d_prom = (actual*100)/promedio

d_actual = (actual*100)/maximo

#* diferencias de porcentajes
dif_act_min = 100 - d_min 
dif_act_prom = 100 - d_prom
dif_act_max = 100 - d_actual  

print("Diferencia en porcentaje del actual al maximo: {:.2f}%".format(dif_act_max))
print("Diferencia en porcentaje del actual al promedio: {:.2f}%".format(dif_act_prom))
print("Diferencia en porcentaje del actual al min: {:.2f}%".format(dif_act_min))

#^ b) porcentaje de material inservible reducido en pormedio y actual
crudo1 = 5
crudo2 = 3.5

d_crudo1 = (promedio*100)/crudo1
d_crudo2 = (actual*100)/crudo2

p_crudo1_prom = 100 - d_crudo1 
p_crudo2_actual = 100 - d_crudo2 

print("Porcentaje de material inservible entre crudo 1 y promedio: {:.2f}%".format(p_crudo1_prom))
print("Porcentaje de material inservible entre crudo 2 y actual: {:.2f}%".format(p_crudo2_actual))

#% c) 10 horas del actual a cuantas equivale de los otros cursos y al reves
horas = 10

eq_act_min = (horas*minimo)/actual
eq_act_prom = (horas*promedio)/actual
eq_act_max = (horas*maximo)/actual

eq_min_act = (horas*actual)/minimo
eq_prom_act = (horas*actual)/promedio
eq_max_act = (horas*actual)/maximo

print("10 horas del actual equivalen a {:.2f} horas del minimo y al reves equivalen a {:.2f} horas".format(eq_act_min,eq_min_act))
print("10 horas del actual equivalen a {:.2f} horas del promedio y al reves equivalen a {:.2f} horas".format(eq_act_prom,eq_prom_act))
print("10 horas del actual equivalen a {:.2f} horas del maximo y al reves equivalen a {:.2f} horas".format(eq_act_max,eq_max_act))
