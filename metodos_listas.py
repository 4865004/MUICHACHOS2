lista = ["hola","toy","aburrido","mano"]

#append sirve para agregar objetos a la lista
lista.append("ayudame")
#insert sirve para agregar un objeto a la lista con un indice especifico
lista.insert(5,"nms")
#extend agrega varios elementos a la lista
lista.extend([False,20,20,20])
#pop elimina un elemnto de la lista segun su indice
lista.pop(8)
#remove elimina un elemento de la lista segun su valor
lista.remove(20)
#sort ordena los elementos de forma acendente (si usamos el parametro reverse=True lo ordena de forma decendente)
#lista .sort()
#reverse  ordena los elementos al reves
#lista.reverse()
#clear elimina todos los elementos de la lista
#lista.clear()
print(lista)