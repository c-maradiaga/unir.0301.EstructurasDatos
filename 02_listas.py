lista = [3,1,0,-3,890,-2,45,-999]

#? la funcion sort() por default ordena de Menor a Mayor:
lista.sort()
print(lista)

#? para ordenar de Mayor a menor usamos el parametro reverse = True
lista.sort(reverse = True)
print(lista)

print("=" * 25)
#? Funcion pop() ---> Recibe el indide del elemento a Eliminar, lo elimina de la lista y lo devuelve como respuesta:
print(lista)
print(lista.pop(0))
print(lista)


