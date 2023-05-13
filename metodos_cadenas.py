cadena = "jfkdlafjk"
cadena1 = "hola soy Carlos"
cadena2 = "Bienvenido"

#! funciones -> funcion()

#* metodos -> dato.metodo()
#* los metodos son funciones especificas de objetos

#? dir -> Devuelve la lista de atributos validos del objeto pasado
#? dir es una funcion
#print(dir(cadena1))
#print(dir(2))

#& upper -> Convierte a mayusculas
#& lower -> Convierte a minusculas
#& capitalize -> Primera en mayuscula

resultado = cadena1.upper()

#+ find -> Busqueda de algo en otra cosa
#+ -1 cuando no encuentra un valor (Case sensitive)
busqueda_find = cadena1.find("c")

#^ index -> buscar una cadena en otra cadena
#^ cuando no encuentra coincidencia lanza una excepcion
busqueda_index = cadena.index("j")

#% isnumeric -> consulta si una cadena es numerico
#% devuelve un valor booleano
es_numerico = cadena.isnumeric()

#! isalpha -> consulta si una cadena es alfanumerica
#! devuelve valor booleano
#! los espacios no son alfanumericos
es_alfanumerico = cadena.isalpha()

print(es_alfanumerico)
