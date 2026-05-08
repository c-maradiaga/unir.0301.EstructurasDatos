lista = [1, 2, "Hola Mundo", 4, 5]

print(lista)

# print(lista[2])    

print(lista[:-1])
print(lista[:-2])
 
# insertanto en la lista:
lista.insert(1, "Insertado en la 1")

# inserta al final de la lista:
lista.append("Agregado al final")
print(lista)

# Lista dentro de listas:
lista.insert(2, ["Enero","Febrero", 1967])
print(lista)

# agregando una lista al final:\
lista.append(["Lunes","Martes","Miercoles"])

print(lista)

# agrega elementos tipo Lista  al final de la lista como elementos normales:
lista.extend(["Uno","Dos"])
print(lista)

# Eliminar elementos de la lista: (si hay varios elementos iguales, elimina el primero de izquierda a derecha)
lista.remove(5)
print(lista)

## Contar elementos en la lista: En este caso devuelve 0 aunque hay un elemento llamdo Lunes, este esta
## en dentro de otra lista y directamente como elemento en la lista llamada "lista"
print(lista.count('Lunes'))

##? En este caso, devuelve la cantidad de 1, ya que el elemento 'Uno' esta como elemento en "lista" y no
##? como un elemento en una sublista dentro de "lista"
print(lista.count('Uno'))


## Invertir los elementos en la lista, los que estan de primero pasan al final:
lista.reverse()
print(lista)

#! Ordenando elementos de la lista: Solo funciona si Todos los elementos de la lista son del mismo
#! tipo, de lo contrario da error:
## lista.sort() --> da errror>











