#? Las tuplas son inmutables, al contrario de las listas.
#? se definen igual que una lista, pero sin los corchetes:
tupla = 2,4,6, "Hola Mundo", "Enero", "Febrero", "Marzo", 1900,2010,2020

print(tupla)

#? El definir una tupla como arriba, se le llama "Empaquetado de Tupla"
#? El Desempaquetado de tuplas tambien se puede hacer:

a, b, c, d, e, f, g, h, i, j =  tupla
print(a, b, c, d)

#! da error, porque deben ser 4 variables, o lo que es lo mismo, deben haber tantas
#! variables como elementos tenga la tupla
#x, y, z =  tupla
#print(x, y, z)
print(c)

## Acceder a elementos de una tupla:
print(tupla[1:])
print("=="*20)
print(tupla[:2])

print(tupla[:5]) ## Definir un rango de elementos, desde el inicio hasta el indice 4 (5-1)
print(tupla[3:]) ## Desde el indice 3 hasta el final de la tupla
print(tupla[3:6]) ## Desde el indice 3 hasta el indice 5 (6-1)
print("=="*20)
print(tupla[-1]) ## Acceder al ultimo elemento de la tupla
print(tupla[-3:]) ## Acceder a los ultimos 3 elementos de la tupla
print("=="*20)
print(tupla[-5:-2]) ## Acceder a los elementos desde el indice -5 hasta el indice -3 ( -2-1)

print("=="*20)
## funciones de tuplas:
print(len(tupla)) ## Devuelve la cantidad de elementos de la tupla
print(tupla.count("Hola Mundo")) ## Devuelve la cantidad de veces que se repite un elemento en la tupla
print(tupla.index(1900)) ## Devuelve el indice de la primera aparicion de un elemento en la tupla




