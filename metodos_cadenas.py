cadena = "jfkdlafjk"
cadena1 = "hola soy Carlos"
cadena2 = "Bienvenido"
cadnum = 123456789

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

#* count() -> cuenta las coincidencias de una cadena en otra
#* devuelve la cantidad de veces que coincida
contar_coincidencia = cadena1.count("a")

#! len -> cuenta cuantos caracteres tiene una cadena
#! es una funcion, solo funciona con strings
contar_caracteres = len(cadena1)

#& startswith -> verifica si una cadena empieza con otra cadena dada 
#& devuelve valor booleano
empieza_con = cadena1.startswith("ho")

#% endswith -> verifica si una cadena termina con otra cadena dada 
#% devuelve valor booleano
termina_con = cadena1.endswith("os")

#^ replace -> reemplaza un pedazo de cadena por otra dada
#^ en caso de no encontrar la coincidencia deja la anterior
cadena_nueva = cadena1.replace("la", "lu")

#+ split -> separa cadenas con la cadena que pasemos
#+ devuelve una lista 
cadena_separada = cadena1.split(" ")

print(cadena_separada)
