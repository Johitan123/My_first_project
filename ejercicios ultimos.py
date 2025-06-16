   
# METODOS

#list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#list.append("o")  # Agrega un elemento al final de la lista
#print(list)

#list.insert(2, "@")  # Inserta un elemento en una posición específica
#print(list)

#list.extend(["e" "l", "m"])  # Agrega varios elementos al final de la lista
#print(list)

#list.remove("c")  # Elimina el primer elemento con el valor especificado
#print(list) 

#list.pop(-3) # Elimina el elemento en la posición especificada (en este caso, el tercer elemento desde el final)
#print(list)  # Imprime la lista después de eliminar el elemento

#list.clear()  # Elimina todos los elementos de la lista
#print(list)  # Imprime la lista vacía

#del list[1:3] # Elimina los elementos en el rango especificado (en este caso, los elementos en las posiciones 1 y 2)
#print(list)  # Imprime la lista después de eliminar los elementos en el rango


#print ("\nOrdenar una lista")
#numbers = [5, 3, 8, 1, 2]
#numbers.sort()  # Ordena la lista en orden ascendente
#print(numbers)  # Imprime la lista ordenada

#print("ordenar listas creando una NUEVA lista")
#sorted_numbers = sorted(numbers)  # Crea una nueva lista ordenada sin modificar la original
#print(sorted_numbers)  # Imprime la nueva lista ordenada

#print("ordenar una lista de cadenas de texto")
#words = ["Banana", "apple", "cherry"]
#sorted_words = sorted(words, key=str.lower)  # Ordena las palabras sin distinguir mayúsculas y minúsculas
#print(sorted_words)  # Imprime la lista de palabras ordenada

#print("ordenar listas creando una NUEVA lista")
#sorted_numbers = sort
# }(numbers)  # Crea una nueva lista ordenada sin modificar la original
#print(sorted_numbers)  # Imprime la nueva lista ordenada


# Mas metodos de listas
animals = ["dog", "cat", "elephant", "lion", "cat", "tiger"]
print(len(animals))  # Imprime la longitud de la lista
print(animals.count("cat")) # Cuenta cuántas veces aparece "cat" en la lista

print("cat" in animals)  # Verifica si "cat" está en la lista
print("giraffe" in animals)  # Verifica si "giraffe" no está en la lista




# Ejercicio 7: 
# Crear una lista de números del 1 al 5.
# Añade un número al final de la lista usando append.
# Inserta el número 10 en la segunda posición de la lista usando insert.
# Modifica el primer elemento de la lista para que sea 0.

print("\nEjercicio 7:")
lista_numeros = [1, 2, 3, 4, 5]
lista_numeros.append(6)  # Añade el número 6 al final de la lista
lista_numeros.insert(1, 10)  # Inserta el número 10 en la segunda posición
lista_numeros[0] = 0  # Modifica el primer elemento para que sea 0
print(lista_numeros)





# Ejercicio 8: Combinar y limpiar listas.
# Extiende la lista1 usando extend().
# Elimina la primera aprición del numero 1 en la lista2 usando remove().
# Elimina el elemento en el indice 2 de la lista1 usando pop(). Imprime el elemento eliminado.
# Limpia completamente la lista2 usando clear().


print("\nEjercicio 8:")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 1, 2]

lista1.extend(lista2)  # Extiende lista1 con los elementos de lista2
print("Lista1 después de extender:", lista1)

lista1.remove(1)  # Elimina la primera aparición del número 1 en lista2
print("Lista2 después de eliminar el primer número 1:", lista2)

elemento_eliminado = lista1.pop(2)  # Elimina el elemento en el índice 2 de lista1
print("Elemento eliminado de lista1:", elemento_eliminado)

lista2.clear()  # Limpia completamente lista2
print("Lista2 después de limpiar:", lista2)




import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 9

# Crea una lista con los siguientes numeros: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de menor a mayor usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Compruebe si el número 10 está en la lista usando in.

print("\nEjercicio 9:")
lista_numeros = [5, 2, 8, 1, 9, 4, 2]
lista_numeros.sort()  # Ordena la lista de menor a mayor
print("Lista ordenada:", lista_numeros)
print(lista_numeros.count(2)) # Cuenta cuántas veces aparece el número 2 en la lista
print(10 in lista_numeros)  # Comprueba si el número 10 está en la lista








# Ejercicio 10

listaoriginal = [1, 2, 3, 4, 5]
copi1 = listaoriginal.copy()  # Crea una copia de la lista original
print("Copia de la lista original:", copi1)

listaoriginal.insert(1,10)  # Modifica la lista original
print("Lista original después de añadir un elemento:", listaoriginal)

listaoriginal.pop(1) 

copi2 = list(listaoriginal) # Otra forma de crear una copia de la lista original
print("Otra copia de la lista original:", copi2)    

copi3 = listaoriginal[:]  # Otra forma de crear una copia de la lista original
print("Tercera copia de la lista original:", copi3)





import os
os.system('cls' if os.name == 'nt' else 'clear')


# METODOS CON LISTAS

lista1 = ["manzana", "BANANA", "cereza", "Melones", "kiwi"]
lista1.sort()  # Ordena la lista en orden alfabético
print("Lista ordenada en orden alfabético:", lista1)
lista1.sort(key=str.lower)  # Ordena la lista sin distinguir mayúsculas y minúsculas
print("Lista ordenada sin distinguir mayúsculas y minúsculas:", lista1)
lista1.reverse()  # Invierte el orden de los elementos en la lista
print("Lista invertida:", lista1)
lista1.sort(reverse=True)  # Ordena la lista en orden alfabético inverso
print("Lista ordenada en orden alfabético inverso:", lista1)
print(lista1.count("manzana"))  # Cuenta cuántas veces aparece "manzana" en la lista


# Ejercicio 12


