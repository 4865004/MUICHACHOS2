cadena1 = "K uvo pue parse"
cadena2 = "Treinta hijueputa"
#dir devuelve la lista de atributos validos del objeto pasado
#dir(cadena1)

#las funciones se escriben como =  nombreDeLaFuncion(Parametros)
#los metodos se escriben como = parametro.metodo()
#upper pasa todas las cadenas en mayusculas
metodoUpper = cadena1.upper()
#lower pasa todas las cadenas en minusculas
metodoLower = cadena1.lower()
#capitalize pasa la primera letra de la cadena a mayuscula
metodoCapitalize = cadena1.capitalize()
#find te devuelve la pocicion de de la cadena que buscas es key sensitive y si no encuentra te devuelve -1
metodoFind = cadena1.find("parse")
#index funciona como find pero si no lo encuentra te devuelve un error
metodoIndex = cadena1.index("p")
#isnumeric funciona para ver si el dato es numerico
metodoIsNumeric = cadena1.isnumeric()
#isalpha funciona para ver si es alfanumerico los espacios no son alphanumeric o los caracteres especiales
metodoIsAlpha = cadena1.isalpha()
#count funciona para ver las coincidencias que hay
metodoCount = cadena1.count("a")
#len cuenta la longitud de caracteres de una cadena
metodoLeng = len(cadena1)
#startswith Verifica si la cadena empiesa con otra cadena al principio es key sensitive
metodoStartswith = cadena1.startswith("k")
#endswith Verifica si la cadena termina con otra cadena 
metodoEndswith = cadena1.endswith("k")
#replace remplasa caracteres de una cadena
metodoReplace = cadena1.replace("K", "KE")
#split devuel una lista hecha con una cadena remplazando un parametro de la cadena
metodoSplit = cadena1.split(" ")
print(metodoSplit)