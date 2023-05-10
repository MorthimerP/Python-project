edad = 19
if edad >= 18:
    print("Puedes pasar")
else:
    print("No puedes pasar")

print("Esto no forma parte de la condicion")

contraseña_almacenada = "Password1"
contraseña_escrita = "Password1"

if contraseña_almacenada == contraseña_escrita:
    print("Iniciando sesion")
else :
    print("Contraseña Incorrecta")

#+ if anidado
ingreso_mensual = 8000
gasto_mensual = 7000
if ingreso_mensual > 2000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("Todo correcto")
    else:
        print("Estas gastando mucho")

elif ingreso_mensual > 50000:
    print("Puedes vivir en cualquier parte del mundo")
    
else: 
    print("No tienes bases economicas estables")