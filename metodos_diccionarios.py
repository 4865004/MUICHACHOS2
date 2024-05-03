diccionario = {
    "nombre" : "holiwis",
    "palabra" : "pendejo de mierda"
}
#keys devuelve las llaves del diccionario
metodoKeys = diccionario.keys()
#get devuelve el valor
metodoGet = diccionario.get("nombre")
#clear elimina todos los elementos del diccionario
#diccionario.clear()
#pop elimina un elemento del diccionario pero solo las llaves
diccionario.pop("nombre")
#items devuelve los items del diccionario
metodoItems = diccionario.items()
print(metodoItems)